#faida ye hai we can pass any amount of non keyword variable and kwargs

def sum_of(a,b):
    return a + b
print(sum_of(2,5))
#what if print(sum_of(2,5,4))
#this is where args are usefull and used we  use *args as it will allow n argument to comme through

def suma(*args):
    sum = 0
    for x in args:
        sum += x
    
    return sum
print(suma(2,5,3))

#args and kwargs. logic build after python course practice required
    
