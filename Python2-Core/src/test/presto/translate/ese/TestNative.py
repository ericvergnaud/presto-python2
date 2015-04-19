from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceESE("native/attribute.pec")

    def testCategory(self):
        self.compareResourceESE("native/category.pec")

    def testMethod(self):
        self.compareResourceESE("native/method.pec")

    def testPrinter(self):
        self.compareResourceESE("native/printer.pec")

    def testReturn(self):
        self.compareResourceESE("native/return.pec")


