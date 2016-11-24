from prompto.argument.CategoryArgument import CategoryArgument
from prompto.error.SyntaxError import SyntaxError



class ExtendedArgument(CategoryArgument):
    def __init__(self, type_, name, attributes):
        super(ExtendedArgument, self).__init__(type_, name)
        self.attributes = attributes



    def setAttributes(self, attributes):
        self.attributes = attributes



    def getProto(self):
        return self.type_.typeName + '(' + str(self.attributes) + ')'



    def hasAttributes(self):
        return self.attributes is not None



    def getAttributes(self):
        return self.attributes



    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, ExtendedArgument):
            return False
        return self.getType() == obj.getType() \
               and self.getName() == obj.getName() \
               and self.getAttributes() == obj.getAttributes()



    def register(self, context):
        from prompto.grammar.INamedValue import INamedValue
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from prompto.grammar.IdentifierList import IdentifierList
        declaration = ConcreteCategoryDeclaration(self.name)
        declaration.setDerivedFrom(IdentifierList(self.type_.typeName))
        declaration.setAttributes(self.attributes)
        context.registerDeclaration(declaration)
        context.registerValue(self)
        if self.defaultExpression is not None:
            value = self.defaultExpression.interpret(context)
            context.setValue(self.name, value)



    def check(self, context):
        self.type_.checkExists(context)
        for attribute in self.attributes:
            from prompto.declaration.AttributeDeclaration import AttributeDeclaration
            actual = context.getRegisteredDeclaration(AttributeDeclaration, attribute)
            if actual is None:
                raise SyntaxError("Unknown attribute: \"" + attribute + "\"")



    def getType(self, context=None):
        from prompto.declaration.IDeclaration import IDeclaration
        return self.type_ if context is None else context.getRegisteredDeclaration(IDeclaration, self.name).getType(
            context)



    def toEDialect(self, writer):
        self.type_.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)
        if len(self.attributes) == 1:
            writer.append(" with attribute ")
            self.attributes.toDialect(writer, False)
        elif len(self.attributes) > 1:
            writer.append(" with attributes ")
            self.attributes.toDialect(writer, True)



    def toODialect(self, writer):
        self.type_.toDialect(writer)
        writer.append('(')
        self.attributes.toDialect(writer, False)
        writer.append(')')
        writer.append(' ')
        writer.append(self.name)



    def toMDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.type_.toDialect(writer)
        writer.append('(')
        self.attributes.toDialect(writer, False)
        writer.append(')')
