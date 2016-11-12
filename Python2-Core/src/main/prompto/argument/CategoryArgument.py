from prompto.argument.BaseArgument import BaseArgument
from prompto.argument.ITypedArgument import ITypedArgument


class CategoryArgument(BaseArgument, ITypedArgument):

    def __init__(self, typ, name):
        super(CategoryArgument, self).__init__(name)
        self.typ = typ

    def getSignature(self, dialect):
        return self.getProto()

    def getProto(self):
        return self.typ.typeName

    def __str__(self):
        return self.name + ':' + self.getProto()

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, CategoryArgument):
            return False
        return self.getType() == obj.getType() \
            and self.getName() == obj.getName()

    def register(self, context):
        from prompto.grammar.INamedValue import INamedValue
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        context.registerValue(self)
        if self.defaultExpression is not None:
            context.setValue(self.name, self.defaultExpression)

    def check(self, context):
        self.typ.checkExists(context)

    def getType(self, context=None):
            return self.typ

    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        super(CategoryArgument, self).toDialect(writer)
        if self.defaultExpression is not None:
            writer.append(" = ")
            self.defaultExpression.toDialect(writer)


    def toEDialect(self, writer):
        self.typ.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)


    def toODialect(self, writer):
        self.typ.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)

    def toSDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.typ.toDialect(writer)
