from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOMO("singleton/attribute.poc")

    def testConstructor(self):
        self.compareResourceOMO("singleton/constructor.poc")

    def testInternal(self):
        self.compareResourceOMO("singleton/internal.poc")

    def testMember(self):
        self.compareResourceOMO("singleton/member.poc")


