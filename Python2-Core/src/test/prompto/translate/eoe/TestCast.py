# generated: 2015-07-05T23:01:01.466
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceEOE("cast/autoDowncast.pec")

    def testCastChild(self):
        self.compareResourceEOE("cast/castChild.pec")

    def testIsAChild(self):
        self.compareResourceEOE("cast/isAChild.pec")

    def testIsAText(self):
        self.compareResourceEOE("cast/isAText.pec")

