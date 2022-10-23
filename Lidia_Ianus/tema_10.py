''' 1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).'''

import unittest
import HtmlTestRunner

from tema_9 import FirstTestcase

"""
Suita de teste : colectie de mai multe teste, pe care le putem rula impreuna.
"""


class TestSuite(unittest.TestCase):

    def test_suite(self):
        # Facem un obiect test suite
        tests_to_run = unittest.TestSuite()
        # In acest obiect adaugam toate testele pe care vrem sa le rulam
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FirstTestcase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(SignInTest)
        ])
        # Facem un obiect de tip html runner, ca sa ne si genereze rapoarte HTML
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Primele teste", report_name="Report from one folder")
        # Rulam toate testele
        runner.run(tests_to_run)