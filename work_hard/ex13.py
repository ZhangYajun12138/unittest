#coding=utf-8
from sys import argv
# (script,first,second) = argv
# third = input("Please input:")
# print("The script is calld:",script)
# print("Your first variable is:",first)
# print("Your second variable is:",second)
# print("Your third variable is:",third)

# 在命令模式下执行 python ex13.py 1st 2nd 3rd

#习题14
from sys import argv
(script,user_name) = argv
prompt = '> '
print("Hi %s,I'm the %s script." %(user_name,script))
print("I'd like to ask you a few question.")
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("Where do you live %s?" %user_name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("""
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.Nice.
""" %(likes,lives,computer))

# 在命令模式下执行 python ex13.py zhang