#coding:utf-8

#习题1
# print('Hello World!',end='')
# print('Hello Again')
# print('Hens',25+30/6)

#习题2
# cars = 100
# space_in_a_car = 4
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
# print('There are',cars,'cars available.')
# print('There are only',drivers,'drivers available.')
# print('There will be',cars_not_driven,'empty cars today.')
# print('We can transport',carpool_capacity,'people today.')
# print('We have',passengers,'to carpool today.')
# print('We need to put about',average_passengers_per_car,'in each car.')

#习题5
# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74
# my_weight = 180
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Black'
# print("Let's talk about %r." % my_name)
# print("He's %r inches tall." % (my_height * 2))
# print("He's %d pounds heavy." % my_weight)
# print("Actually that's not too heavy.")
# print("He's got %s eyes and %s hair." %(my_eyes,my_hair))
# print("His teeth are usually %s depending on the coffee." % my_teeth)
# print("If I add %d,%d,and %d I get %d." % (my_age,my_height,my_weight,my_age + my_height + my_weight))

#习题6
# x = "There are %d types of people." % 10 # 10种人
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." %(binary,do_not)
# print(x)
# print(y)
# print("I said: %r." % x)
# print("I also said: '%s'." % y)
# hilarious = False
# joke_evaluation = "Isn't that joke so funny? %r"
# print(joke_evaluation % hilarious)
# w = "This is the left side of..."
# e = "a string with a right side."
# print(w + e)

#习题7
# print("Mary had a little lamb.")
# print("Its fleece was white as %s." % 'show' )
# print("And everyone that Mary went.")
# print("." * 10) # what'd that do?
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
# print(end1 + end2 + end3 + end4 + end5 + end6)
# print(end7 + end8 + end9 + end10 + end11 + end12)

#习题8
# formatter = "%r %r %r %r"
# print(formatter %(1,2,3,4))
# print(formatter %('one','two','three','four'))
# print(formatter %(True,False,False,True))
# print(formatter %(formatter,formatter,formatter,formatter))
# print(formatter %('I had this thing',
#                   'That you could type up right.',
#                   "But it didn't sing.",
#                   "So I said goodnight."))

# 习题9
# Here's some new strange stuff,remember type it exactly.
# days = "Mon Tue Wen Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"
# print("Here are the days:",days)
# print("Here are the months:",months)
# print("""
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want,or 5,or 6.
# """)

# 习题10
# print("I am 6'2\" tall.")
# print('I am 6\'2" tall.')
# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."
# fat_cat = '''
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# '''
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

#习题11
# print("How old are you? ",end='')
age = input("How old are you? ")
# print("How tall are you? ",end='')
height = input("How tall are you? ")
# print("How much do you weight? ",end='')
weight = input("How much do you weight? ")
print("So,you're %r old,%r tall and %r heavy." %(age,height,weight))

#习题13 参数、解包、变量
