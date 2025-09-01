# List in Python
 # Lists
 #  what are lists
# lists vs arrays
# How to creat a list
# characterstics of list
# how to creat a list
# Access items in a list
# Editing items in a list
# Deleting items in a list
# Operation on lists
# functions on list
   
         #  List  
'''  list is a data type where we can store multiple items in a single variable.
it is a collection of data items. for Example'''

list = [12,34,77,89,90,26,33]
print(list)
  
  # in list we can add different data type in a single variable.

l = [23,567, "Naveed", "Ali", True , False]
print(l) 
 
# List VS array
   #  Array are fixed in size while list are dynamic
   # in Array we can add one type of data in single variable
   # speed of Execution is Slower in list
   # List Occupy More space as compare array 

 # characterstics of list
   # Changeable/Mutable 
   # Hetrogeneous
l = [23,567, "Naveed", "Ali", True , False]
print(l)

   # Can have Duplicate
L = [1,2,6,3,2,1,2]
print(L)

  # Can Be nested
Li = [12,44,56,76,[32,45,64],3476,52]
print(Li)

# Access items in a list
 # Indexing
m= [1,2,534,32,87,23,53]
print(m[4]) # positive indexing
print(m[-4]) #Negative index
print(m[len(m)-4])
  
  # Adding Items in List
   #append ==> it is used to add one item in list
k = [2,3,5,6] 
k.append(8)
print(k)
  
   #Extend ==> it is used to add more thenone item in list
N = [2,3,5,6] 
N.extend([4,9,4])
print(N)
  
  # Insert
M = [3,6,8,5,9,23,54]
M.insert(3,234)
print(M)

   # Editing items in a list
   
A = [34,5,3,7,23,75,64,34]
A[5] = 236
print(A)
A[-6] = 536
print(A) 
A[3:6] = [435,13,44]
print(A)

  # Deleting items in a list
  # del
S = [3,4,2,6,8]
del S[-1]
print(S)
 # Remove
D = [3,4,2,6,8]
D.remove(6)
print(D)
 # Clear
F = [3,4,2,6,8]
F.clear
print(F)
 
   # Operation on lists
     # Arithmetic ==> " + " and " * "
L1 = [2 ,3,1,5,6,7]
L2 = [9,8,4]
print(L1 + L2)
print(L1 * 3)
     # Membership
L1 = [2 ,3,1,5,6,7]
print(5 in L1)  
 
          # Operation on lists
l2 = [2 ,3,1,5,6,7]
for i in l2:
    print(i)    
     
     # functions on list
       #len/min/max/sorted
    L1 = [2 ,3,1,5,6,7]
    print(len(L1))
    print(min(L1))
    print(max(L1))
    print(sorted(L1))
    # Count
    M = [3,6,8,5,2,23,54,2,3,45,3,65,3,47,63]
    print(M.count(3))
    print(M.count(2))
    # index
    M = [3,6,8,5,2,23,54,2,3,45,3,65,3,47,63]
    print(M.index(5))
     # Reverse
M = [3,6,8,5,2,23,54,2,3,45,3,65,3,47,63]
M.reverse()
print(M)
   # sort (vs sorted)
M = [3,6,8,5,2,23,54,2,3,45,3,65,3,47,63]
print(M)
print(sorted(M))
print(M)
M.sort()  #sort ==> permanently sort but sorted do temprarly 
print(M)