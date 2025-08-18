import requests
#extract data from source - Rest API/Cloud/DWH/FS/DB
products=requests.get('https://dummyjson.com/products').json()['products']

#tranform data - for csv file(pid,pname,price,category,brand) - only beuty products
#tranform data - for  mysql table
#tranform data -for  json file /mongodb collection
new_products=[]
new_products_json=[]
for product in products:
    if product['category'] =='beauty':
        new_products.append((product['id'],
                             product['title'],
                             product['price'],
                             product['category'],
                             product['brand']))
        new_products_json.append({'pid':product['id'],
                                  'pname':product['title'],
                                  'price':product['price'],
                                  'category':product['category'],
                                  'brand':product['brand']
                                  })
print(len(new_products))
print(len(new_products_json))






