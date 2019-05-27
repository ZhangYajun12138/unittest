#coding:utf-8
# 习题17:更多文件操作
from sys import argv
from os.path import exists
(script,from_flie,to_file) = argv
print("Copying from %s to %s." %(from_flie,to_file))
input_file = open(from_flie) # 打开源文件
indata = input_file.read() # 获取源文件内容
print("The input file is %d bytes long." %len(indata))
print("Does the output file exist? %r" %exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input("please input:")

output = open(to_file,"w") # 打开目标文件
output.write(indata) # 将源文件内容写入目标文件
print("Alright, all done.")
input_file.close() # 关闭源文件
output.close() # 关闭目标文件