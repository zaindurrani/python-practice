#EVENT LIKE IF ELSE CONTROL SWITCH LIKE LIGHT BULB ETC
#CONTROL FLOW ORDER IN WHICH INSTRUCTIONS ARE EXECUTED

#(CONDITIONALS)IF, ELSE , ELIF ESLE IF, LOOPS(FOR LOOP , WHILE LOOP)
#CODE EXAMPLES
#what to do is to give discount of 10 doll if total bill is 100 AND aboce

bill_total = int(input("total bill amount?: "))
discount = 10
discount1 = 20
if bill_total > 100:
    bill_total = bill_total - discount
if  bill_total > 200:
    bill_total = bill_total - discount1

if bill_total < 100:
    print("your bill is less than 100 and to qualify for discount bill should at least be 100")
elif bill_total > 200:
    print("bill is grater than 200")

print("your total bill will be: "+ str(bill_total))
