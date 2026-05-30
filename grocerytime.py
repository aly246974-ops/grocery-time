# it will be a story
# you and your family are planning to go shopping and you are assinged to do a grocery list.
from icecream import ic

groceries=[]
# your mom asked to add honey, milk, and butter
groceries.append("honey")
groceries.append("milk")
groceries.append("butter")
ic(groceries)

# your sister asked you to add a candy, a banana, and some chips
groceries.append("candy")
groceries.append("banana")
groceries.append("chips")
ic(groceries)

# you want doritoes,chocolate,and pepsi
groceries.append("doritoes")
groceries.append("chocolate")
groceries.append("pepsi")
ic(groceries)

# your mom reviewed the grocery list and asked to remove chips. 
groceries.remove("chips")
ic(groceries)

# your mom asked you to remove the fourth item
groceries.pop(3)
ic(groceries)

# your mom asked how many items are in the grocery list.

ic(len(groceries))

# your mom asked to add cheese after the butter
groceries.insert(3,"cheese")
ic(groceries)