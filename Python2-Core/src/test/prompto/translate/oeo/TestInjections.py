# generated: 2015-07-05T23:01:01.556
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestInjections(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testExpressionInjection(self):
        self.compareResourceOEO("injections/expressionInjection.poc")

