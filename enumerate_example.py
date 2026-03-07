def myFun(inputstr):
    list=[]
    for index, char in enumerate(inputstr,start=1):
        if(index%2==0):
            list.append(char.upper())
        else:
            list.append(char.lower())
    return list

inputstr = "Hello, World!"
result = myFun(inputstr)
print(result)