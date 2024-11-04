import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox
import time
import datetime
import mysql.connector as sql
import threading
import sys
import re

from main_directory.open_windows import open_windows_list
from main_directory.country_codes_file import country_codes
from main_directory.DocumentationWindow import documentation
from main_directory.refresh_windows_functions_file import signup_refresh_registry
from main_directory.password_functions_file import password_check
from main_directory.password_functions_file import create_salt
from main_directory.password_functions_file import hash_password
from main_directory.password_functions_file import loading
from main_directory.card_number import create_card_number
from main_directory.card_number import create_pin
from main_directory.card_number import hash_pin
from main_directory.client_database import create_account

PopOutCalender_SIGNUP = []  # used to check the launch of the pop out calendar while returning to the signup window from the main calendar window
PopOutChatBox_SIGNUP = []  # used to check the launch of the pop out chat box while returning to the signup window from the main chat box window
REMOTE_SERVER = "one.one.one.one"


def signup():
    """
        -> objective: starting the signup window

        -> we create the signup window using the modules tkinter and tkinter.ttk

        -> creating a signup window with labels and buttons
            -> labels include visual displays and details when the client reacts with the app
            -> buttons can be used by the client to visit various other windows:
                                1. return to home button
                                2. login window button
                                3. delete account window button
                                4. documentation window buttons
                                5. refresh home window buttons
                                6. launch calendar button
                                7. launch chat box button
                                8. launch chat box BETA button
                                9. exit button
                                10. back button
        -> the signup window also has the input boxes for the client to register with his details:
                                1. name
                                2. email
                                3. address
                                4. phone
                                5. username
                                6. password

        once the user clicks a particular button, for example, the login button,
        he/she will be redirected to the login window.
        for this, the signup window is first destroyed using the <tkinter_window>.destroy() method and
        the login window is called from the login file located in main_directory.login

        this way of opening windows is followed by all the buttons be it login, delete account,
        open chat box, calendar etc.

        at the last of the left sided menu, we can see the exit button that can be used by the client
        to exit the app

        at the top right, there is a submit button to register the user
            """

    print('[ INFO ] Tkinter [ Tkinter     ] : signup window loaded successfully')

    signup_window = tk.Tk()
    signup_window.title("Sign Up For A New Account")
    signup_window.focus_force()
    signup_window.config(bg='#70d4c3')
    signup_window.resizable(False, False)
    try:
        signup_window.iconbitmap(r'..\main_directory\ico1.ico')

        from PIL import ImageTk, Image

        image2 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\signup.png"))

        img_lb2 = tk.Label(signup_window, image=image2, borderwidth=0)
        img_lb2.pack()
        img_lb2.place(x=0, y=0)
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    def run_pop_out_calender_signup():

        """
                    we check the PopOutCalendar_SIGNUP list first.
                    if the length of the list is equal to 1, only then will the calendar function further execute
                    the function call.

                    initially, the length of PopOutCalendar_SIGNUP list is 0 but when the PopOutCalendar is called from
                    the main_directory.PopOutCalendar__reg__utils__ file, the list gets appended and the new length
                    becomes 1

                    hence, when the length of the list is 1, we again append another value to it to stop it from
                    executing the same code again and again everytime the home window is called.

                    when the function is called, the PopOutCalendar__reg__utils__ file containing PopOutCalendar
                    object gets called and executed
                """

        if len(PopOutCalender_SIGNUP) == 1:

            PopOutCalender_SIGNUP.append(1)

            from main_directory.PopOutCalendar__reg__utils__ import PopOutCalendar
            app = PopOutCalendar()
            app.run()

    """
        now we check for running the pop out calendar if it is called by the client. After a certain time, 
        we run the run_pop_out_calendar_signup() function side by side to the actual signup() function.

        this way, the client can have a legitimate access to both the signup window and the calendar window
        at the same time
    """

    signup_window.after(10, lambda: run_pop_out_calender_signup())

    def run_pop_out_chat_box_signup():

        """
                    we check the PopOutChatBox_SIGNUP list first.
                    if the length of the list is equal to 1, only then will the chat box function further execute
                    the function call.

                    initially, the length of PopOutChatBox_SIGNUP list is 0 but when the PopOutChatBox is called from
                    the main_directory.PopOutChatBox__reg__utils__ file, the list gets appended and the new length
                    becomes 1

                    hence, when the length of the list is 1, we again append another value to it to stop it from
                    executing the same code again and again everytime the home window is called.

                    when the function is called, the PopOutChatBox__reg__utils__ file containing PopOutChatBox
                    object gets called and executed
                """

        if len(PopOutChatBox_SIGNUP) == 1:

            PopOutChatBox_SIGNUP.append(1)

            from main_directory.PopOutChatBox__reg__utils__ import PopOutChatBox
            app = PopOutChatBox()
            app.run()

    """
        now we check for running the pop out chat box if it is called by the client. After a certain time, 
        we run the run_pop_out_chat_box_signup() function side by side to the actual signup() function.

        this way, the client can have a legitimate access to both the signup window and the chat box window
        at the same time
    """

    signup_window.after(10, lambda: run_pop_out_chat_box_signup())

    # _____________________________________________________________________________
    #
    # # the heading for the window
    #
    # heading = tk.Label(signup_window, text='Signup',
    #                    bg='#70d4c3',
    #                    font=('Georgia', '40'))
    # heading.pack()
    # heading.place(x=350, y=75)

    # ______________fixing window on screen__________credit: stack_overflow

    w = 800  # width for the Tk root
    h = 700  # height for the Tk root

    # get screen width and height
    ws = signup_window.winfo_screenwidth()  # width of the screen
    hs = signup_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    signup_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    # _________________fixing window on screen_END___________________________

    # _________________________design - start________________________________

    label1 = tk.Label(signup_window, text='',
                      bg='#2d3a4d',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    label2 = tk.Label(signup_window, text='',
                      bg='#2d3a4d',
                      width=150,
                      height=2,
                      font=('Georgia', '20'))
    label2.pack()
    label2.place(x=0, y=0)

    # _________________________design - end___________________________________

    # _________________time module display -start___________credit: stack_overflow

    clock = tk.Label(signup_window,
                     bg='#2d3a4d',
                     fg='white',
                     font=('Georgia', '10'))
    clock.pack()
    clock.place(x=720, y=0)

    def tick():  # credit: StackOverflow
        updated_time = time.strftime('%H:%M:%S')
        clock.config(text=updated_time + '   ')
        clock.after(200, tick)

    threading.Thread(target=tick, daemon=True).start()

    # ________________________time display - end_____________________________

    # ________________________date display - start__________credit: stack_overflow

    date = datetime.datetime.now()
    date_label = tk.Label(signup_window,
                          text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                          bg='#2d3a4d',
                          fg='white',
                          font=('Georgia', '10'))
    date_label.pack()
    date_label.place(x=590, y=0)

    # ________________________date display - end_____________________________
    # mode
    mode = tk.Label(signup_window, text='', bg='#2d3a4d', font=('Helvetica', '10'))
    mode.pack()
    mode.place(x=510, y=0)

    def mode_function():
        from connection import is_connected as connection

        check_connection = connection(REMOTE_SERVER)

        if check_connection is True:
            mode.config(fg='#34eb43', text='ONLINE')
            mode.after(5000, mode_function)
        else:
            mode.config(fg='#ff0000', text='OFFLINE')
            mode.after(5000, mode_function)

    threading.Thread(target=mode_function, daemon=True).start()

    # _____________________initial_window_setup_completed____________________

    def submit():

        """
                when the user clicks the submit button, the submit() function is called.
                the function requires the following:
                            1. name
                            2. email
                            3. address
                            4. phone number
                            5. username
                            6. password

                once the email is taken, the database is checked if or not the email is present already.
                if it is present, an error is showed, otherwise the user continues.

                once the phone number is taken, the database is checked if or not the phone number is present already.
                if it is present, an error is showed, otherwise the user continues.

                once the username is taken, the app connects to the mysql database where it is checked
                if the username entered by the user actually exists or not. if exists, it displays an error; otherwise the
                user continues

                then the password entered is hashed and then stored in the database. at the time of signup, the card number
                and the pin of the user is displayed.

                once all the formalities are done, the signup window is destroyed and home window is launched
        """

        name = sw_input_name_field_entry_box.get()

        if len(name) == 0:
            messagebox.showerror(title='Error', message='Enter a name!')

        else:
            if name.isascii():
                concatenated_name = name.replace(" ", '')

                contains_other_char = False
                for i in concatenated_name:
                    if not i.isalpha():
                        contains_other_char = True

                if contains_other_char is True:
                    messagebox.showerror(title='Name Error', message='Enter alphabets only')

                else:
                    name = name.title().lstrip().rstrip()
                    final_name = name

                    email = sw_input_email_field_entry_box.get()
                    email = email.lstrip().rstrip()

                    pattern = r"[a-zA-z0-9!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9.-_]+\.(com|edu|net)"

                    if email.isascii():

                        if '@' in email:

                            contains_space = False
                            for i in email:
                                if i.isspace():
                                    contains_space = True

                            if contains_space is True:
                                messagebox.showerror(title='Fatal Email Error', message='Enter valid email id only. \nNo whitespace allowed')

                            else:

                                email_slice = email.split('@')

                                if len(email_slice) != 2:
                                    messagebox.showerror(title='Fatal Email Error', message="Enter valid email id only. More than one '@' (or none) is not allowed")

                                else:

                                    if re.search(pattern, email):

                                        if email[-4] == '.' and (email[-3:] in ('com', 'edu', 'net')):

                                            connection = sql.connect(host='localhost',
                                                                     user='root',
                                                                     password='dpsbn',
                                                                     database='client_db')

                                            if connection.is_connected():
                                                cursor = connection.cursor()
                                                cursor.execute("""SELECT EMAIL FROM client where EMAIL='{}'""".format(email))
                                                result = cursor.fetchall()
                                                cursor.close()
                                                connection.close()
                                                result = list(result)

                                                try:
                                                    if result[0][0] == email:
                                                        messagebox.showerror(title='Email Error', message='Email id already taken\n\nEnter a valid email id')

                                                except IndexError:

                                                    not_allowed_list = r'(),:;<>[\]\"'

                                                    email_continue = True
                                                    for i in not_allowed_list:
                                                        if i in email:
                                                            email_continue = False

                                                    if email_continue is False:
                                                        messagebox.showerror(title='Email Error', message='No special characters allowed except !#$%&\'*+-/=?^_`{|}~ ')
                                                        pass

                                                    else:
                                                        final_email = email

                                                        address1 = sw_input_address1_field_entry_box.get()
                                                        address1 = address1.replace(', ', ' ')
                                                        address1 = address1.replace(',', ' ')
                                                        address1 = address1.lstrip().rstrip()

                                                        address2 = sw_input_address2_field_entry_box.get()
                                                        address2 = address2.replace(', ', ' ')
                                                        address2 = address2.replace(',', ' ')
                                                        address2 = address2.lstrip().rstrip()

                                                        address3 = sw_input_address3_field_entry_box.get()
                                                        address3 = address3.replace(', ', ' ')
                                                        address3 = address3.replace(',', ' ')
                                                        address3 = address3.lstrip().rstrip()

                                                        address = address1.title() + ' ' + address2.title() + ' ' + address3.title()
                                                        address = address.lstrip().rstrip()

                                                        if len(address) == 0:
                                                            messagebox.showerror(title='Address Error', message='Address length can\'t be zero')

                                                        else:
                                                            final_address = address.title()

                                                            phone = sw_input_phone_field_entry_box.get()
                                                            phone = phone.lstrip().rstrip()

                                                            connection = sql.connect(host='localhost',
                                                                                     user='root',
                                                                                     password='dpsbn',
                                                                                     database='client_db')

                                                            if connection.is_connected():
                                                                code = clicked.get()
                                                                __phone__ = code + phone

                                                                cursor = connection.cursor()
                                                                cursor.execute("""SELECT PHONE FROM client where PHONE='{}'""".format(__phone__))
                                                                result = cursor.fetchall()
                                                                cursor.close()
                                                                connection.close()
                                                                result = list(result)

                                                                try:
                                                                    if result[0][0] == __phone__:
                                                                        messagebox.showerror(title='Phone Error', message='Phone number already taken\n\nEnter a valid phone number')

                                                                except IndexError:

                                                                    contains_other_char_phone = False
                                                                    for i in phone:
                                                                        if not i.isdigit():
                                                                            contains_other_char_phone = True

                                                                    if contains_other_char_phone is True:
                                                                        messagebox.showerror(title='Phone Number Error', message='Enter numbers only')

                                                                    else:
                                                                        if len(phone) == 10:

                                                                            code = clicked.get()
                                                                            actual_phone_number = code+phone

                                                                            final_phone_number = actual_phone_number

                                                                            username = sw_input_username_field_entry_box.get()
                                                                            username = username.lstrip().rstrip()
                                                                            username.replace(' ', '')

                                                                            if len(username) >=5 and username.isdigit():
                                                                                messagebox.showerror(title='Username Error', message='Enter a valid username\nUsername cannot be a number')

                                                                            elif len(username) >= 5:

                                                                                if username.isascii():

                                                                                    connection = sql.connect(host='localhost',
                                                                                                             user='root',
                                                                                                             password='dpsbn',
                                                                                                             database='client_db')

                                                                                    if connection.is_connected():
                                                                                        cursor = connection.cursor()
                                                                                        cursor.execute("""SELECT USERNAME FROM client where USERNAME='{}'""".format(username))
                                                                                        result = cursor.fetchall()
                                                                                        cursor.close()
                                                                                        connection.close()
                                                                                        result = list(result)

                                                                                        try:
                                                                                            if result[0][0] == username:
                                                                                                messagebox.showerror(title='Error', message='Username already taken')

                                                                                        except IndexError:
                                                                                            final_username = username

                                                                                            pwd = sw_input_password1_field_entry_box.get()
                                                                                            pwd = pwd.lstrip().rstrip()

                                                                                            if pwd.isascii():

                                                                                                __password__ = password_check(pwd)

                                                                                                confirm_pwd = sw_input_password2_field_entry_box.get()
                                                                                                confirm_pwd = confirm_pwd.lstrip().rstrip()

                                                                                                if __password__ is True:

                                                                                                    if pwd == confirm_pwd:

                                                                                                        check__check_box_value = cb_var.get()

                                                                                                        if check__check_box_value == 1:

                                                                                                            send_email_verification = messagebox.askyesnocancel(title="Email Verification", message="Do you want email verification during signup?\n\nClick YES for email verification\nClick NO for regular on-device signup")

                                                                                                            if send_email_verification is True:
                                                                                                                from connection import is_connected

                                                                                                                check_connection = is_connected(REMOTE_SERVER)

                                                                                                                if check_connection is True:
                                                                                                                    import yagmail
                                                                                                                    import random

                                                                                                                    characters = '1234567890'
                                                                                                                    chr2 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

                                                                                                                    n1 = random.choice(characters)
                                                                                                                    n2 = random.choice(characters)
                                                                                                                    n3 = random.choice(characters)
                                                                                                                    n4 = random.choice(characters)
                                                                                                                    n5 = random.choice(characters)
                                                                                                                    n6 = random.choice(characters)
                                                                                                                    n7 = random.choice(characters)
                                                                                                                    n8 = random.choice(chr2)
                                                                                                                    n9 = random.choice(chr2)

                                                                                                                    __otp__ = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9

                                                                                                                    server_connection = sql.connect(host='localhost',
                                                                                                                                             user='root',
                                                                                                                                             password='dpsbn',
                                                                                                                                             database='dsi_gmail')

                                                                                                                    server_cursor = server_connection.cursor()
                                                                                                                    server_cursor.execute("""SELECT emailid, pwd FROM company_gmail where emailid='{}'""".format('datasyncinternational@gmail.com'))
                                                                                                                    result = server_cursor.fetchall()
                                                                                                                    server_cursor.close()

                                                                                                                    server_email = result[0][0]
                                                                                                                    server_pwd = result[0][1]

                                                                                                                    yag = yagmail.SMTP(server_email, server_pwd)
                                                                                                                    yag.send(f"{final_email}", 'Verification', f"Hello {final_name}\n\nHere is your one time password: {__otp__}\n\nDO NOT SHARE THIS\n\n\nRegards\nTeam DSI")

                                                                                                                    email_ver_win = tk.Tk()
                                                                                                                    email_ver_win.title("Email Verification")
                                                                                                                    email_ver_win.focus_force()
                                                                                                                    email_ver_win.config(bg='#f2ea94')
                                                                                                                    email_ver_win.resizable(False, False)
                                                                                                                    email_ver_win.overrideredirect(False)
                                                                                                                    email_ver_win.lift()

                                                                                                                    heading = tk.Label(email_ver_win, text='One Time Password',
                                                                                                                                       bg='#f2ea94',
                                                                                                                                       font=('aerial', '21'))
                                                                                                                    heading.pack()
                                                                                                                    heading.place(x=110, y=20)

                                                                                                                    # ______________fixing window on screen__________credit: stack_overflow

                                                                                                                    w = 470  # width for the Tk root
                                                                                                                    h = 300  # height for the Tk root

                                                                                                                    # get screen width and height
                                                                                                                    ws = email_ver_win.winfo_screenwidth()  # width of the screen
                                                                                                                    hs = email_ver_win.winfo_screenheight()  # height of the screen

                                                                                                                    # calculate x and y coordinates for the Tk root window
                                                                                                                    x = (ws / 2) - (w / 2)
                                                                                                                    y = (hs / 2) - (h / 2)

                                                                                                                    # set the dimensions of the screen
                                                                                                                    # and where it is placed
                                                                                                                    email_ver_win.geometry('%dx%d+%d+%d' % (w, h, x, y))
                                                                                                                    # login_window.geometry("800x600")
                                                                                                                    display = tk.Label(email_ver_win, text=f'Enter the otp below',
                                                                                                                                       bg='#f2ea94',
                                                                                                                                       font=('Georgia', '15'))
                                                                                                                    display.pack()
                                                                                                                    display.place(x=140, y=100)

                                                                                                                    entry_box = tk.Entry(email_ver_win,
                                                                                                                                         width=10,
                                                                                                                                         bg='#ffffff',
                                                                                                                                         font=('aerial', '25'))
                                                                                                                    entry_box.pack()
                                                                                                                    entry_box.place(x=145, y=150)

                                                                                                                    entry_box.focus_force()

                                                                                                                    def verify(*args):
                                                                                                                        user_input = entry_box.get()
                                                                                                                        user_input = user_input.lstrip().rstrip()

                                                                                                                        if user_input == __otp__:
                                                                                                                            email_ver_win.destroy()

                                                                                                                            final_password_ = pwd

                                                                                                                            salt_ = create_salt()

                                                                                                                            __object___ = threading.Thread(target=loading, daemon=True)
                                                                                                                            __object___.start()

                                                                                                                            password_final_ = hash_password(salt_, final_password_)

                                                                                                                            final_card_number_ = create_card_number()
                                                                                                                            final_pin_ = create_pin()

                                                                                                                            messagebox.showinfo(title='Details', message=f'{final_name}, your card number is {final_card_number_}\nYour PIN in {final_pin_}\n\nDO NOT SHARE THESE')

                                                                                                                            __object__2_ = threading.Thread(target=loading, daemon=True)
                                                                                                                            __object__2_.start()

                                                                                                                            pin_ = hash_pin(final_pin_)
                                                                                                                            # name, email, username, password, salt, phone, address, card, pin, balance

                                                                                                                            currency_code_ = get_currency.get()

                                                                                                                            signup_window.destroy()
                                                                                                                            create_account(final_name, final_email, final_username, password_final_, salt_, final_phone_number, final_address, final_card_number_, pin_, currency_code_)
                                                                                                                        else:
                                                                                                                            email_ver_win.destroy()
                                                                                                                            messagebox.showerror(title="Error", message='Incorrect otp!')

                                                                                                                    check = tk.Button(email_ver_win,
                                                                                                                                      text='     Verify     ',
                                                                                                                                      bg='#deb82f',
                                                                                                                                      activeforeground='black',
                                                                                                                                      activebackground='#bf9d22',
                                                                                                                                      fg='black',
                                                                                                                                      relief=tk.FLAT,
                                                                                                                                      command=verify,
                                                                                                                                      font=('Georgia', '10'))
                                                                                                                    check.pack()
                                                                                                                    check.place(x=200, y=250)
                                                                                                                    check.bind('<Enter>', func=lambda e: check.config(bg='#a89552'))
                                                                                                                    check.bind('<Leave>', func=lambda e: check.config(bg='#deb82f'))

                                                                                                                    email_ver_win.bind('<Return>', verify)

                                                                                                                    email_ver_win.mainloop()

                                                                                                                else:
                                                                                                                    messagebox.showerror(title="Connection error", message="You are not connected to the internet")

                                                                                                            elif send_email_verification is False:

                                                                                                                final_password = pwd

                                                                                                                salt = create_salt()

                                                                                                                __object__ = threading.Thread(target=loading, daemon=True)
                                                                                                                __object__.start()

                                                                                                                password_final = hash_password(salt, final_password)

                                                                                                                final_card_number = create_card_number()
                                                                                                                final_pin = create_pin()

                                                                                                                messagebox.showinfo(title='Details', message=f'{final_name}, your card number is {final_card_number}\nYour PIN in {final_pin}\n\nDO NOT SHARE THESE')

                                                                                                                __object__2 = threading.Thread(target=loading, daemon=True)
                                                                                                                __object__2.start()

                                                                                                                pin = hash_pin(final_pin)
                                                                                                                # name, email, username, password, salt, phone, address, card, pin, balance

                                                                                                                currency_code = get_currency.get()

                                                                                                                signup_window.destroy()
                                                                                                                create_account(final_name, final_email, final_username, password_final, salt, final_phone_number, final_address, final_card_number, pin, currency_code)
                                                                                                        else:
                                                                                                            messagebox.showerror(title=' Agreement Error', message='You have not agreed to the terms and conditions!')

                                                                                                    else:
                                                                                                        messagebox.showerror(title=' Password Error', message='Passwords don\'t match!')

                                                                                            else:
                                                                                                messagebox.showerror(title='Password Error', message='Enter ASCII characters only')

                                                                                    else:
                                                                                        messagebox.showerror(title='Server Error', message='The server crashed!')
                                                                                else:
                                                                                    messagebox.showerror(title='Username Error', message='Enter ASCII characters only')
                                                                            else:
                                                                                messagebox.showerror(title='Username Error', message='Username cannot be less than 5 characters')

                                                                        else:
                                                                            messagebox.showerror(title='Phone Error', message='Enter a valid number!')
                                                            else:
                                                                messagebox.showerror(title='Server Error', message='The server crashed!')
                                            else:
                                                messagebox.showerror(title='Server Error', message='The server crashed!')
                                        else:
                                            messagebox.showerror(title='Fatal Email Error', message='Enter valid email id only')
                                    else:
                                        messagebox.showerror(title='Fatal Email Error', message='Enter valid email id only')
                        else:
                            messagebox.showerror(title='Domain Error', message='Enter valid email id only')
                    else:
                        messagebox.showerror(title='Email Error', message='Enter ASCII characters only')
            else:
                messagebox.showerror(title='Name Error', message='Enter ASCII characters only')

    # __________________________body of the window___________________________

    def go_back():

        """
                when the back button is pressed, the function checks the last element of the open windows list
                located in main_directory.open_windows.py. getting the last element, it pops it out og the list
                and then the signup window destroys and the last element that is stored in the variable is
                then read and the window is recalled and run .

                eg. if home is the last element of the list, then home is removed and then stored in a variable.
                 the login window is destroyed and home is then called by calling the home function located at
                main_directory.home.py file.
        """

        length = len(open_windows_list)
        element = open_windows_list[length-1]

        if element == 'home':
            open_windows_list.pop()
            from main_directory.HomeWindow import home
            signup_window.destroy()
            home()

        elif element == 'login':
            open_windows_list.pop()
            from main_directory.LoginWindow import login
            signup_window.destroy()
            login()

        elif element == 'delete':
            open_windows_list.pop()
            from main_directory.DeleteWindow import delete
            signup_window.destroy()
            delete()

        elif element == 'docs':
            open_windows_list.pop()
            from main_directory.DocumentationWindow import documentation
            signup_window.destroy()
            documentation()

    go_back_button = tk.Button(signup_window,
                               text="  Back  ",
                               bg='#2d3a4d',
                               relief=tk.FLAT,
                               activeforeground='white',
                               activebackground='#546f7a',
                               fg='white',
                               command=go_back,
                               font=('Georgia', '10'))
    go_back_button.pack()
    go_back_button.place(x=5, y=20)
    go_back_button.bind('<Enter>', func=lambda e: go_back_button.config(bg='#64758f'))
    go_back_button.bind('<Leave>', func=lambda e: go_back_button.config(bg='#2d3a4d'))

    # ________________________________________________________________________________________________

    # __________________________________________ name field  _________________________________________

    # sw_display_name_field_label = tk.Label(signup_window,
    #                                        bg='#70d4c3',
    #                                        text="Enter your name  :",
    #                                        font=('aerial', '12'))
    # sw_display_name_field_label.pack()
    # sw_display_name_field_label.place(x=150, y=190)

    sw_input_name_field_entry_box = ttk.Entry(signup_window,
                                              width=25,
                                              font=('aerial', '12'))
    sw_input_name_field_entry_box.pack()
    sw_input_name_field_entry_box.place(x=460, y=217)

    sw_input_name_field_entry_box.focus_force()

    name_info = tk.Label(signup_window, bg='#ff61f4',
                         font=('aerial', '12'),
                         borderwidth=0)
    name_info.pack()
    name_info.place(x=458, y=219)

    name_info_lbl = tk.Label(signup_window, text='  i  ',
                             bg='#5E17EB',
                             font=('aerial', '12'),
                             fg='white',
                             borderwidth=0)
    name_info_lbl.pack()
    name_info_lbl.place(x=720, y=217)
    name_info_lbl.bind('<Enter>', func=lambda e: name_info.config(bg='#dedede', text='You cannot change your name\nin the future', fg='red'))
    name_info_lbl.bind('<Leave>', func=lambda e: name_info.config(bg='#ff61f4', text=''))

    # __________________________________________ email field  _________________________________________

    # sw_display_email_field_label = tk.Label(signup_window,
    #                                         bg='#70d4c3',
    #                                         text="Enter your email  :",
    #                                         font=('aerial', '12'))
    # sw_display_email_field_label.pack()
    # sw_display_email_field_label.place(x=150, y=240)

    sw_input_email_field_entry_box = ttk.Entry(signup_window,
                                               width=25,
                                               font=('aerial', '12'))
    sw_input_email_field_entry_box.pack()
    sw_input_email_field_entry_box.place(x=460, y=267)

    email_info = tk.Label(signup_window, bg='#9e61ff',
                          font=('aerial', '12'),
                          borderwidth=0)
    email_info.pack()
    email_info.place(x=458, y=269)

    email_info_lbl = tk.Label(signup_window, text='  i  ',
                              bg='#5E17EB',
                              font=('aerial', '12'),
                              fg='white',
                              borderwidth=0)
    email_info_lbl.pack()
    email_info_lbl.place(x=720, y=267)
    email_info_lbl.bind('<Enter>', func=lambda e: email_info.config(bg='#dedede', text='You cannot change your email\nin the future', fg='red'))
    email_info_lbl.bind('<Leave>', func=lambda e: email_info.config(bg='#9e61ff', text=''))

    # __________________________________________ address1 field  _________________________________________

    # sw_display_address1_field_label = tk.Label(signup_window,
    #                                            bg='#70d4c3',
    #                                            text="Enter your address  :",
    #                                            font=('aerial', '12'))
    # sw_display_address1_field_label.pack()
    # sw_display_address1_field_label.place(x=150, y=290)

    sw_input_address1_field_entry_box = ttk.Entry(signup_window,
                                                  width=25,
                                                  font=('aerial', '12'))
    sw_input_address1_field_entry_box.pack()
    sw_input_address1_field_entry_box.place(x=460, y=317)

    # __________________________________________ address2 field  _________________________________________

    sw_input_address2_field_entry_box = ttk.Entry(signup_window,
                                                  width=25,
                                                  font=('aerial', '12'))
    sw_input_address2_field_entry_box.pack()
    sw_input_address2_field_entry_box.place(x=460, y=347)

    # __________________________________________ address2 field  _________________________________________

    sw_input_address3_field_entry_box = ttk.Entry(signup_window,
                                                  width=25,
                                                  font=('aerial', '12'))
    sw_input_address3_field_entry_box.pack()
    sw_input_address3_field_entry_box.place(x=460, y=377)

    # __________________________________________ phone field  _________________________________________

    # sw_display_phone_field_label = tk.Label(signup_window,
    #                                         bg='#70d4c3',
    #                                         text="Enter your phone  :",
    #                                         font=('aerial', '12'))
    # sw_display_phone_field_label.pack()
    # sw_display_phone_field_label.place(x=150, y=400)

    sw_input_phone_field_entry_box = ttk.Entry(signup_window,
                                               width=16,
                                               font=('aerial', '12'))
    sw_input_phone_field_entry_box.pack()
    sw_input_phone_field_entry_box.place(x=460, y=445)

    # _________________________________________country code drop down ___________________________________

    clicked = tk.StringVar()
    clicked.set("91::")
    drop = ttk.Combobox(signup_window, textvariable=clicked, state='readonly', width=5)
    drop['values'] = country_codes
    drop.pack()
    drop.place(x=625, y=447)

    # _________________________________________currency code drop down ___________________________________

    get_currency = tk.StringVar()
    get_currency.set('INR')

    currency_dropdown = ttk.Combobox(signup_window, textvariable=get_currency, state='readonly', width=5)

    currency_codes = ['AUD', 'INR', 'USD', 'EUR', 'NZD', 'AED', 'LKR', 'SAR']
    currency_dropdown['values'] = currency_codes
    currency_dropdown.pack()
    currency_dropdown.place(x=695, y=447)

    # __________________________________________ username field  _________________________________________
    #
    # sw_display_username_field_label = tk.Label(signup_window,
    #                                            bg='#70d4c3',
    #                                            text="Enter your username  :",
    #                                            font=('aerial', '12'))
    # sw_display_username_field_label.pack()
    # sw_display_username_field_label.place(x=150, y=450)

    sw_input_username_field_entry_box = ttk.Entry(signup_window,
                                                  width=25,
                                                  font=('aerial', '12'))
    sw_input_username_field_entry_box.pack()
    sw_input_username_field_entry_box.place(x=460, y=495)

    username_info = tk.Label(signup_window, bg='#c29cff',
                             font=('aerial', '12'),
                             borderwidth=0)
    username_info.pack()
    username_info.place(x=458, y=497)

    username_info_lbl = tk.Label(signup_window, text='  i  ',
                                 bg='#5E17EB',
                                 font=('aerial', '12'),
                                 fg='white',
                                 borderwidth=0)
    username_info_lbl.pack()
    username_info_lbl.place(x=720, y=495)
    username_info_lbl.bind('<Enter>', func=lambda e: username_info.config(bg='#dedede', text='You cannot change your username\nin the future', fg='red'))
    username_info_lbl.bind('<Leave>', func=lambda e: username_info.config(bg='#c29cff', text=''))

    # __________________________________________ password 1 field  _________________________________________

    # sw_display_password1_field_label = tk.Label(signup_window,
    #                                             bg='#70d4c3',
    #                                             text="Enter your password  :",
    #                                             font=('aerial', '12'))
    # sw_display_password1_field_label.pack()
    # sw_display_password1_field_label.place(x=150, y=500)

    sw_input_password1_field_entry_box = ttk.Entry(signup_window,
                                                   show='*',
                                                   width=25,
                                                   font=('aerial', '12'))
    sw_input_password1_field_entry_box.pack()
    sw_input_password1_field_entry_box.place(x=460, y=545)

    def hide_pwd1():
        pin___label1.config(command=show_pwd1, text=' ○ ')
        sw_input_password1_field_entry_box.configure(show='*')
        pass

    def show_pwd1():
        pin___label1.config(command=hide_pwd1, text=' — ')
        sw_input_password1_field_entry_box.configure(show='')
        pass

    pin___label1 = tk.Button(signup_window,
                             text=' ○ ',
                             command=show_pwd1,
                             relief=tk.FLAT,
                             bg='#5E17EB',
                             fg='white',
                             activeforeground='white',
                             activebackground='#364f44',
                             borderwidth=0)
    pin___label1.pack()
    pin___label1.place(x=720, y=545)

    # __________________________________________ password 2 field  _________________________________________

    # sw_display_password2_field_label = tk.Label(signup_window,
    #                                             bg='#70d4c3',
    #                                             text="Confirm your password  :",
    #                                             font=('aerial', '12'))
    # sw_display_password2_field_label.pack()
    # sw_display_password2_field_label.place(x=150, y=550)

    sw_input_password2_field_entry_box = ttk.Entry(signup_window,
                                                   show='*',
                                                   width=25,
                                                   font=('aerial', '12'))
    sw_input_password2_field_entry_box.pack()
    sw_input_password2_field_entry_box.place(x=460, y=595)

    def hide_pwd2():
        pin___label2.config(command=show_pwd2, text=' ○ ')
        sw_input_password2_field_entry_box.configure(show='*')
        pass

    def show_pwd2():
        pin___label2.config(command=hide_pwd2, text=' — ')
        sw_input_password2_field_entry_box.configure(show='')
        pass

    pin___label2 = tk.Button(signup_window,
                             text=' ○ ',
                             command=show_pwd2,
                             relief=tk.FLAT,
                             bg='#5E17EB',
                             fg='white',
                             activeforeground='white',
                             activebackground='#364f44',
                             borderwidth=0)
    pin___label2.pack()
    pin___label2.place(x=720, y=595)

    # __________________________ check box __________________________________________

    cb_var = tk.IntVar()
    check_box = tk.Checkbutton(signup_window, text='I agree to the terms and conditions required to register',
                               variable=cb_var,
                               font=('aerial', '12'),
                               bg='#8C52FF',
                               activebackground='#53688a')
    check_box.pack()
    check_box.place(x=200, y=650)

    def on_closing():

        """
                    when the client calls the exit function, the exit prompt is displayed confirming
                    whether the user actually wants to exit from the app
                """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            signup_window.destroy()
            sys.exit()

    signup_window.protocol("WM_DELETE_WINDOW", on_closing)

    def next_entry_box(*args):
        if len(sw_input_name_field_entry_box.get()) != 0:
            sw_input_email_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0:
            sw_input_address1_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0:
            sw_input_address2_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0 and len(sw_input_address2_field_entry_box.get()) != 0:
            sw_input_address3_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0 and len(sw_input_address2_field_entry_box.get()) != 0 and len(sw_input_address3_field_entry_box.get()) != 0:
            sw_input_phone_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0 and len(sw_input_address2_field_entry_box.get()) != 0 and len(sw_input_address3_field_entry_box.get()) != 0 and len(sw_input_phone_field_entry_box.get()) != 0:
            sw_input_username_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0 and len(sw_input_address2_field_entry_box.get()) != 0 and len(sw_input_address3_field_entry_box.get()) != 0 and len(sw_input_phone_field_entry_box.get()) != 0 and len(sw_input_username_field_entry_box.get()) != 0:
            sw_input_password1_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0 and len(sw_input_address2_field_entry_box.get()) != 0 and len(sw_input_address3_field_entry_box.get()) != 0 and len(sw_input_phone_field_entry_box.get()) != 0 and len(sw_input_username_field_entry_box.get()) != 0 and len(sw_input_password1_field_entry_box.get()) != 0:
            sw_input_password2_field_entry_box.focus_force()

        if len(sw_input_name_field_entry_box.get()) != 0 and len(sw_input_email_field_entry_box.get()) != 0 and len(sw_input_address1_field_entry_box.get()) != 0 and len(sw_input_address2_field_entry_box.get()) != 0 and len(sw_input_address3_field_entry_box.get()) != 0 and len(sw_input_phone_field_entry_box.get()) != 0 and len(sw_input_username_field_entry_box.get()) != 0 and len(sw_input_password1_field_entry_box.get()) != 0 and len(sw_input_password2_field_entry_box.get()) != 0:
            submit()

    signup_window.bind('<Return>', next_entry_box)

    # ____________________________ buttons ___________________________________________________

    def usr_exit_request():

        """
                    when the client calls the exit function, the exit prompt is displayed confirming
                    whether the user actually wants to exit from the app
                """

        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            signup_window.destroy()
            sys.exit()

    def redirect_to_login_window():

        """
                    when this method is called, the signup window is first destroyed and then the signup() function
                    is called from main_directory.signup file and the open_windows_list from main_directory.open_windows
                    gets appended by 'signup'
                """

        open_windows_list.append("signup")
        signup_window.destroy()
        from main_directory.LoginWindow import login
        login()

    def redirect_to_delete_window():

        """
                     when this method is called, the signup window is first destroyed and then the delete() function
                    is called from main_directory.delete file and the open_windows_list from main_directory.open_windows
                    gets appended by 'signup'
                """

        open_windows_list.append("signup")
        signup_window.destroy()
        from main_directory.DeleteWindow import delete
        delete()

    def redirect_to_documentation_window():

        """
                    when this method is called, the signup window is first destroyed and then the documentation() function
                    is called from main_directory.documentation file and the open_windows_list from main_directory.open_windows
                    gets appended by 'signup'
                """

        open_windows_list.append("signup")
        signup_window.destroy()
        documentation()

    # login button creation and placement along with the commands and methods
    login_button = tk.Button(signup_window, text='           Log In           ',
                             bg='#2d3a4d',
                             activeforeground='white',
                             activebackground='#546f7a',
                             fg='white',
                             relief=tk.FLAT,
                             command=redirect_to_login_window,
                             font=('Georgia', '10'))
    login_button.pack()
    login_button.place(x=60, y=20)
    login_button.bind('<Enter>', func=lambda e: login_button.config(bg='#64758f'))
    login_button.bind('<Leave>', func=lambda e: login_button.config(bg='#2d3a4d'))

    # delete account button creation and placement along with the commands and methods
    delete_button = tk.Button(signup_window, text='     Delete Account     ',
                              bg='#2d3a4d',
                              activeforeground='white',
                              activebackground='#546f7a',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_delete_window,
                              font=('Georgia', '10'))
    delete_button.pack()
    delete_button.place(x=184, y=20)
    delete_button.bind('<Enter>', func=lambda e: delete_button.config(bg='#64758f'))
    delete_button.bind('<Leave>', func=lambda e: delete_button.config(bg='#2d3a4d'))

    # documentation button creation and placement along with the commands and methods
    doc_button = tk.Button(signup_window, text=' Documentation ',
                           bg='#2d3a4d',
                           activeforeground='white',
                           activebackground='#546f7a',
                           fg='white',
                           relief=tk.FLAT,
                           command=redirect_to_documentation_window,
                           font=('Georgia', '10'))
    doc_button.pack()
    doc_button.place(x=680, y=30)
    doc_button.bind('<Enter>', func=lambda e: doc_button.config(bg='#64758f'))
    doc_button.bind('<Leave>', func=lambda e: doc_button.config(bg='#2d3a4d'))

    # exit button creation and placement along with the commands and methods
    exit_button = tk.Button(signup_window, text='     \n    Exit    \n     ',
                            bg='#2d3a4d',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            relief=tk.FLAT,
                            command=usr_exit_request,
                            font=('Georgia', '10'))
    exit_button.pack()
    exit_button.place(x=2, y=637)
    exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
    exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#2d3a4d'))

    # submit button creation and placement along with the commands and methods
    submit_button = tk.Button(signup_window, text='     Submit     ',
                              bg='#364f44',
                              activeforeground='black',
                              activebackground='#364f44',
                              fg='white',
                              relief=tk.FLAT,
                              command=submit,
                              font=('Georgia', '10'))
    submit_button.pack()
    submit_button.place(x=650, y=650)
    submit_button.bind('<Enter>', func=lambda e: submit_button.config(bg='#547a6a'))
    submit_button.bind('<Leave>', func=lambda e: submit_button.config(bg='#364f44'))

    # refresh button creation and placement along with the commands and methods
    def refresh():
        signup_window.destroy()
        signup_refresh_registry()

    refresh_label = tk.Label(signup_window, text='',
                             bg='#ff61f4',
                             font=('Georgia', '12'),
                             borderwidth=0)
    refresh_label.pack()
    refresh_label.place(x=70, y=95)

    refresh_button = tk.Button(signup_window, text='     \n     ♻      \n     ',
                               bg='#2d3a4d',
                               activeforeground='white',
                               activebackground='#546f7a',
                               relief=tk.FLAT,
                               fg='white',
                               command=refresh,
                               font=('Georgia', '10'))
    refresh_button.pack()
    refresh_button.place(x=2, y=75)
    refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#64758f'), refresh_label.config(text='   Refresh    ', bg='#2d3a4d', fg='white')))
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#2d3a4d'), refresh_label.config(text='', bg='#ff61f4')))

    # home button creation and placement along with the commands and methods
    def return_home():
        signup_window.destroy()
        open_windows_list.clear()
        from main_directory.HomeWindow import home
        home()

    home_label = tk.Label(signup_window, text='',
                          bg='#ff61f4',
                          font=('Georgia', '12'),
                          borderwidth=0)
    home_label.pack()
    home_label.place(x=70, y=155)

    home_button = tk.Button(signup_window, text='     \n  Home  \n     ',
                            bg='#2d3a4d',
                            activeforeground='white',
                            activebackground='#546f7a',
                            relief=tk.FLAT,
                            fg='white',
                            command=return_home,
                            font=('Georgia', '10'))
    home_button.pack()
    home_button.place(x=2, y=140)
    home_button.bind('<Enter>', func=lambda e: (home_button.config(bg='#64758f'), home_label.config(text='   Home    ', bg='#2d3a4d', fg='white')))
    home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#2d3a4d'), home_label.config(text='', bg='#ff61f4')))

    # chat box button creation and placement along with the commands and methods
    self_chat_box_label = tk.Label(signup_window, text='',
                                   bg='#664699',
                                   font=('Georgia', '12'),
                                   borderwidth=0)
    self_chat_box_label.pack()
    self_chat_box_label.place(x=70, y=420)

    def call_scb():
        open_windows_list.append('signup')
        signup_window.destroy()
        from main_directory.ChatBox__reg__utils__ import ChatApplicationWn
        chat_box = ChatApplicationWn()
        chat_box.run()

    self_chat_box_button = tk.Button(signup_window, text='     \n    Chat   \n     ',
                                     bg='#2d3a4d',
                                     activeforeground='white',
                                     activebackground='#546f7a',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_scb,
                                     font=('Georgia', '10'))
    self_chat_box_button.pack()
    self_chat_box_button.place(x=2, y=400)
    self_chat_box_button.bind('<Enter>', func=lambda e: (self_chat_box_button.config(bg='#64758f'), self_chat_box_label.config(text='   Chat Bot   ', bg='#2d3a4d', fg='white')))
    self_chat_box_button.bind('<Leave>', func=lambda e: (self_chat_box_button.config(bg='#2d3a4d'), self_chat_box_label.config(text='', bg='#664699')))

    # calendar button creation and placement along with the commands and methods
    self_calendar_label = tk.Label(signup_window, text='',
                                   bg='#664699',
                                   font=('Georgia', '12'),
                                   borderwidth=0)
    self_calendar_label.pack()
    self_calendar_label.place(x=70, y=350)

    def call_calendar():
        open_windows_list.append('signup')
        signup_window.destroy()
        from main_directory.Calendar__reg__utils__ import Calendar
        chat_box = Calendar()
        chat_box.run()

    self_calendar_button = tk.Button(signup_window, text='     \n       C       \n     ',
                                     bg='#2d3a4d',
                                     activeforeground='white',
                                     activebackground='#546f7a',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_calendar,
                                     font=('Georgia', '10'))
    self_calendar_button.pack()
    self_calendar_button.place(x=2, y=330)
    self_calendar_button.bind('<Enter>', func=lambda e: (self_calendar_button.config(bg='#64758f', fg='white'), self_calendar_label.config(text='   Calendar   ', bg='#2d3a4d', fg='white')))
    self_calendar_button.bind('<Leave>', func=lambda e: (self_calendar_button.config(bg='#2d3a4d', fg='white'), self_calendar_label.config(text='', bg='#664699')))

    class OptionsPaneHome:

        def __init__(self):

            """
                creating a context (option) menu when the user right clicks on any part of the signup window
                __init__ is used to initialise the class object named OptionPaneHome

                available options for the user:
                    1. refresh
                    2. chat box
                    3. calendar
                    4. exit
                    5. home
                    6. back

                if the context menu is left idle and unused, it will be destroyed after 5 seconds
            """

            super(OptionsPaneHome, self).__init__()

            self.options_signup_wn = tk.Tk()
            self.options_signup_wn.overrideredirect(True)
            self.options_signup_wn.config(bg='#1c1c1c')

            abs_coord_x = self.options_signup_wn.winfo_pointerx() - self.options_signup_wn.winfo_rootx()
            abs_coord_y = self.options_signup_wn.winfo_pointery() - self.options_signup_wn.winfo_rooty()
            self.options_signup_wn.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_signup_wn.geometry("100x178")

            # back button creation and placement along with the commands and methods
            opt_back_button = tk.Button(self.options_signup_wn,
                                        text='         Back           ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.__go_back__,
                                        activebackground='#3d3d3d')
            opt_back_button.pack()
            opt_back_button.place(x=0, y=0)
            opt_back_button.bind('<Enter>', func=lambda e: opt_back_button.config(bg='#3d3d3d'))
            opt_back_button.bind('<Leave>', func=lambda e: opt_back_button.config(bg='#1c1c1c'))

            # refresh button creation and placement along with the commands and methods
            opt_refresh_button = tk.Button(self.options_signup_wn,
                                           text='       Refresh       ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=self.refresh__,
                                           activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=30)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            # home button creation and placement along with the commands and methods
            opt_home_button = tk.Button(self.options_signup_wn,
                                        text=' Return Home     ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.return_home__,
                                        activebackground='#3d3d3d')
            opt_home_button.pack()
            opt_home_button.place(x=0, y=60)
            opt_home_button.bind('<Enter>', func=lambda e: opt_home_button.config(bg='#3d3d3d'))
            opt_home_button.bind('<Leave>', func=lambda e: opt_home_button.config(bg='#1c1c1c'))

            # chat box button creation and placement along with the commands and methods
            opt_chat_box_button = tk.Button(self.options_signup_wn,
                                            text='Open Chat Box  ',
                                            relief=tk.FLAT,
                                            font=('Georgia', '10'),
                                            bg='#1c1c1c',
                                            fg='white',
                                            command=self.cal_scb__,
                                            activebackground='#3d3d3d')
            opt_chat_box_button.pack()
            opt_chat_box_button.place(x=0, y=90)
            opt_chat_box_button.bind('<Enter>', func=lambda e: opt_chat_box_button.config(bg='#3d3d3d'))
            opt_chat_box_button.bind('<Leave>', func=lambda e: opt_chat_box_button.config(bg='#1c1c1c'))

            # calendar button creation and placement along with the commands and methods
            opt_calendar_button = tk.Button(self.options_signup_wn,
                                            text='Open Calendar  ',
                                            relief=tk.FLAT,
                                            font=('Georgia', '10'),
                                            bg='#1c1c1c',
                                            fg='white',
                                            command=self.call_calendar__,
                                            activebackground='#3d3d3d')
            opt_calendar_button.pack()
            opt_calendar_button.place(x=0, y=120)
            opt_calendar_button.bind('<Enter>', func=lambda e: opt_calendar_button.config(bg='#3d3d3d'))
            opt_calendar_button.bind('<Leave>', func=lambda e: opt_calendar_button.config(bg='#1c1c1c'))

            # exit button creation and placement along with the commands and methods
            opt_exit_button = tk.Button(self.options_signup_wn,
                                        text='           Exit          ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.exit__,
                                        activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=150)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            # binding the left button and the right button to the signup window
            signup_window.bind('<Button-1>', self.left_button_options__home)
            signup_window.bind('<Button-3>', self.right_button_options__home)

            # destroying the context (option) menu if left idle and unused
            self.options_signup_wn.after(5000, lambda: self.options_signup_wn.destroy())

        def run(self):

            """
                running the class object OptionPaneHome using the <tkinter_window>.mainloop() method
            """

            self.options_signup_wn.mainloop()

        def cal_scb__(self):
            self.options_signup_wn.destroy()
            call_scb()

        def refresh__(self):
            self.options_signup_wn.destroy()
            refresh()

        def return_home__(self):
            self.options_signup_wn.destroy()
            return_home()

        def call_calendar__(self):
            self.options_signup_wn.destroy()
            call_calendar()

        def exit__(self):
            self.options_signup_wn.destroy()
            usr_exit_request()

        def left_button_options__home(self, *args):
            try:
                self.options_signup_wn.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_signup_wn.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

        def __go_back__(self):

            """
                when the back button is pressed, the function checks the last element of the open windows list
                located in main_directory.open_windows.py. getting the last element, it pops it out og the list
                and then the signup window destroys and the last element that is stored in the variable is
                then read and the window is recalled and run .

                eg. if home is the last element of the list, then home is removed and then stored in a variable.
                the login window is destroyed and home is then called by calling the home function located at
                main_directory.home.py file.
            """

            length = len(open_windows_list)
            element = open_windows_list[length - 1]

            if element == 'home':
                open_windows_list.pop()
                from main_directory.HomeWindow import home
                self.options_signup_wn.destroy()
                signup_window.destroy()
                home()

            elif element == 'login':
                open_windows_list.pop()
                from main_directory.LoginWindow import login
                self.options_signup_wn.destroy()
                signup_window.destroy()
                login()

            elif element == 'delete':
                open_windows_list.pop()
                from main_directory.DeleteWindow import delete
                self.options_signup_wn.destroy()
                signup_window.destroy()
                delete()

            elif element == 'docs':
                open_windows_list.pop()
                from main_directory.DocumentationWindow import documentation
                self.options_signup_wn.destroy()
                signup_window.destroy()
                documentation()

    def relaunch_options_pane():

        """
            relaunching the option menu when the user does a repeated right click
        """

        options_pane = OptionsPaneHome()
        options_pane.run()

    def right_button_options__home(*args):

        """
            launching the option menu when a right click is performed
        """

        options_pane = OptionsPaneHome()
        options_pane.run()

    signup_window.bind('<Button-3>', right_button_options__home)  # binding the right button to the signup window

    def redirect_to_login_window_(*args):
        redirect_to_login_window()

    def redirect_to_delete_window_(*args):
        redirect_to_delete_window()

    def back_(*args):
        go_back()

    def call_calendar_(*args):
        call_calendar()

    def call_scb_(*args):
        call_scb()

    def refresh_(*args):
        refresh()

    def redirect_to_documentation_window_(*args):
        redirect_to_documentation_window()

    def exit_(*args):
        on_closing()

    signup_window.bind('<Control-l>', redirect_to_login_window_)
    signup_window.bind('<Control-d>', redirect_to_delete_window_)
    signup_window.bind('<Control-b>', back_)
    signup_window.bind('<Alt-c>', call_calendar_)
    signup_window.bind('<Control-r>', refresh_)
    signup_window.bind('<Control-t>', redirect_to_documentation_window_)
    signup_window.bind('<Control-h>', call_scb_)
    signup_window.bind('<Control-e>', exit_)

    def return_home_(*args):
        return_home()

    signup_window.bind('<Alt-h>', return_home_)

    # finally, running the login window (tkinter GUI) using <window_object>.mainloop()
    signup_window.mainloop()

# signup()
