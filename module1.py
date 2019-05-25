# # coding:utf-8
# '''
# module 1 包含以下内容：
#     my_book:字符串
#     say_hi：函数
#     User：类
# '''
# print('这是module 1')
# my_book = 'python'
# def say_hi(user):
#     print('%s welcome'%user)
# def say_hi2(user):
#     print('%s welcome'%user)
# class User:
#     def __init__(self,name):
#         self.name = name
#     def walk(self):
#         print('%s is walking'%self.name)
#     def __repr__(self):
#         return 'User[name='+self.name+']'
#
# __all__ = ['my_book','say_hi','User']
#
# def test_my_book():
#     print(my_book)
# def test_say_hi():
#     say_hi('zhang')
#     say_hi(User('yajun'))
# def test_User():
#     u = User('luzong')
#     u.walk()
#     print(u)
#
# if __name__ == '__main__':
#     test_my_book()
#     test_say_hi()
#     test_User()
import math
def one_equation(a,b):
    '''
    求一元二次方程a*x + b = 0的解
    :param a: 方程式中变量的系数
    :param b: 方程式中的常量
    :return: 方程式的解
    '''
    if a == 0:
        raise ValueError('参数错误')
    else:
        # return b/a
        return -b/a

def two_equation(a,b,c):
    '''
    求一元二次方程式a*x*x + b*x + c = 0的解
    :param a: 方程式中变量二次幂的系数
    :param b: 方程式中变量的系数
    :param c: 方程式中的常量
    :return: 方程式的根
    '''
    if a == 0:
        raise ValueError('参数错误')
    elif b*b - 4*a*c < 0:
        raise ValueError("方程式在有理数范围内无解")
    elif b*b - 4*a*c == 0:
        return -b/(2*a)
    else:
        r1 = (-b + (b*b -4*a*c)**0.5)/(2*a)
        r2 = (-b - (b*b -4*a*c)**0.5)/(2*a)
        return (r1,r2)
