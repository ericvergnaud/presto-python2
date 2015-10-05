from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.error.SyntaxError import SyntaxError

class NativeCategoryDeclaration ( ConcreteCategoryDeclaration ):

    def __init__(self, name, attributes, categoryBindings, attributeBindings, methods):
        super(NativeCategoryDeclaration, self).__init__(name, attributes)
        self.categoryBindings = categoryBindings
        self.attributeBindings = attributeBindings
        self.boundedClass = None
        self.methods = methods

    def __str__(self):
        return self.getName() + (":" + str(self.attributes)) if self.attributes is not None else ""

    def register(self, context):
        context.registerDeclaration(self)
        bounded = self.getBoundedClass(False)
        if bounded is not None:
            context.registerNativeBinding(bounded, self)

    def newInstance(self):
        from prompto.value.NativeInstance import NativeInstance
        return NativeInstance(self)

    def getBoundedClass(self, fail):
        if self.boundedClass is None:
            binding = self.getBinding(fail)
            if binding is not None:
                self.boundedClass = binding.interpret()
                if fail and self.boundedClass is None:
                    raise SyntaxError("No Python class:" + str(binding))
        return self.boundedClass

    def getBinding(self, fail):
        for binding in self.categoryBindings:
            from prompto.python.PythonNativeCategoryBinding import Python2NativeCategoryBinding
            if isinstance(binding, Python2NativeCategoryBinding):
                return binding
        if fail:
            raise SyntaxError("Missing Python2 binding !")
        else:
            return None

    def toEDialect(self, writer):
        self.protoToEDialect(writer, False, True)
        self.bindingsToEDialect(writer)
        if self.methods is not None and len(self.methods)>0:
            writer.append("and methods:")
            writer.newLine()
            self.methodsToEDialect(writer, self.methods)

    def categoryTypeToEDialect(self, writer):
        writer.append("native category")

    def bindingsToEDialect(self, writer):
        writer.indent()
        self.categoryBindings.toDialect(writer)
        writer.dedent()
        writer.newLine()

    def toODialect(self, writer):
        self.allToODialect(writer, True) # always has body;

    def categoryTypeToODialect(self, writer):
        writer.append("native category")

    def bodyToODialect(self, writer):
        self.categoryBindings.toDialect(writer)
        if self.methods is not None and len(self.methods)>0:
            writer.newLine()
            writer.newLine()
            self.methodsToODialect(writer, self.methods)

    def toSDialect(self, writer):
        self.protoToSDialect(writer, None)
        writer.indent()
        writer.newLine()
        self.categoryBindings.toDialect(writer)
        if self.methods is not None and len(self.methods)>0:
            for method in self.methods:
                w = writer.newMemberWriter()
                method.toDialect(w)
                writer.newLine()
        writer.dedent()
        writer.newLine()

    def categoryTypeToSDialect(self, writer):
        writer.append("native category")
