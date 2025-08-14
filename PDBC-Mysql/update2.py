employees_data = (
    (1, "Alice", 50000),
    (2, "Bob", 52000),
    (3, "Charlie", 54000),
    (4, "David", 56000),
    (5, "Eve", 58000),
    (6, "Frank", 60000),
    (7, "Grace", 62000),
    (8, "Heidi", 64000),
    (9, "Ivan", 66000),
    (10, "Judy", 68000),
    (11, "Karl", 70000),
    (12, "Laura", 72000),
    (13, "Mallory", 74000),
    (14, "Niaj", 76000),
    (15, "Olivia", 78000),
    (16, "Peggy", 80000),
    (17, "Quentin", 82000),
    (18, "Rupert", 84000),
    (19, "Sybil", 86000),
    (20, "Trent", 88000),
    (21, "Uma", 90000),
    (22, "Victor", 92000),
    (23, "Walter", 94000),
    (24, "Xavier", 96000),
    (25, "Yvonne", 98000),
    (26, "Zack", 100000),
    (27, "Ava", 102000),
    (28, "Ben", 104000),
    (29, "Cathy", 106000),
    (30, "Derek", 108000),
    (31, "Ella", 110000),
    (32, "Finn", 112000),
    (33, "Gina", 114000),
    (34, "Hank", 116000),
    (35, "Ivy", 118000),
    (36, "Jake", 120000),
    (37, "Kara", 122000),
    (38, "Liam", 124000),
    (39, "Mona", 126000),
    (40, "Nate", 128000),
    (41, "Opal", 130000),
    (42, "Paul", 132000),
    (43, "Queen", 134000),
    (44, "Rita", 136000),
    (45, "Sam", 138000),
    (46, "Tina", 140000),
    (47, "Umar", 142000),
    (48, "Vera", 144000),
    (49, "Will", 146000),
    (50, "Zoe", 148000),
)

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
             insert into employees(eid,ename,esal)
             values(%s,%s,%s)
            '''
    cursor.executemany(sql_st,employees_data)
    dbcon.commit()
    print("Inserted 50 records")

except mysql.connector.Error as err:
    print(err.msg)
finally:
    dbcon.close()