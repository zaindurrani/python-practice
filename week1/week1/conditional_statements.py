#if else elif in details
#In keeping with the light switch example, the state of the switch 
#can be stored with a Boolean value of True or False.
electricity = bool(input())
if electricity:
    electricity = False
    print("no electricity")
if electricity:
    electricity = True
    print("turning on the lights")