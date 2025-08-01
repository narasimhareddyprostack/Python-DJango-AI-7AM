'''
read data.txt and write into new file  ie abc.txt
'''
fp1=open('data.txt','r')
data=fp1.read()

fp2=open("abc.txt",'a')
fp2.write(data)
print("New File Created")
fp1.close()
fp2.close()