import time
# list

names = ["Aly","Layla","Badr","Mohamed","Omar","Mohsen","Abdullah","Abdulaziz","Adam","Yazan","Malek"]

# # count number of items in the list-
print(len(names))   
print(names)
# printing names 1 by 1-----
for i in range(10):
    print(names[i])
    time.sleep(1)
# adding item to list
names.append("Alex")
# insert an item into the list
# name is the object and 3 is index
names.insert(3,"Fares")
for i in range(13):
    print(names[i])
    time.sleep(1)

#  print last item of list
i=12
print(names[i])
i=-1
print(names[i])
