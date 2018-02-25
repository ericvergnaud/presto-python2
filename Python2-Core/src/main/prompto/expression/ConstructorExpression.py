from io import StringIO
from prompto.expression.IExpression import IExpression
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.type.DocumentType import DocumentType
from prompto.value.Document import Document
from prompto.value.IInstance import IInstance
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NotMutableError import NotMutableError

class ConstructorExpression(IExpression):

    def __init__(self, itype, copyFrom, assignments, checked):
        self.mutable = False
        self.itype = itype
        self.copyFrom = copyFrom
        self.assignments = assignments
        self.checked = checked

    def getType(self):
        return self.itype

    def getAssignments(self):
        return self.assignments

    def setCopyFrom(self, copyFrom):
        self.copyFrom = copyFrom

    def getCopyFrom(self):
        return self.copyFrom

    def __str__(self):
        with StringIO() as sb:
            if self.mutable:
                sb.write("mutable ")
            sb.write(self.itype.typeName)
            sb.write(' ')
            if self.copyFrom is not None:
                sb.write("(from:")
                sb.write(str(self.copyFrom))
                sb.write(") ")
            if self.assignments is not None:
                sb.write("with ")
                sb.write(str(self.assignments))
            return sb.getvalue()

    def toDialect(self, writer):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        cd = writer.context.getRegisteredDeclaration(CategoryDeclaration, self.itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.itype.typeName)
        self.checkFirstHomonym(writer.context, cd)
        super(ConstructorExpression, self).toDialect(writer)


    def toEDialect(self, writer):
        self.itype.toDialect(writer)
        if self.copyFrom is not None:
            writer.append(" from ")
            writer.append(str(self.copyFrom))
            if self.assignments is not None and len(self.assignments)>0:
                writer.append(",")
        if self.assignments is not None:
            self.assignments.toDialect(writer)


    def toODialect(self, writer):
        self.itype.toDialect(writer)
        assignments = ArgumentAssignmentList()
        if self.copyFrom is not None:
            from prompto.grammar.ArgumentAssignment import ArgumentAssignment
            from prompto.argument.AttributeArgument import AttributeArgument
            assignments.append(ArgumentAssignment(AttributeArgument("from"), self.copyFrom))
        if self.assignments is not None:
            assignments.extend(self.assignments)
        assignments.toDialect(writer)


    def toMDialect(self, writer):
        self.toODialect(writer)


    def checkFirstHomonym(self, context, decl):
        if self.checked:
            return
        if self.assignments is not None and len(self.assignments)>0:
            assign = self.assignments[0]
            if assign.argument is None:
                from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
                from prompto.expression.InstanceExpression import InstanceExpression
                name = assign.expression.name if isinstance(assign.expression, (UnresolvedIdentifier, InstanceExpression)) else None
                if name is not None and decl.hasAttribute(context, name):
                    from prompto.argument.AttributeArgument import AttributeArgument
                    assign.argument = AttributeArgument(name)
                    assign.expression = None
        self.checked = True


    def check(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.itype.typeName)
        self.checkFirstHomonym(context, cd)
        cd.checkConstructorContext(context)
        if self.copyFrom is not None:
            cft = self.copyFrom.check(context)
            if not isinstance(cft, (CategoryType, DocumentType)):
                raise SyntaxError("Cannot copy from " + cft.getName())
        if self.assignments is not None:
            for assignment in self.assignments:
                if not cd.hasAttribute(context, assignment.getName()):
                    raise SyntaxError("\"" + assignment.getName() +
                        "\" is not an attribute of " + self.itype.typeName)
                assignment.check(context)
        return cd.getType(context)

    def interpret(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.itype.typeName)
        self.checkFirstHomonym(context, cd)
        instance = self.itype.newInstance(context)
        instance.mutable = True
        if self.copyFrom is not None:
            copyObj = self.copyFrom.interpret(context)
            if isinstance(copyObj, IInstance):
                for name in copyObj.getMemberNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.getMemberValue(context, name)
                        if value is not None and value.mutable and not self.itype.mutable:
                            raise NotMutableError()
                        instance.setMember(context, name, value)
            elif isinstance(copyObj, Document):
                for name in copyObj.getMemberNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.getMemberValue(context, name)
                        if value is not None and value.mutable and not self.itype.mutable:
                            raise NotMutableError()
                        # TODO convert to attribute type
                        instance.setMember(context, name, value)
        if self.assignments is not None:
            for assignment in self.assignments:
                value = assignment.getExpression().interpret(context)
                if value is not None and value.mutable and not self.itype.mutable:
                    raise NotMutableError()
                instance.setMember(context, assignment.getName(), value)
        instance.mutable = self.itype.mutable
        return instance
