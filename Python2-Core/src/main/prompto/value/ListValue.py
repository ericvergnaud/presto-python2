from io import StringIO

from prompto.value.BaseValueList import BaseValueList
from prompto.value.Integer import Integer
from prompto.error.SyntaxError import SyntaxError

class ListValue(BaseValueList):

    def __init__(self, itemType, items=None, item=None):
        from prompto.type.ListType import ListType
        super(ListValue, self).__init__(ListType(itemType), items)
        if item is not None:
            self.items.append(item)

    def newInstance(self, items):
        return ListValue(self.type.itemType, items=items)

    def setItem(self, index, element):
        self.items[index] = element

    def Add(self, context, value):
        from prompto.value.SetValue import SetValue
        from prompto.value.TupleValue import TupleValue
        if isinstance(value, (ListValue, TupleValue, SetValue)):
            return self.merge(value)
        else:
            return super(ListValue, self).Add(context, value)

    def Multiply(self, context, value):
        if isinstance(value, Integer):
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            elif count == 0:
                return ListValue(self.itemType)
            elif count == 1:
                return self
            else:
                result = []
                for i in range(1,count+1):
                    result.extend(self.items)
                return ListValue(self.type.itemType, items=result)
        else:
            raise SyntaxError("Illegal: List * " + type(value).__name__)

    def __str__(self):
        with StringIO() as sb:
            sb.write(u"[")
            for v in self.items:
                sb.write(unicode(v))
                sb.write(u", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len - 2)
            sb.write(u"]")
            return sb.getvalue()

	
