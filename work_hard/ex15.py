#coding:utf-8
# 习题15：读取文件
from sys import argv
(script,filename) = argv
txt = open(filename)
print("Here's your file %r:" %filename)
print(txt.read())
txt.close()
print("Type the filenam again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()

# python D:\张亚军\WEB测试\学习了\单元测试\unittest\work_hard\ex15.py \
# D:\张亚军\WEB测试\学习了\单元测试\unittest\work_hard\ex15_sample.txt
