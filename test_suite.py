#encoding:utf-8
import unittest
from module2 import TestModule1
from test_hello_add import TestHelloAdd

test_cases = (TestModule1,TestHelloAdd)

def whole_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

if __name__ == "__main__":
    # runner = unittest.TextTestRunner(verbosity=2)#①
    # runner.run(whole_suite())
    with open('test_report.txt','a') as f:
        runner = unittest.TextTestRunner(verbosity=2,stream=f)
    #     runner = unittest.TextTestRunner(verbosity=2)
        runner.run(whole_suite())