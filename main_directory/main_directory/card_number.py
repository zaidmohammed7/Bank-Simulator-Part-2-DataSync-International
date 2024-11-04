def create_card_number():
    import random
    import mysql.connector as sql

    connection = sql.connect(host='localhost',
                             user='root',
                             password='dpsbn',
                             database='client_db')

    if connection.is_connected():

        used_card_number_list = []

        while True:

            number_set = '1234567890'

            n1 = random.choice(number_set)
            n2 = random.choice(number_set)
            n3 = random.choice(number_set)
            n4 = random.choice(number_set)
            n5 = random.choice(number_set)
            n6 = random.choice(number_set)
            n7 = random.choice(number_set)
            n8 = random.choice(number_set)
            n9 = random.choice(number_set)
            n10 = random.choice(number_set)
            n11 = random.choice(number_set)
            n12 = random.choice(number_set)
            n13 = random.choice(number_set)
            n14 = random.choice(number_set)
            n15 = random.choice(number_set)
            n16 = random.choice(number_set)

            card_number = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13 + n14 + n15 + n16

            mycur = connection.cursor()
            mycur.execute("SELECT CARD_NUMBER FROM client WHERE CARD_NUMBER = '{}'".format(card_number))
            result = mycur.fetchall()
            mycur.close()

            result = list(result)

            if card_number not in used_card_number_list:
                if len(result) != 0:
                    used_card_number_list.append(card_number)
                    continue

                elif len(result) == 0:
                    break

        return card_number


def create_pin():
    import random
    number_set = '1234567890'

    n1 = random.choice(number_set)
    n2 = random.choice(number_set)
    n3 = random.choice(number_set)
    n4 = random.choice(number_set)

    pin = n1 + n2 + n3 + n4

    return pin


def hash_pin(pin):
    import hashlib as hl
    pwd = pin

    for i in range(1000000):
        pwd = hl.sha512(pwd.encode('UTF-8')).hexdigest()

    hash2 = pwd

    for i in range(1000000):
        hash2 = hl.sha512(hash2.encode('UTF-8')).hexdigest()

    hash3 = hash2

    for i in range(1000000):
        hash3 = hl.sha512(hash3.encode('UTF-8')).hexdigest()

    hash4 = hash3

    for i in range(1000000):
        hash4 = hl.sha512(hash4.encode('UTF-8')).hexdigest()

    hash5 = hash4

    for i in range(1000000):
        hash5 = hl.sha512(hash5.encode('UTF-8')).hexdigest()

    final_hash = hash5
    return final_hash

