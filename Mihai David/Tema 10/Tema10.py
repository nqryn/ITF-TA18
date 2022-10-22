import unittest
import HtmlTestRunner
from Tema9 import Login


class TestSuite9(unittest.TestCase):

    def test_suite(self):
        # Facem un obiect test suite
        tests_to_run = unittest.TestSuite()
        # In acest obiect adaugam toate testele pe care vrem sa le rulam
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
        ])
        # Facem un obiect de tip html runner, ca sa ne si genereze rapoarte HTML
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Primele teste", report_name="Ceva")
        # Rulam toate testele
        runner.run(tests_to_run)