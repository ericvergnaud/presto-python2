# generated: 2015-07-05T23:01:01.489
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOSO("condition/complexIf.poc")

    def testElseIf(self):
        self.compareResourceOSO("condition/elseIf.poc")

    def testReturnIf(self):
        self.compareResourceOSO("condition/returnIf.poc")

    def testSimpleIf(self):
        self.compareResourceOSO("condition/simpleIf.poc")

    def testSwitch(self):
        self.compareResourceOSO("condition/switch.poc")

    def testTernary(self):
        self.compareResourceOSO("condition/ternary.poc")

