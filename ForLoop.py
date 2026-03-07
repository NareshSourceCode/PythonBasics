mLst =[1, 3,4,5,6,7,8,9]
for i in mLst:
    if(i%2==0):# printing only even numbers
        print(f"{i} is even number") # printing even numbers with a message
    elif(i%2!=0): # printing only odd numbers   
        print(f'{i} is odd number') # printing odd numbers with a message

sum =1
for i in range(1,9): # printing numbers from 1 to 10
   # print(i) # printing numbers from 1 to 10
    sum =sum+i
print(f"The sum of first 10 natural numbers is {sum}") # printing the sum of first 10 natural numbers

mTupleList = [(1,2),(3,4),(5,6)]
for i in mTupleList:
    print(i) # printing the tuple list
for (a,b) in mTupleList:
    print(f"{a}  ") # printing the tuple list
    print(f"{b}") # printing the tuple list

mydict = {'name':'John','age':30,'city':'New York'}
for key in mydict: # printing the dictionary values
    print(key) # printing the dictionary values
for key in mydict: # printing the dictionary values
    print(mydict[key]) # printing the dictionary values
for key, value in mydict.items(): # printing the dictionary values
    print(f"{key} : {value}") # printing the dictionary values


sentense ="Hello, World! Welcome to Python programming. " \
"This language is great for data science and machine learning."
for word in sentense.split(): # printing the words in the sentence
    if(word[0]=='p' or word[0]=='P'): # printing the words that start with 'p' or 'P'
        print(word) # printing the words that start with 'p' or 'P'

for i in range(1,111):
    if(i%3==0): # printing the numbers that are divisible by 3
        print(i) # printing the numbers that are divisible by 3