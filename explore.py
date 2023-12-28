print("\n---- part 1, assigning items to a list ----")

# assign a list using specific items
my_friends = ['bill', 'ted', 42, 3.14]  
# note: can be mixed types, but more typical to be one type

# assign an empty list, add items to it
my_chores = []
my_chores.append("dishes")  #NOTE the syntax, list_name.function_name()
my_chores.append("mow the lawn")


# how to print? Many ways...most simply
print(my_chores)
print("my friends list contains: " + str(my_friends))





print("\n\n---- part 2, changing items ----")
my_chores[1]="laundry"
print(my_chores)




print("\n\n---- part 3, len() and 'in' ----")
print(len(my_chores))

# the keyword 'in' can be used for various things
if 'dishes' in my_chores:
 print('yes, I found that in the list')
else:
 print('that element is not in the list')







