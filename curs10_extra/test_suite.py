import unittest
import HtmlTestRunner

from my_test_case_copy import MyTestCase
from test_automation_jules_app_sign_in import SignInTest

"""
Suita de teste : colectie de mai multe teste, pe care le putem rula impreuna.
"""


class TestSuite(unittest.TestCase):

    def test_suite(self):
        # Facem un obiect test suite
        tests_to_run = unittest.TestSuite()
        # In acest obiect adaugam toate testele pe care vrem sa le rulam
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(SignInTest)
        ])
        # Facem un obiect de tip html runner, ca sa ne si genereze rapoarte HTML
        runner = HtmlTestRunner.HTMLTestRunner(report_title="Primele teste", report_name="Ceva")
        # Rulam toate testele
        runner.run(tests_to_run)
