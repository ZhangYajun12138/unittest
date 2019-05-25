#coding=utf-8
import unittest
from hello_add import *

class TestHelloAdd(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(),'hello world')

    @unittest.skip(reason='临时跳过')
    def test_add(self):
        self.assertTrue(add(1,2) == 3)
        self.assertEqual(add(-2,5),3)
        self.assertEqual(add(-0.5,-0.3),-0.8)

    # def setUp(self) -> None:
    #     print('-----setUp-----')
    #
    # def tearDown(self) -> None:
    #     print('-----tearDown-----')
    @classmethod
    def setUpClass(cls) -> None:
        print('-----setupclass-----')
    @classmethod
    def tearDownClass(cls) -> None:
        print('-----teardownclass-----')

if __name__ =='__main__':
    unittest.main(verbosity=2)