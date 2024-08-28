#logical operators
"""
    a

"""
a = 2
b= 4

if(a<b and b>a):
    print("hi")
if(a<b or  b>a):
    print("hi")

bill_total = 210

discount1 = 10
discount2 = 20
if bill_total  > 100 or  bill_total < 200:
    print("bill is greater  than 100!")




def is_loyalty_customer(customer):
    return customer == 'loyal'

def calculate_discount(total, discount_percentage):
    return total * (1 - discount_percentage / 100)

def apply_discount(total_bill, loyalty_customer):
    if is_loyalty_customer(loyalty_customer) and total_bill > 100:
        discount = 20
    elif total_bill > 100:
        discount = 10
    else:
        print('Sorry, no discount ...')
        discount = 0
    return calculate_discount(total_bill, discount)

def calculate_total(total_bill, loyalty_customer):
    discounted_total = apply_discount(total_bill, loyalty_customer) 
    service_charge = 0.05 if discounted_total <= 100 else 0
    return discounted_total + service_charge

loyalty_customer = 'loyal'
total_bill = 124

final_total = calculate_total(total_bill, loyalty_customer)
print('Total Bill:', final_total)