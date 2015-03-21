from presto.error.InternalError import InternalError
from presto.error.InvalidResourceError import InvalidResourceError
from presto.error.NullReferenceError import NullReferenceError
from presto.expression.IExpression import IExpression
from presto.type.ResourceType import ResourceType
from presto.type.TextType import TextType
from presto.value.IResource import IResource
from presto.error.SyntaxError import SyntaxError

class ReadExpression ( IExpression ) :

    def __init__(self, resource):
        super(ReadExpression, self).__init__()
        self.resource = resource

    def __str__(self):
        return "read from " + str(self.resource)

    def check(self, context):
        context = context.newResourceContext()
        sourceType = self.resource.check(context)
        if not isinstance(sourceType, ResourceType):
            raise SyntaxError("Not a readable resource!")
        return TextType.instance

    def interpret(self, context):
        context = context.newResourceContext()
        o = self.resource.interpret(context)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, IResource):
            raise InternalError("Illegal read source: " + o)
        if not o.isReadable():
            raise InvalidResourceError("Not readable")
        return o.readFully()

    def toDialect(self, writer):
        writer.append("read from ")
        self.resource.toDialect(writer)
