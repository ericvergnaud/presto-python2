from presto.error.NullReferenceError import NullReferenceError
from presto.parser.Dialect import Dialect
from presto.python.PythonNativeCall import Python2NativeCall
from presto.statement.SimpleStatement import SimpleStatement
from presto.type.TypeMap import TypeMap
from presto.type.VoidType import VoidType


class StatementList(list):

    def __init__(self, statement=None):
        super(StatementList, self).__init__()
        if statement != None:
            self.append(statement)

    def check(self, context, nativeOnly=False):
        types = TypeMap()
        for statement in self:
            if nativeOnly and not isinstance(statement, Python2NativeCall):
                continue
            type_ = statement.check(context)
            if type_ != VoidType.instance:
                types[type_.getName()] = type_
        return types.inferType(context)

    def interpret(self, context):
        try:
            return self.doInterpret(context)
        except ReferenceError:
            raise NullReferenceError()

    def doInterpret(self, context):
        for statement in self:
            context.enterStatement(statement)
            try:
                result = statement.interpret(context)
                if result is not None:
                    return result
            finally:
                context.leaveStatement(statement)
        return None

    def interpretNative(self, context, returnType):
        try:
            return self.doInterpretNative(context, returnType)
        except ReferenceError:
            raise NullReferenceError()

    def doInterpretNative(self, context, returnType):
        for statement in self:
            if not isinstance(statement, Python2NativeCall):
                continue
            context.enterStatement(statement)
            try:
                result = statement.interpret(context, returnType)
                if result is not None:
                    return result
            finally:
                context.leaveStatement(statement)
        return None

    def toDialect(self, writer):
        for statement in self:
            statement.toDialect(writer)
            if isinstance(statement, SimpleStatement):
                if writer.dialect is Dialect.O:
                    writer.append(';')
                writer.newLine()
