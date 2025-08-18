import requests,csv
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

#load into csv,mysql table,json file and mongodb collection
fp1=None
fp2=None
dbcon=None 
curson=None 
try:
    fp1=open('products.csv','w',newline='')
    csv_writer=csv.writer(fp1)
    #CSV file Header
    csv_writer.writerow(['pid','pname','price','category','brand'])
    csv_writer.writerows(new_products)
    print("New CSV File Created!")

except csv.Error as err:
        print(f"Error processing CSV: {err}") 



finally:
    fp1.close()





