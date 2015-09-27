# generated: 2015-07-05T23:01:01.468
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAutoDowncast(self):
        self.checkOutput("cast/autoDowncast.pec")

    def testCastChild(self):
        self.checkOutput("cast/castChild.pec")

    def testIsAChild(self):
        self.checkOutput("cast/isAChild.pec")

    def testIsAText(self):
        self.checkOutput("cast/isAText.pec")

