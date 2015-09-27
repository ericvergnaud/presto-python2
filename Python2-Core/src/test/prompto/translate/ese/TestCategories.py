# generated: 2015-07-05T23:01:01.474
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceESE("categories/copyFromAscendant.pec")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceESE("categories/copyFromAscendantWithOverride.pec")

    def testCopyFromDescendant(self):
        self.compareResourceESE("categories/copyFromDescendant.pec")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceESE("categories/copyFromDescendantWithOverride.pec")

