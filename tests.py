import unittest
from index import Banco

class testeBanco(unittest.TestCase):

    def testeDeposito(self):
        banco = Banco()
        self.assertEquals(banco.deposito(1000), True)

    def testeSaque(self):
        banco = Banco()
        banco.deposito(1000)
        self.assertEquals(banco.saque(100), True)


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(testeBanco)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()