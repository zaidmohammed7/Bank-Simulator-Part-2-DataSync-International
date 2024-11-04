from tkinter import messagebox

errors_dictionary = {
    1: 'Password length should not be less than 8 characters',
    2: 'Password length should not be more than 50 characters',
    3: 'Password must contain at least one lowercase letter',
    4: 'Password must contain at least one uppercase letter',
    5: 'Password must contain at least one number',
    6: 'Password must contain at least one special character'
}


def password_check(password):
    errors = []
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    value = True

    if len(password) < 8:
        errors.append(1)
        value = False
    if len(password) > 50:
        errors.append(2)
        value = False
    if not any(char.islower() for char in password):
        errors.append(3)
        value = False
    if not any(char.isupper() for char in password):
        errors.append(4)
        value = False
    if not any(char.isdigit() for char in password):
        errors.append(5)
        value = False
    if not any(char in special_characters for char in password):
        errors.append(6)
        value = False

    if value is True:
        return True

    else:
        string = ''
        errors_list = []

        for i in errors:
            errors_list.append(string + errors_dictionary[i])

        __value__ = '\n'.join(errors_list)
        messagebox.showerror(title='Password Error', message=__value__)


def loading():
    import tkinter as tk

    root = tk.Tk()
    root.title('Loading')
    root.config(bg='#323232')

    root.overrideredirect(True)

    # ______________fixing window on screen__________credit: stack_overflow

    w = 400  # width for the Tk root
    h = 100  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    label = tk.Label(root, text='\n\n     Processing Request     \n\n',
                     bg='#323232',
                     fg='white',
                     font=('Helveica', '25'))
    label.pack()

    root.after(7000, lambda: root.destroy())

    root.mainloop()

    return True


def create_salt():
    import random
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()'

    import mysql.connector as sql

    from tkinter import messagebox
    connection = sql.connect(host='localhost',
                             user='root',
                             password='dpsbn',
                             database='client_db')

    if connection.is_connected():

        used_salt_list = []

        while True:
            n1 = random.choice(characters)
            n2 = random.choice(characters)
            n3 = random.choice(characters)
            n4 = random.choice(characters)
            n5 = random.choice(characters)
            n6 = random.choice(characters)
            n7 = random.choice(characters)
            n8 = random.choice(characters)
            n9 = random.choice(characters)
            n10 = random.choice(characters)
            n11 = random.choice(characters)
            n12 = random.choice(characters)
            n13 = random.choice(characters)
            n14 = random.choice(characters)
            n15 = random.choice(characters)
            n16 = random.choice(characters)
            n17 = random.choice(characters)
            n18 = random.choice(characters)
            n19 = random.choice(characters)
            n20 = random.choice(characters)
            n21 = random.choice(characters)
            n22 = random.choice(characters)
            n23 = random.choice(characters)
            n24 = random.choice(characters)
            n25 = random.choice(characters)
            n26 = random.choice(characters)
            n27 = random.choice(characters)
            n28 = random.choice(characters)
            n29 = random.choice(characters)
            n30 = random.choice(characters)
            n31 = random.choice(characters)
            n32 = random.choice(characters)
            n33 = random.choice(characters)
            n34 = random.choice(characters)
            n35 = random.choice(characters)
            n36 = random.choice(characters)
            n37 = random.choice(characters)
            n38 = random.choice(characters)
            n39 = random.choice(characters)
            n40 = random.choice(characters)
            n41 = random.choice(characters)
            n42 = random.choice(characters)
            n43 = random.choice(characters)
            n44 = random.choice(characters)
            n45 = random.choice(characters)
            n46 = random.choice(characters)
            n47 = random.choice(characters)
            n48 = random.choice(characters)
            n49 = random.choice(characters)
            n50 = random.choice(characters)
            n51 = random.choice(characters)
            n52 = random.choice(characters)
            n53 = random.choice(characters)
            n54 = random.choice(characters)
            n55 = random.choice(characters)
            n56 = random.choice(characters)
            n57 = random.choice(characters)
            n58 = random.choice(characters)
            n59 = random.choice(characters)
            n60 = random.choice(characters)
            n61 = random.choice(characters)
            n62 = random.choice(characters)
            n63 = random.choice(characters)
            n64 = random.choice(characters)
            n65 = random.choice(characters)
            n66 = random.choice(characters)
            n67 = random.choice(characters)
            n68 = random.choice(characters)
            n69 = random.choice(characters)
            n70 = random.choice(characters)
            n71 = random.choice(characters)
            n72 = random.choice(characters)
            n73 = random.choice(characters)
            n74 = random.choice(characters)
            n75 = random.choice(characters)
            n76 = random.choice(characters)
            n77 = random.choice(characters)
            n78 = random.choice(characters)
            n79 = random.choice(characters)
            n80 = random.choice(characters)
            n81 = random.choice(characters)
            n82 = random.choice(characters)
            n83 = random.choice(characters)
            n84 = random.choice(characters)
            n85 = random.choice(characters)
            n86 = random.choice(characters)
            n87 = random.choice(characters)
            n88 = random.choice(characters)
            n89 = random.choice(characters)
            n90 = random.choice(characters)
            n91 = random.choice(characters)
            n92 = random.choice(characters)
            n93 = random.choice(characters)
            n94 = random.choice(characters)
            n95 = random.choice(characters)
            n96 = random.choice(characters)
            n97 = random.choice(characters)
            n98 = random.choice(characters)
            n99 = random.choice(characters)
            n100 = random.choice(characters)
            n101 = random.choice(characters)
            n102 = random.choice(characters)
            n103 = random.choice(characters)
            n104 = random.choice(characters)
            n105 = random.choice(characters)
            n106 = random.choice(characters)
            n107 = random.choice(characters)
            n108 = random.choice(characters)
            n109 = random.choice(characters)
            n110 = random.choice(characters)
            n111 = random.choice(characters)
            n112 = random.choice(characters)
            n113 = random.choice(characters)
            n114 = random.choice(characters)
            n115 = random.choice(characters)
            n116 = random.choice(characters)
            n117 = random.choice(characters)
            n118 = random.choice(characters)
            n119 = random.choice(characters)
            n120 = random.choice(characters)
            n121 = random.choice(characters)
            n122 = random.choice(characters)
            n123 = random.choice(characters)
            n124 = random.choice(characters)
            n125 = random.choice(characters)
            n126 = random.choice(characters)
            n127 = random.choice(characters)
            n128 = random.choice(characters)

            salt = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13 + n14 + n15 + n16 + n17 + n18 + n19 + n20 + n21 + n22 + n23 + n24 + n25 + n26 + n27 + n28 + n29 + n30 + n31 + n32 + n33 + n34 + n35 + n36 + n37 + n38 + n39 + n40 + n41 + n42 + n43 + n44 + n45 + n46 + n47 + n48 + n49 + n50 + n51 + n52 + n53 + n54 + n55 + n56 + n57 + n58 + n59 + n60 + n61 + n62 + n63 + n64 + n65 + n66 + n67 + n68 + n69 + n70 + n71 + n72 + n73 + n74 + n75 + n76 + n77 + n78 + n79 + n80 + n81 + n82 + n83 + n84 + n85 + n86 + n87 + n88 + n89 + n90 + n91 + n92 + n93 + n94 + n95 + n96 + n97 + n98 + n99 + n100 + n101 + n102 + n103 + n104 + n105 + n106 + n107 + n108 + n109 + n110 + n111 + n112 + n113 + n114 + n115 + n116 + n117 + n118 + n119 + n120 + n121 + n122 + n123 + n124 + n125 + n126 + n127 + n128

            mycur = connection.cursor()
            mycur.execute("SELECT PASSWORD_SALT FROM client WHERE PASSWORD_SALT = '{}'".format(salt))
            result = mycur.fetchall()
            mycur.close()

            result = list(result)

            if salt not in used_salt_list:
                if len(result) != 0:
                    used_salt_list.append(salt)
                    continue

                elif len(result) == 0:
                    break

        return salt

    else:
        messagebox.showerror(title='Server Error', message='Server has crashed!')


def hash_password(salt, password):
    import hashlib as hl

    pwd = password + salt

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
