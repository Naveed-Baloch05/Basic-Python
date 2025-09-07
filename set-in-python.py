# Sets
'''A Set is an unordered collection of items. Every set element is
unique means (No duplicates) and can not be changed ( must be immutable). however
a set itself.We can add or remove items from it.''' 
# Creating Sets
 #empty
s = set ()
print(s)
s1 = {1,2,4,5,6,67}
print(s1)
 # Accessing Items ==> can not because due to unorderd
  
  # Adding Items
S = {1,2,3,5,6,7}
S.add (9)
print(S) 
  # update ==> add multiple items in set with the help of list
S3 = {1,2,3,5}
S3.update([7,8,9])
print(S3)
    
     # Deleting Items
     # del ==> it can delet the hole set not any item in set
     # discard
S4 = {1,2,3,5,6,7}
S4.discard(6)
print(S4)
 #pop  ==> it will delete any Random item from set
S5 = {1,2,3,5,6,7}
S5.pop()
print(S5)
 # clear ==> it make the hole set empty
S6 = {1,2,3,5,6,7}
S6.clear()
print(S6)
 
  
     # Set Operation
     # Union (|) ==> no duplicate every item in each set is run olny one time
N2 = {1,2,3,5,6,7}
N3 = {2,8,9,3,4}
print (N2| N3)
     # Intersection(&) ==> common items of two sets
N2 = {1,2,3,5,6,7}
N3 = {2,8,9,3,4}
print (N2 & N3)
     # Difference (-) ==> the item of first set print which is not in set 2
N2 = {1,2,3,5,6,7}
N3 = {2,8,9,3,4}
print (N2 - N3)
     # symmetric difference (^) ==> without common items of both set are print
N2 = {1,2,3,5,6,7}
N3 = {2,8,9,3,4}
print (N2 ^ N3)
     # Membership Test ==> will test weather that item is presant or not in given set
N2 = {1,2,3,5,6,7}
print (2 not in N2)
print(1 in N2)
   