from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceOMO("builtins/dateDayOfMonth.poc")

    def testDateDayOfYear(self):
        self.compareResourceOMO("builtins/dateDayOfYear.poc")

    def testDateMonth(self):
        self.compareResourceOMO("builtins/dateMonth.poc")

    def testDateTimeDayOfMonth(self):
        self.compareResourceOMO("builtins/dateTimeDayOfMonth.poc")

    def testDateTimeDayOfYear(self):
        self.compareResourceOMO("builtins/dateTimeDayOfYear.poc")

    def testDateTimeHour(self):
        self.compareResourceOMO("builtins/dateTimeHour.poc")

    def testDateTimeMinute(self):
        self.compareResourceOMO("builtins/dateTimeMinute.poc")

    def testDateTimeMonth(self):
        self.compareResourceOMO("builtins/dateTimeMonth.poc")

    def testDateTimeSecond(self):
        self.compareResourceOMO("builtins/dateTimeSecond.poc")

    def testDateTimeTZName(self):
        self.compareResourceOMO("builtins/dateTimeTZName.poc")

    def testDateTimeTZOffset(self):
        self.compareResourceOMO("builtins/dateTimeTZOffset.poc")

    def testDateTimeYear(self):
        self.compareResourceOMO("builtins/dateTimeYear.poc")

    def testDateYear(self):
        self.compareResourceOMO("builtins/dateYear.poc")

    def testDictCount(self):
        self.compareResourceOMO("builtins/dictCount.poc")

    def testEnumName(self):
        self.compareResourceOMO("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.compareResourceOMO("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.compareResourceOMO("builtins/enumValue.poc")

    def testListCount(self):
        self.compareResourceOMO("builtins/listCount.poc")

    def testSetCount(self):
        self.compareResourceOMO("builtins/setCount.poc")

    def testTextCount(self):
        self.compareResourceOMO("builtins/textCount.poc")

    def testTimeHour(self):
        self.compareResourceOMO("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.compareResourceOMO("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.compareResourceOMO("builtins/timeSecond.poc")

    def testTupleCount(self):
        self.compareResourceOMO("builtins/tupleCount.poc")


