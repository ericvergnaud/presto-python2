# generated: 2015-07-05T23:01:01.707
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceEOE("tuples/multiAssignment.pec")

    def testSingleAssignment(self):
        self.compareResourceEOE("tuples/singleAssignment.pec")

    def testTupleElement(self):
        self.compareResourceEOE("tuples/tupleElement.pec")

