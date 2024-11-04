import mysql.connector as sql

connection = sql.connect(host='localhost',
                         user='root',
                         password='dpsbn',
                         database='admin_db')

if connection.is_connected() is True:
    print('[ INFO ] MySQL   [ MYSQL       ] : database loaded successfully')
    cur = connection.cursor()
    cur.execute('use admin_db')
    cur.execute("""CREATE TABLE IF NOT EXISTS administrators (
        NAME VARCHAR(30) NOT NULL,
        USERNAME VARCHAR(30) PRIMARY KEY,
        PASSWORD VARCHAR(128) NOT NULL,
        PASSWORD_SALT VARCHAR(128) NOT NULL UNIQUE,
        SECURITY_KEY VARCHAR(128) NOT NULL)
        """)
    connection.close()

else:
    print("Server failed! Try again later")


def insert():

    cur2 = connection.cursor()

    cur2.execute("""INSERT INTO administrators VALUES
        ()""")
    cur2.close()
    connection.commit()
    connection.close()

