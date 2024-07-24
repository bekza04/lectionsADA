d1 = {"a": 100, "b": 200, "c":300}

d2 = {"a": 300, "b": 200, "d": 400}

print(d1["b"] == d2["b"]) 
#True



person = {"name": "Kelly", "age":25, "city": "New york"}
print(person["age"]) 
#25





sample_set = {"Yellow", "Orange", "Black"}

sample_list = ["Blue", "Green", "Red"]




set1 = {6, 4, 2, 5, 7, 8, 10, 9}
set1.discard(7)
print(set1)
#{2, 4, 5, 6, 8, 9, 10}


set2 = {'Python', 'it', 'c++', 'java', 'programming'}
set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
print(set2.intersection(set3))
#{'java', 'programming', 'c++'}

set2 = {'Python', 'it', 'c++', 'java', 'programming'}
set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
print(set3 - set2)
#{'dart', 'css', 'html'}


set4 = {12, 13, 15, 36, 73}
set4.add(90)
print(set4)
popped = set4.pop
set4.pop()
print(set4)
#{36, 73, 90, 12, 13, 15}
#{73, 90, 12, 13, 15}




# menu_dict = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu_dict["besh_barmak] = "130"
# print(menu_dict)




dict = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}




print(dir(set))
print(dir(dict))
set6 = {'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'}
set7 = {'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'}
print(set6.intersection(set7))
#{'pop', 'copy', 'clear', 'update'}


list_ = ["hat", "book", "laptop", "top", "pen"]
list_.remove("pen")
print(list_)
#['hat', 'book', 'laptop', 'top']




