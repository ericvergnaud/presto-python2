from prompto.store.TypeFamily import TypeFamily
from prompto.type.BaseType import BaseType


class PropertiesType(BaseType):

    def __init__(self, properties):
        super(PropertiesType, self).__init__(TypeFamily.PROPERTIES)
        self.properties = properties

    def getMemberMethods(self, context, name):
        prop = self.properties.get(name, None)
        return super(PropertiesType, self).getMemberMethods(context, name) if prop is None else prop.validator.getMethodDeclarations(context)

