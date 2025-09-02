# Tuples In Python
 # Tuple
'''Tuple in python is similar to list but tuple is an immutable List.
A tuple can not be changed in any way once it is created. the tuple have " () " while list have " [] " .'''
 # Creating Tuple
   # empty
t1 = () 
print(t1)
# creating a tuple with single item
t2 = (3,) # to print single item we Add Comma " , " in tuple
print(t2)
  
t3 = (12,34,55,23,"NAveed", "Ali", "Umar", True, False)
print(t3)
 # Accessing Items
   
t4 =  (12,34,55,23,"NAveed", "Ali", "Umar", True, False , 54,66,77)
print(t4[3])
print(t4[-2])
print(t4[1:8:2])
 # Editing items / Adding items
'''Items can not edite or added in tuple if once the tuple is created'''
 
 # Operation in Tuple
   # Arithmetic ==> " + " and " * "
L1 = [2 ,3,1,5,6,7]
L2 = [9,8,4]
print(L1 + L2)
print(L1 * 3)