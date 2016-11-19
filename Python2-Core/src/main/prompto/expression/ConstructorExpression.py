from io import StringIO
from prompto.expression.IExpression import IExpression
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.type.DocumentType import DocumentType
from prompto.value.Document import Document
from prompto.value.IInstance import IInstance
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NotMutableError import NotMutableError

class ConstructorExpression(IExpression):

    def __init__(self, typ, assignments):
        self.copyFrom = None
        self.typ = typ
        self.setAssignments(assignments)

    def getType(self):
        return self.typ

    def setAssignments(self, assignments):
        self.assignments = assignments
        # in OOPS, first anonymous argument is copyFrom
        if assignments is not None and len(assignments)>0 and assignments[0].getArgument() is None:
            self.copyFrom = assignments[0].getExpression()
            self.assignments.pop(0)

    def getAssignments(self):
        return self.assignments

    def setCopyFrom(self, copyFrom):
        self.copyFrom = copyFrom

    def getCopyFrom(self):
        return self.copyFrom

    def __str__(self):
        with StringIO() as sb:
            if self.typ.mutable:
                sb.write("mutable ")
            sb.write(self.typ.getName())
            sb.write(' ')
            if self.copyFrom is not None:
                sb.write("(from:")
                sb.write(str(self.copyFrom))
                sb.write(") ")
            if self.assignments is not None:
                sb.write("with ")
                sb.write(str(self.assignments))
            return sb.getvalue()

    def toEDialect(self, writer):
        self.typ.toDialect(writer)
        if self.copyFrom is not None:
            writer.append(" from ")
            writer.append(str(self.copyFrom))
            if self.assignments is not None and len(self.assignments)>0:
                writer.append(",")
        if self.assignments is not None:
            self.assignments.toDialect(writer)

    def toODialect(self, writer):
        self.typ.toDialect(writer)
        assignments = ArgumentAssignmentList()
        if self.copyFrom is not None:
            from prompto.grammar.ArgumentAssignment import ArgumentAssignment
            assignments.append(ArgumentAssignment(None, self.copyFrom))
        if self.assignments is not None:
            assignments.extend(self.assignments)
        assignments.toDialect(writer)

    def toMDialect(self, writer):
        self.toODialect(writer)

    def check(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.typ.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.typ.getName())
        type = cd.getType(context)
        cd.checkConstructorContext(context)
        if self.copyFrom is not None:
            cft = self.copyFrom.check(context)
            if not isinstance(cft, (CategoryType, DocumentType)):
                raise SyntaxError("Cannot copy from " + cft.getName())
        if self.assignments is not None:
            for assignment in self.assignments:
                if not cd.hasAttribute(context, assignment.getName()):
                    raise SyntaxError("\"" + assignment.getName() +
                        "\" is not an attribute of " + self.typ.getName())
                assignment.check(context)
        return type

    def interpret(self, context):
        instance = self.typ.newInstance(context)
        instance.mutable = True
        if self.copyFrom is not None:
            copyObj = self.copyFrom.interpret(context)
            from prompto.declaration.CategoryDeclaration import CategoryDeclaration
            cd = context.getRegisteredDeclaration(CategoryDeclaration, self.typ.typeName)
            if isinstance(copyObj, IInstance):
                for name in copyObj.getMemberNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.getMember(context, name)
                        if value is not None and value.mutable and not self.typ.mutable:
                            raise NotMutableError()
                        instance.setMember(context, name, value)
            elif isinstance(copyObj, Document):
                for name in copyObj.getMemberNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.getMember(context, name)
                        if value is not None and value.mutable and not self.typ.mutable:
                            raise NotMutableError()
                        # TODO convert to attribute type
                        instance.setMember(context, name, value)
        if self.assignments is not None:
            for assignment in self.assignments:
                value = assignment.getExpression().interpret(context)
                if value is not None and value.mutable and not self.typ.mutable:
                    raise NotMutableError()
                instance.setMember(context, assignment.getName(), value)
        instance.mutable = self.typ.mutable
        return instance
