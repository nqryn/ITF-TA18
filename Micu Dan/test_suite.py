import unittest
import HtmlTestRunner


from .tema_curs9 import TestCaseCurs9
from .automation_practice_tests import TestsEdge


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCaseCurs9),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestsEdge)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Primele teste", report_name="DanTestSuite")
        runner.run(tests_to_run)
