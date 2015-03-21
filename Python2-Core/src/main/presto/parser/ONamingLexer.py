from presto.parser.OLexer import OLexer
from presto.parser.Dialect import Dialect
from presto.parser.Utils import extractTokenNames


class ONamingLexer(OLexer):

	tokenNames = extractTokenNames(OLexer)

	@classmethod
	def getTokenName(cls, token=None, type_=None):
		if type_ is None:
			type_ = token.getType()
		return cls.tokenNames[type_]

	def __init__(self, input_):
		super(ONamingLexer, self).__init__(input_)

	def getDialect(self):
		return Dialect.O
