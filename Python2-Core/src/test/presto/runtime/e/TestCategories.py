from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCopyFromAscendant(self):
        self.checkOutput("categories/copyFromAscendant.e")

    def testCopyFromAscendantWithOverride(self):
        self.checkOutput("categories/copyFromAscendantWithOverride.e")

    def testCopyFromDescendant(self):
        self.checkOutput("categories/copyFromDescendant.e")

    def testCopyFromDescendantWithOverride(self):
        self.checkOutput("categories/copyFromDescendantWithOverride.e")


