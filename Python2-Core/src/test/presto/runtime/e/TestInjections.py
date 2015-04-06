from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestInjections(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testExpressionInjection(self):
        self.checkOutput("injections/expressionInjection.pec")


