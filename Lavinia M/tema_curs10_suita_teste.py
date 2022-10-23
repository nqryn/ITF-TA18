import unittest
import HTMLTestRunner

from tema_curs9 import Login
from tema_curs10 import EdgeTestCase


class SuitaTeste(unittest.TestCase):

    def suita_teste(self):
        teste_de_rulat = unittest.TestSuite
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(EdgeTestCase)
        ])

        runner = HTMLTestRunner.HTMLTestRunner(report_name='Primul raport de testare', combined_reports=True)
        runner.run(SuitaTeste)
