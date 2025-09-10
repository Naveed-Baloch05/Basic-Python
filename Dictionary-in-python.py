# Dictionary
'''dictionary in python is a collection of keys and its values. it store
 data values like map. it is not like other data type which hold only 
a single value as an element. for Example'''
dict ={'name':'Naveed', 'age':'23', 'gender':'Male'}
print(dict)
  
  # Creading Dictionary
   #empty
d = {}
print(d)
    # 1D dictionary
d1 = {'name':'Naveed', 'gender':'Male'} 
print(d1)
     # with Mixed Keys
d2 = {(1,2,6,7):3, 'Name':'Naveed', 'hallo':'world' }   
print(d2)
    # 2D Dictionary
d2 = {
    "Name":"Naveed", 
    "College":"Any one",
    "Sem":"4th",
    "Subjects":{
        "dsa":50,
        "math":60,
        "eng":70,
        "phy":80
    }  
      }
print(d2)

        # Accesing Items
        # two way 
        # []
        # get
d1 = {'name':'Naveed', 'gender':'Male'}
print(d1['name'])           
print(d1.get('name'))
  # Adding key-value pair
d1 = {'name':'Naveed', 'gender':'Male'}
d1['age'] = 55
print(d1)
d1['Weight'] = 50
print(d1)
  # Remove key-value pair
  # pop
d7 = {'Name':'Naveed', 'hallo':'world', 'weight':47, 'age': 23 }  
d7.pop('weight')  
print(d7)
  # popItems
d7.popitem()
print(d7)
   # del
del d7 ['Name']
print(d7)
 # Editing Key- value pair
d2 = {
    "Name":"Naveed", 
    "College":"Any one",
    "Sem":"4th",
    "Subjects":{
        "dsa":50,
        "math":60,
        "eng":70,
        "phy":80
    }  
      }
d2["Sem"] = "5th"
print
print(d2)
d2["Subjects"]["math"] = 40
print(d2)