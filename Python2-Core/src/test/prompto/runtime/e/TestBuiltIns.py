from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCharCodePoint(self):
        self.checkOutput("builtins/charCodePoint.pec")

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.checkOutput("builtins/dateMonth.pec")

    def testDateTimeDayOfMonth(self):
        self.checkOutput("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.checkOutput("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.checkOutput("builtins/dateTimeHour.pec")

    def testDateTimeMilli(self):
        self.checkOutput("builtins/dateTimeMilli.pec")

    def testDateTimeMinute(self):
        self.checkOutput("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.checkOutput("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.checkOutput("builtins/dateTimeSecond.pec")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.pec")

    def testDictCount(self):
        self.checkOutput("builtins/dictCount.pec")

    def testDictKeys(self):
        self.checkOutput("builtins/dictKeys.pec")

    def testDictValues(self):
        self.checkOutput("builtins/dictValues.pec")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.pec")

    def testListCount(self):
        self.checkOutput("builtins/listCount.pec")

    def testSetCount(self):
        self.checkOutput("builtins/setCount.pec")

    def testTextCapitalize(self):
        self.checkOutput("builtins/textCapitalize.pec")

    def testTextCount(self):
        self.checkOutput("builtins/textCount.pec")

    def testTextLowercase(self):
        self.checkOutput("builtins/textLowercase.pec")

    def testTextSplit(self):
        self.checkOutput("builtins/textSplit.pec")

    def testTextUppercase(self):
        self.checkOutput("builtins/textUppercase.pec")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.pec")

    def testTimeMilli(self):
        self.checkOutput("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.pec")

    def testTupleCount(self):
        self.checkOutput("builtins/tupleCount.pec")


