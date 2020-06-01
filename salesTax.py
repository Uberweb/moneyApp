tax_rates = open("taxRates")
dic = {}
for line in tax_rates:
    line = line.strip().split(',')
    state = line[0]
    rate = line[1]
    dic[state] = rate


def error_message():
    print("Something went wrong!")


def calculate_sales_tax(chosenState, price):
    #this function looks up the sales tax file and calculates the sales tax
    #based on the price
    if chosenState in dic:
        print()
    x = (chosenState/100)*price
    salePrice = price + x
    return salePrice


#currently only USA, eventually, we will extend globally, eg:
#Australia 10% GST

