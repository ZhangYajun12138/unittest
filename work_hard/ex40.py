# coding:utf-8
# 40.字典

cities = {"CA":"Francisco","MI":"Detroit","FL":"Jacksonville"}
cities["NY"] = "New York"
cities["OR"] = "Portland"

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities["_find"] = find_city

while True:
    print("State?(ENTER to quit)")
    state = input("> ")
    if not state:
        break
    else:
        pass
    city_found = cities["_find"](cities,state)
    print(city_found)