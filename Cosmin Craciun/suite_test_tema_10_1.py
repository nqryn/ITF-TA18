import unittest
import HTMLTestRunner

from tema_9_obligatorie_verificatori import InternetHero
from tema_10_test_alerts import EdgeTestCase


class TestSuit(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(InternetHero),
            unittest.defaultTestLoader.loadTestsFromTestCase(EdgeTestCase)
        ])

        runner = HTMLTestRunner.HTMLTestRunner(report_name='First report of test runner', tested_by="Cosmin Craciun")
        runner.run(tests_to_run)
