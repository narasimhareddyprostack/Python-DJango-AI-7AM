prod_prices=[98,198,298,398]

#increse every product price +plus one
#output
#           [99,199,299,399]

new_prod_prices=[]

for price in prod_prices:
    new_prod_prices.append(price+1)

print(prod_prices)
print(new_prod_prices)