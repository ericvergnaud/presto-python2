from prompto.type.BooleanType import Boolean
from prompto.type.IterableType import IterableType


class ContainerType ( IterableType ) :

    def __init__(self, family, itemType):
        super(ContainerType, self).__init__(family, itemType)

    def checkContains(self, context, other):
        if self.itemType.isAssignableTo(context, other):
            return BooleanType.instance
        else:
            return super(ContainerType, self).checkContains(context, other)
