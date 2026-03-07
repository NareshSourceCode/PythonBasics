def myfunc(a,b,c,d,e): # fixed number of positional arguments
    print(f"Given arguments are: {a} {b} {c} {d} {e}") # printing the given arguments
    print('Hello, World!') # printing Hello, World!

def myfunc1(*args): 
    print(args)
    print('first line of the function') # printing the first line of the function
    print(args) # args is a tuple of positional arguments
  

def myfunc2(**kwargs): 
    print('2nd line of the function')
  
    print(kwargs) # kwargs is a dictionary of keyword arguments

def myfunc3(*args,**kwargs): 
    print('3rd line of the function')
    print(args) # args is a tuple of positional arguments
    print(kwargs) # kwargs is a dictionary of keyword arguments

    
myfunc1(1,2,3,4,5) # calling the function with positional arguments
myfunc2(name='Naresh',age=30) # calling the function with keyword arguments
myfunc3(1,2,3,4,5,name='Naresh',age=30) # calling the function with positional and keyword arguments