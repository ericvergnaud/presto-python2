# generated: 2015-07-05T23:01:01.658
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGetter(self):
        self.checkOutput("setters/getter.pec")

    def testGetterCall(self):
        self.checkOutput("setters/getterCall.pec")

    def testSetter(self):
        self.checkOutput("setters/setter.pec")

