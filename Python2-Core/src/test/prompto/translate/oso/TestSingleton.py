# generated: 2015-07-05T23:01:01.667
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOSO("singleton/attribute.poc")

    def testMember(self):
        self.compareResourceOSO("singleton/member.poc")

