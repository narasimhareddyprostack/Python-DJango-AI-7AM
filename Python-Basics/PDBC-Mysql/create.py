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
            create table employees(eid int Not Null,ename varchar(32) Not Null ,esal float);
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print('Table Created Success fully')
except mysql.connector.Error as err:
    print(err.msg)

finally:
    print("finally block - will execute always")
    dbcon.close()