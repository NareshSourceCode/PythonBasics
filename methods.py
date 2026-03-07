print("******Start of the program******")
mList =[3,5,6,5,4,6,8,7,54,6,77,88,99,100]
def even_odd(num): # Syntax for defining a function
    if(num%2==0):
        return f"{num} is even number"
    else:
        return f"{num} is odd number"

for i in mList:
    print(even_odd(i))
mList.insert(0,2) # inserting a number at the beginning of the list
print(mList) # printing the list after inserting a number at the beginning of the list

mList.append(101) # appending a number at the end of the list
print(mList) # printing the list after appending a number at the end of the list


def printString(string):
    print(f"Given string is: {string}") # printing the given string
printString("Hello Naresh Goud  !") # calling the function to print a string


def add(a,b):
    print(f"Adding {a} and {b} result is: {a+b}") # printing the numbers to be added
    return a+b # returning the sum of two numbers
add(5,10) # calling the function to add two numbers



def sub(a,b):
    return a-b;
print(sub(2,3))


#Below is the code for finding the employee who has worked the most hours in a week

emp_hours=[('Naresh',100),('Goud',200),('Nanditha',300)]

def emp_check(emp_hours):
    emp_name=''
    max_hours=0
    for name,hours in emp_hours:
        if max_hours < hours:
            emp_name=name
            max_hours=hours
            print(name+" has worked for "+str(hours)+" hours")
             
    return (emp_name,max_hours)
print(emp_check(emp_hours))


print("******End of the program******")
