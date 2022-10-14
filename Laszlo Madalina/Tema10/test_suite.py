import unittest
import HtmlTestRunner

# from tema9 import MyTestCase
# from test_automation_jules_app_sign_in import SignInTest
from test_automation_shop_app_chrome import ShopTestCase
from test_automation_shop_app_safari import ShopTestCaseSafari
from test_automation_shop_app_edge import ShopTestCaseEdge


class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            # unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(SignInTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(ShopTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(ShopTestCaseSafari),
            unittest.defaultTestLoader.loadTestsFromTestCase(ShopTestCaseEdge)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='Testele dupa corectari',
                                               report_name='Raport teste')
        runner.run(tests_to_run)
