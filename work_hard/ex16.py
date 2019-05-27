#coding:utf-8
'''
close -----关闭文件
read -----读取文件内容，返回一个值
readline -----读取文本文件中的一行
truncate -----清空文件
write(stuff) -----将stuff写入文件
'''
from sys import argv
(script,filename) = argv
print("We are going to erase %r." %filename)
print("If you don't want that, hit CTRL-C.")
print("IF you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename,"w")
print("Truncating the file. Goodbye.")
target.truncate() # 清空内容
print("Now I'm going to ask you for three lines.")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")
print("I'm going to wtite these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()

# python D:\张亚军\WEB测试\学习了\单元测试\unittest\work_hard\ex16.py D:\张亚军\WEB测试\学习了\单元测试\unittest\work_hard\ex16_sample.txt