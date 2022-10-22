import unittest
import HtmlTestRunner
from Tema9 import Login


class TestSuite9(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
        ])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Primele teste", report_name="Ceva")
        runner.run(tests_to_run)
