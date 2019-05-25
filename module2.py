# from module1 import *
# print(my_book)
# say_hi('zhang')
# # say_hi2('zhang')
#
# user = User('yajun')
# print(user)
# user.walk()
# import fk_package
# import string
# print([e for e in dir(string) if not e.startswith('__')])
# print(string.__all__)
# i = fk_package.billing.Item(5)
# print(i)
# help(range)
# import sys
# import os
# import time
# # print(os.name)
# # print(os.getppid())
# # print(os.cpu_count())
# # os.startfile('d:\\test.txt')
# import time
# # 将当前时间转换为时间字符串
# print(time.asctime())
# # 将指定时间转换时间字符串，时间元组的后面3个元素没有设置
# print(time.asctime((2018, 2, 4, 11, 8, 23, 0, 0 ,0))) # Mon Feb  4 11:08:23 2018
# # 将以秒数为代表的时间转换为时间字符串
# print(time.ctime(30)) # Thu Jan  1 08:00:30 1970
# # 将以秒数为代表的时间转换为struct_time对象。
# print(time.gmtime(30))
# # 将当前时间转换为struct_time对象。
# print(time.gmtime())
# # 将以秒数为代表的时间转换为代表当前时间的struct_time对象
# print(time.localtime(30))
# # 将元组格式的时间转换为秒数代表的时间
# print(time.mktime((2018, 2, 4, 11, 8, 23, 0, 0 ,0))) # 1517713703.0
# # 返回性能计数器的值
# print(time.perf_counter())
# # 返回当前进程使用CPU的时间
# print(time.process_time())
# #time.sleep(10)
# # 将当前时间转换为指定格式的字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# st = '2018年3月20日'
# # 将指定时间字符串恢复成struct_time对象。
# print(time.strptime(st, '%Y年%m月%d日'))
# # 返回从1970年1月1日0点整到现在过了多少秒。
# print(time.time())
# # 返回本地时区的时间偏移，以秒为单位
# print(time.timezone) # 在国内东八区输出-28800

import unittest
from module1 import *

class TestModule1(unittest.TestCase):
    def test_one_equation(self):
        self.assertEqual(one_equation(a=5,b=9),-1.8)
        self.assertTrue(one_equation(4,10) == -2.5,msg=-0.00001)
        self.assertTrue(one_equation(4,-27) == 27/4)
        with self.assertRaises(ValueError):
            one_equation(0,9)

    def test_two_equation(self):
        (r1,r2) =two_equation(1,-3,2)
        self.assertCountEqual((r1,r2),(1.0,2.0),'求解出错')
        (r1, r2) = two_equation(2, -7, 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        r = two_equation(1,-4,4)
        self.assertEqual(r,2.0,"求解出错")
        with self.assertRaises(ValueError):
            two_equation(0,9,3)
        with self.assertRaises(ValueError):
            two_equation(4,1,10)

if __name__ == '__main__':
    unittest.main()