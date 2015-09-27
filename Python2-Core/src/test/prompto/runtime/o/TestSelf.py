# generated: 2015-07-05T23:01:01.653
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSelf(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSelfAsParameter(self):
        self.checkOutput("self/selfAsParameter.poc")

    def testSelfMember(self):
        self.checkOutput("self/selfMember.poc")

