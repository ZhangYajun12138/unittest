# coding:utf-8
# 39.列表的操作
import  os
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list,let's fix that.")
stuff = ten_things.split(" ")
print(stuff)
more_stuff = ["Day","Night","Song","Frisbee","Cron","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print("There's %d items now." %len(stuff))

print("There we go:",stuff)
print("Let's go some things with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
# print(os.join(" ",stuff))
print("#".join(stuff[3:5]))