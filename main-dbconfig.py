import mysql.connector

conn=mysql.connector.connect(host='localhost' , password='root', user='root', database='new_schema',)
contents = []
cursor=conn.cursor()
_SQL= """show tables"""

cursor.execute(_SQL)

contents.append(cursor.fetchall())
print(str(contents))

_mbs="""describe tasks"""
cursor.execute(_mbs)
res=cursor.fetchall()
#print(res)
for row in res:
        print(row,sep=' ')
_res="""insert into emp(id,ename) values(3,'Rupu')"""

cursor.execute(_res)
conn.commit()

_jhk="""select * from emp"""
cursor.execute(_jhk)

for row in cursor.fetchall():
        print(row,sep=' ')
        
cursor.close()
conn.close()


#        print('hi')
