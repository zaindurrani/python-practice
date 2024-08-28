"""
exception errors are the type of errors that are shown in the execution
 that may cause application to crash example sitiuation like 5/0 that 
 has syntactical correctness but not logical correctenss

 so we use try and except function try the statement that can cause failure of program
 except by printing out what to print in this case,  , 

 as in 
 
try:
    ans = divide_by(40, 0)
    e shows short form

except Exception as e:
__class__ will show what kind of error it is probably
    print("something went wrong", e)
    print(e.__class__)

"""
#code are as under

def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except Exception as e:
    print("something went wrong", e)
    print(e.__class__)
