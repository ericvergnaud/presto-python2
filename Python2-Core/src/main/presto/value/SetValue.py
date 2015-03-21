from presto.error.IndexOutOfRangeError import IndexOutOfRangeError
from presto.error.SyntaxError import SyntaxError
from presto.value.BaseValue import BaseValue
from presto.value.IContainer import IContainer
from presto.value.Integer import Integer
from io import StringIO

class SetValue(BaseValue, IContainer):

    def __init__(self, itemType, items = None):
        from presto.type.SetType import SetType
        super(SetValue, self).__init__( SetType(itemType))
        self.items = items if items is not None else set()

    def isEmpty(self):
        return len(self.items)==0

    def __len__(self):
        return len(self.items)

    def getItems(self, context=None):
        for item in self.items:
            yield item

    def hasItem(self, context, item):
        return item in self.items

    def getItem(self, context, index):
        if isinstance(index, Integer):
            idx = index.IntegerValue()
            for item in self.items:
                idx -= 1
                if idx==0:
                    return item
            raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + index.toString())


    def __eq__(self, obj):
        if not isinstance(obj, SetValue):
            return False
        return self.items==obj.items


    def __str__(self):
        with StringIO() as sb:
            sb.write(u"<")
            for v in self.items:
                sb.write(unicode(v))
                sb.write(u", ")
            len = sb.tell()
            if len > 2:
                sb.truncate(len - 2)
                sb.seek(len-2)
            sb.write(u">")
            return sb.getvalue()

    def Add(self, context, value):
        if isinstance(value, IContainer):
            return self.merge(value.items)
        else:
            raise SyntaxError("Illegal: " + self.type.name + " + " + type(value).__name__)


    def merge(self, items):
        data = set()
        data |= self.items
        data |= items
        return SetValue(self.type.itemType, data)
