# generated: 2015-07-05T23:01:01.479
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceEOE("closures/globalClosureNoArg.pec")

    def testGlobalClosureWithArg(self):
        self.compareResourceEOE("closures/globalClosureWithArg.pec")

    def testInstanceClosureNoArg(self):
        self.compareResourceEOE("closures/instanceClosureNoArg.pec")

