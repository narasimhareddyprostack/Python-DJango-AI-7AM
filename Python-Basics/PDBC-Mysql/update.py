import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='dbone')
    cursor=dbcon.cursor()
    sql_st='''
            insert into employees
            values
            (103,'Priya',65000.45);
         '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data/Employee Record Inserted")
except mysql.connector.Error as err:
    print(err.msg)
finally:
    pass