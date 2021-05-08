import mysql.connector

dbconfig={  'host':'127.0.0.1',
            'user': 'vsearch',
            'password':'vsearchpasswd',
            'database':'vsearchlogDB',}

conn=mysql.connector.connect(**dbconfig)

cursor=conn.cursor(buffered=True)

__SQL='''INSERT INTO log (phrase,letters,ip,browser_string,results)
         VALUES (%s,%s,%s,%s,%s)
'''
cursor.execute(__SQL,('hitch-hicker','xyz','127.0.0.1','Google','set()'))

__SQL=''' select * from log
'''
cursor.execute(__SQL)

for row in cursor.fetchall():
    print(row)


conn.commit()
cursor.close()
conn.close()