from presto.error.ExecutionError import ExecutionError
from presto.literal.TextLiteral import TextLiteral


class InvalidDataError(ExecutionError):

    def __init__(self, message):
        super(InvalidDataError, self).__init__(message)

    def getExpression(self, context):
        s = self.message.replace('"',"'") # ensure TextLiteral interprets the full string
        return TextLiteral('"' + s + '"')
