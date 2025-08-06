prod_prices=[98,198,298,398]

#increse every product price +plus one
#output
#           [99,199,299,399]

def addplus(price):
    return price+1

map_obj=map(addplus,prod_prices)
#           executing privided function, for every element of list/seq
new_prod_prices=list(map_obj)
print(prod_prices)
print(new_prod_prices)