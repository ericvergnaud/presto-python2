# generated: 2015-07-05T23:01:01.471
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAutoDowncast(self):
        self.checkOutput("cast/autoDowncast.poc")

    def testCastChild(self):
        self.checkOutput("cast/castChild.poc")

    def testIsAChild(self):
        self.checkOutput("cast/isAChild.poc")

    def testIsAText(self):
        self.checkOutput("cast/isAText.poc")

