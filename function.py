  # Function  
''' it is a block of code that perform a specific task
 whenever it is called.
 for example.
  def is_even (i) : " "" 
   # def ==> is a key which show that it is a function
   # is_even ==> it is the name if that funtion.
   # (i) ==> ("it is parameter or argument) it is the place where you provide the input 
    to the function.
   after [ : ]we add optional docstring " "" ==> optionasl docstring which tell
   us about fuction, thing like what the input required, what wiill the function return.
   # funtion body ==> Where we write the logic of the funtion.
   for example.
      X=i%2==0.
    #Return statment of funtion
    return X
    # Funtion Call ==>
    # is_even(6) 
    #  Lets create a function ( with docstring)       ''' 

def is_even(num):
    """This function prints if given number is Odd or Even.
    input  - any valid integer
    output - prints odd/even directly
    """
   
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")
   


# test the function with numbers 1 to 10
for i in range(1, 11):
    is_even(i)

       