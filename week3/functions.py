
def totaltax():
    bill =int( input())
    tax_rate = 15
    total_tax = (bill * 100) / tax_rate
    print(total_tax)


totalamount1 = totaltax()
print(totalamount1)

#or we can also add arguments , so when we run the function, we just have to add data to the eg: totaltax(bill, taxrate)

