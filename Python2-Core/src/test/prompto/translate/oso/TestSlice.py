# generated: 2015-07-05T23:01:01.674
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceOSO("slice/sliceList.poc")

    def testSliceRange(self):
        self.compareResourceOSO("slice/sliceRange.poc")

    def testSliceText(self):
        self.compareResourceOSO("slice/sliceText.poc")

