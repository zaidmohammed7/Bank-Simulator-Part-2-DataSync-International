import mysql.connector as sql

connection = sql.connect(host='localhost',
                         user='root',
                         password='dpsbn')

if connection.is_connected() is True:
    cur = connection.cursor()
    cur.execute("""CREATE DATABASE IF NOT EXISTS client_db""")

connection = sql.connect(host='localhost',
                         user='root',
                         password='dpsbn',
                         database='client_db')

if connection.is_connected() is True:
    print('[ INFO ] MySQL   [ MYSQL       ] : database loaded successfully')
    cur = connection.cursor()
    cur.execute('use client_db')
    cur.execute("""CREATE TABLE IF NOT EXISTS client (
    NAME VARCHAR(30) NOT NULL,
    EMAIL VARCHAR(40) NOT NULL UNIQUE,
    USERNAME VARCHAR(30) PRIMARY KEY,
    PASSWORD VARCHAR(128) NOT NULL,
    ACCOUNT_IN_USE_PERMISSION VARCHAR(5) NOT NULL, 
    PASSWORD_SALT VARCHAR(128) NOT NULL UNIQUE,
    PHONE VARCHAR(17) NOT NULL UNIQUE,
    ADDRESS VARCHAR(100) NOT NULL,
    CARD_NUMBER VARCHAR(16) NOT NULL UNIQUE,
    PIN_NUMBER VARCHAR(128) NOT NULL,
    CARD_NUMBER_IN_USE_PERMISSION VARCHAR(5) NOT NULL ,
    BALANCE VARCHAR(15) NOT NULL,
    TRANSFERS VARCHAR(15) NOT NULL,
    WITHDRAWALS VARCHAR(15) NOT NULL,
    DEPOSITS VARCHAR(15) NOT NULL)
    """)
    connection.close()

else:
    print("Server failed! Try again later")


def create_account(name, email, username, password, salt, phone, address, card, pin, currency_code):
    from main_directory.operation_functions_pyfiles import signup_successful
    acc_permission = True
    card_permission = True
    balance = 0
    varchar_balance = currency_code + str(balance)
    import mysql.connector as mysql
    conn = mysql.connect(host='localhost',
                         user='root',
                         password='dpsbn',
                         database='client_db')

    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO client VALUES ('{name}','{email}','{username}','{password}','{acc_permission}','{salt}','{phone}','{address}','{card}','{pin}','{card_permission}','{varchar_balance}','{varchar_balance}','{varchar_balance}','{varchar_balance}')""")
    conn.commit()
    cursor.close()
    conn.close()
    signup_successful()


def delete_account(username):
    from main_directory.operation_functions_pyfiles import delete_successful
    import mysql.connector as mysql
    conn = mysql.connect(host='localhost',
                         user='root',
                         password='dpsbn',
                         database='client_db')

    cursor = conn.cursor()
    cursor.execute(f"""DELETE FROM client WHERE USERNAME='{username}'""")
    conn.commit()
    cursor.close()
    conn.close()
    delete_successful()

