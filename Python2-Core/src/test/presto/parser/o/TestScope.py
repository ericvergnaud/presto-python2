from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.error.SyntaxError import SyntaxError
from presto.declaration.IDeclaration import IDeclaration
from presto.declaration.AttributeDeclaration import AttributeDeclaration
from presto.declaration.CategoryDeclaration import CategoryDeclaration
from presto.runtime.Context import MethodDeclarationMap

class TestScope(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()

    def testAttribute(self):
        self.assertIsNone(self.context.getRegisteredDeclaration(IDeclaration, "id"))
        stmts = self.parseString("attribute id: Integer;")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
        actual = self.context.getRegisteredDeclaration(IDeclaration, "id")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, AttributeDeclaration)
        try:
            stmts.register(self.context)
            self.fail()
        except SyntaxError:
            pass


    def testCategory(self):
        self.assertIsNone(self.context.getRegisteredDeclaration(IDeclaration, "Person"))
        stmts = self.parseString("category Person(id, name);")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
        actual = self.context.getRegisteredDeclaration(IDeclaration, "Person")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, CategoryDeclaration)
        try:
            stmts.register(self.context)
            self.fail()
        except SyntaxError:
            pass


    def testMethod(self):
        self.assertIsNone(self.context.getRegisteredDeclaration(IDeclaration, "printName"))
        stmts = self.parseString("attribute name: Text;"
                                 + "method printName( name ) {"
                                 + "print (value=name); }")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
        actual = self.context.getRegisteredDeclaration(IDeclaration, "printName")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, MethodDeclarationMap)
        stmts = self.parseString("method printName (Person p ) {"
                                 + "print (value = \"person\" + p.name ); } ")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
