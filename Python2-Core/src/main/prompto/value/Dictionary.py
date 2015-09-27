from io import StringIO

from prompto.error.InternalError import InternalError
from prompto.expression.IExpression import IExpression
from prompto.type.TextType import TextType
from prompto.type.DictType import DictType
from prompto.type.MissingType import MissingType
from prompto.value.BaseValue import BaseValue
from prompto.value.IContainer import IContainer
from prompto.value.IValue import IValue
from prompto.value.Integer import Integer
from prompto.value.ListValue import ListValue


class Dictionary(BaseValue, IContainer):

    @staticmethod
    def merge(dict1, dict2):
        return Dictionary(dict1.type.itemType, value=dict(dict1.value.items() + dict2.value.items()))

    def __init__(self, itemType, copyFrom=None, value=None):
        super(Dictionary, self).__init__(DictType(itemType))
        if copyFrom != None:
            self.value = copyFrom.value
        elif value != None:
            self.value = value
        else:
            self.value = dict()

    def size(self):
        return len(self.value)


    def isEmpty(self):
        return len(self.value) == 0


    def Add(self, context, value):
        if isinstance(value, Dictionary):
            return Dictionary.merge(self, value)
        else:
            raise SyntaxError("Illegal: Dict + " + type(value).__name__)


    def hasItem(self, context, value):
        from prompto.value.Text import Text
        if isinstance(value, Text):
            return self.value.get(value.value, None) is not None
        else:
            raise SyntaxError("Only Text key is supported by " + type(self).__name__)


    def GetMember(self, context, name):
        if "length" == name:
            return Integer(self.size())
        elif "keys" == name:
            from prompto.value.Text import Text
            res = [Text(k) for k in self.value.keys()]
            return ListValue(TextType.instance, items=res)
        elif "values" == name:
            return ListValue(self.type.itemType, items=self.value.values())
        else:
            raise SyntaxError("No such member:" + name)

    def getItem(self, context, item):
        from prompto.value.Text import Text
        if isinstance(item, Text):
            value = self.value.get(item.value, None)
            if isinstance(value, IValue):
                return value
            else:
                raise InternalError("Item not a value!")
        else:
            raise SyntaxError("No such item:" + str(item))


    def ConvertTo(self, type_):
        return self


    def __eq__(self, obj):
        if not isinstance(obj, Dictionary):
            return False
        return self.value == obj.value


    def __str__(self):
        with StringIO() as sb:
            sb.write(u"{")
            for k, v in self.value.items():
                sb.write(unicode(k))
                sb.write(u":")
                sb.write(unicode(v))
                sb.write(u", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len - 2)
            sb.write(u"}")
            return sb.getvalue()

    def getKeys(self):
        from prompto.value.Text import Text
        for k in self.value.iterkeys():
            yield Text(k)


    def getItems(self, context):
        for k, v in self.value.iteritems():
            yield KVPValue(k, v)


class KVPValue(BaseValue):

    def __init__(self, key, value):
        super(KVPValue, self).__init__(MissingType.instance)
        from prompto.value.Text import Text
        self.key = Text(key)
        self.value = value

    def GetMember(self, context, name):
        if "key" == name:
            return self.key
        elif "value" == name:
            value = self.value
            if isinstance(value, IExpression):
                value = value.interpret(context)
            return value
        else:
            raise SyntaxError("No such member:" + name)