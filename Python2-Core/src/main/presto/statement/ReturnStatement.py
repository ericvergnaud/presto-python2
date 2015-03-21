from presto.type.VoidType import VoidType
from presto.runtime.VoidResult import VoidResult
from presto.statement.SimpleStatement import SimpleStatement


class ReturnStatement ( SimpleStatement ):

    def __init__(self, expression):
        super(ReturnStatement, self).__init__()
        self.expression = expression

    def getExpression(self):
        return self.expression

    def __str__(self):
        return "return " + str(self.expression)

    def toDialect(self, writer):
        writer.append("return ")
        if self.expression is not None:
            writer.append(" ")
            self.expression.toDialect(writer)

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, ReturnStatement):
            return False
        exp = self.expression
        other = obj.expression
        if id(exp)==id(other):
            return True
        elif exp is None or other is None:
            return False
        else:
            return exp==other

    def check(self, context):
        if self.expression is None:
            return VoidType.instance
        else:
            return self.expression.check(context)

    def interpret(self, context):
        if self.expression is None:
            return VoidResult.instance
        else:
            return self.expression.interpret(context)
