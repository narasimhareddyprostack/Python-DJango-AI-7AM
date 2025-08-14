import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='dbone')
    cursor=dbcon.cursor()
    sql_st='select * from employees;'
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    print(employees)
    for employee in employees:
        print(employee)

except mysql.connector.Error as err:
    print(err.msg)
finally:
    dbcon.close()