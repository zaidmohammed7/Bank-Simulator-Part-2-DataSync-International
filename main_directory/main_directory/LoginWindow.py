import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import datetime
import sys

from main_directory.refresh_windows_functions_file import login_refresh_registry
from main_directory.open_windows import open_windows_list
from main_directory.password_functions_file import hash_password
from main_directory.password_functions_file import loading
from main_directory.operation_functions_pyfiles import otp

import threading

PopOutCalender_LOGIN = []   # used to check the launch of the pop out calendar while returning to the login window from the main calendar window
PopOutChatBox_LOGIN = []  # used to check the launch of the pop out chat box while returning to the login window from the main chat box window
REMOTE_SERVER = "one.one.one.one"


def login():
    """
        -> objective: starting the login window

        -> we create the login window using the modules tkinter and tkinter.ttk

        -> creating a login window with labels and buttons
           -> labels include visual displays and details when the client reacts with the app
           -> buttons can be used by the client to visit various other windows:
                               1. return to home button
                               2. signup window button
                               3. delete account window button
                               4. documentation window buttons
                               5. refresh home window buttons
                               6. launch calendar button
                               7. launch chat box button
                               8. launch chat box BETA button
                               9. exit button
                               10. back button
        -> the login window also has the input boxes for the client to enter his account credentials
           -> entry boxes for: 1. username of the client
                               2. password of the client

        once the user clicks a particular button, for example, the signup button,
        he/she will be redirected to the signup window.
        for this, the login window is first destroyed using the <tkinter_window>.destroy() method and
        the signup window is called from the signup file located in main_directory.signup

        this way of opening windows is followed by all the buttons be it login, delete account,
        open chat box, calendar etc.

        at the last of the left sided menu, we can see the exit button that can be used by the client
        to exit the app

        on the centre of the window, there's the entry boxes for the username and password and also the submit button
        that calls the submit function which then connects to the mysql database and verifies the user credentials
    """

    print('[ INFO ] Tkinter [ Tkinter     ] : login window loaded successfully')

    """
        first we create the login window named the login_window and perform certain operations on it
        like resize, adding title, put a background colour and make in non-resizable since tkinter does not
        change the positions of hard-coded accessories placement on the window
    """

    login_window = tk.Tk()
    login_window.title("Log Into Your Account")
    login_window.focus_force()
    login_window.config(bg='#66ffaf')
    login_window.resizable(False, False)
    try:
        login_window.iconbitmap(r'..\main_directory\ico1.ico')

        from PIL import ImageTk, Image
        image2 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\login.png"))

        img_lb2 = tk.Label(login_window, image=image2, borderwidth=0)
        img_lb2.pack()
        img_lb2.place(x=0, y=0)
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    def run_pop_out_calender_login():

        """
            we check the PopOutCalendar_LOGIN list first.
            if the length of the list is equal to 1, only then will the calendar function further execute
            the function call.

            initially, the length of PopOutCalendar_LOGIN list is 0 but when the PopOutCalendar is called from
            the main_directory.PopOutCalendar__reg__utils__ file, the list gets appended and the new length
            becomes 1

            hence, when the length of the list is 1, we again append another value to it to stop it from
            executing the same code again and again everytime the home window is called.

            when the function is called, the PopOutCalendar__reg__utils__ file containing PopOutCalendar
            object gets called and executed
        """

        if len(PopOutCalender_LOGIN) == 1:
            PopOutCalender_LOGIN.append(1)

            from main_directory.PopOutCalendar__reg__utils__ import PopOutCalendar
            app = PopOutCalendar()
            app.run()

    """
        now we check for running the pop out calendar if it is called by the client. After a certain time, 
        we run the run_pop_out_calendar_login() function side by side to the actual login() function.

        this way, the client can have a legitimate access to both the login window and the calendar window
        at the same time
    """

    login_window.after(10, lambda: run_pop_out_calender_login())

    def run_pop_out_chat_box_login():

        """
            we check the PopOutChatBox_LOGIN list first.
            if the length of the list is equal to 1, only then will the chat box function further execute
            the function call.

            initially, the length of PopOutChatBox_LOGIN list is 0 but when the PopOutChatBox is called from
            the main_directory.PopOutChatBox__reg__utils__ file, the list gets appended and the new length
            becomes 1

            hence, when the length of the list is 1, we again append another value to it to stop it from
            executing the same code again and again everytime the home window is called.

            when the function is called, the PopOutChatBox__reg__utils__ file containing PopOutChatBox
            object gets called and executed
        """

        if len(PopOutChatBox_LOGIN) == 1:
            PopOutChatBox_LOGIN.append(1)
            from main_directory.PopOutChatBox__reg__utils__ import PopOutChatBox
            app = PopOutChatBox()
            app.run()

    """
        now we check for running the pop out chat box if it is called by the client. After a certain time, 
        we run the run_pop_out_chat_box_login() function side by side to the actual login() function.

        this way, the client can have a legitimate access to both the login window and the chat box window
        at the same time
    """

    login_window.after(10, lambda: run_pop_out_chat_box_login())

    # ______________fixing window on screen__________credit: stack_overflow

    w = 800  # width for the Tk root
    h = 600  # height for the Tk root

    # get screen width and height
    ws = login_window.winfo_screenwidth()  # width of the screen
    hs = login_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    login_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    # # _________________fixing window on screen_END___________________________
    #
    # heading = tk.Label(login_window, text='Login',
    #                    bg='#66ffaf',
    #                    font=('Georgia', '40'))
    # heading.pack()
    # heading.place(x=350, y=75)

    # _________________________design - start________________________________

    # here we start designing the home_window window with different colors and labels and texts

    label1 = tk.Label(login_window, text='',
                      bg='#127544',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    label2 = tk.Label(login_window, text='',
                      bg='#127544',
                      width=150,
                      height=2,
                      font=('Georgia', '20'))
    label2.pack()
    label2.place(x=0, y=0)

    # _________________________design - end___________________________________

    # _________________time module display -start___________credit: stack_overflow

    clock = tk.Label(login_window,
                     bg='#127544',
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
    date_label = tk.Label(login_window,
                          text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                          bg='#127544',
                          fg='white',
                          font=('Georgia', '10'))
    date_label.pack()
    date_label.place(x=590, y=0)

    # ________________________date display - end_____________________________

    # mode
    mode = tk.Label(login_window, text='', bg='#127544', font=('Helvetica', '10'))
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

    # __________________________body of the window___________________________

    # go back button creation and placement along with the commands and functions
    def go_back():

        """
        when the back button is pressed, the function checks the last element of the open windows list
        located in main_directory.open_windows.py. getting the last element, it pops it out og the list
        and then the login window destroys and the last element that is stored in the variable is
        then read and the window is recalled and run.

        eg. if home is the last element of the list, then home is removed and then stored in a variable.
        the login window is destroyed and home is then called by calling the home function located at
        main_directory.home.py file.
        """

        length = len(open_windows_list)
        element = open_windows_list[length-1]

        if element == 'home':
            open_windows_list.pop()
            from main_directory.HomeWindow import home
            login_window.destroy()
            home()

        elif element == 'signup':
            open_windows_list.pop()
            from main_directory.SignupWindow import signup
            login_window.destroy()
            signup()

        elif element == 'delete':
            open_windows_list.pop()
            from main_directory.DeleteWindow import delete
            login_window.destroy()
            delete()

        elif element == 'docs':
            open_windows_list.pop()
            from main_directory.DocumentationWindow import documentation
            login_window.destroy()
            documentation()

    go_back_button = tk.Button(login_window,
                               text="  Back  ",
                               bg='#127544',
                               relief=tk.FLAT,
                               activeforeground='white',
                               activebackground='#3b785a',
                               fg='white',
                               command=go_back,
                               font=('Georgia', '10'))
    go_back_button.pack()
    go_back_button.place(x=5, y=20)
    go_back_button.bind('<Enter>', func=lambda e: go_back_button.config(bg='#66ffaf', fg='black'))
    go_back_button.bind('<Leave>', func=lambda e: go_back_button.config(bg='#127544', fg='white'))

    # refresh button creation and placement along with the commands and functions
    def refresh():
        login_window.destroy()
        login_refresh_registry()

    refresh_label = tk.Label(login_window, text='',
                             bg='#06140C',
                             font=('Georgia', '12'),
                             borderwidth=0)
    refresh_label.pack()
    refresh_label.place(x=70, y=95)

    refresh_button = tk.Button(login_window, text='     \n     ♻      \n     ',
                               bg='#127544',
                               activeforeground='white',
                               activebackground='#3b785a',
                               relief=tk.FLAT,
                               fg='white',
                               command=refresh,
                               font=('Georgia', '10'))
    refresh_button.pack()
    refresh_button.place(x=2, y=75)
    refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#66ffaf', fg='black'), refresh_label.config(text='   Refresh    ', bg='#127544', fg='white')))
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#127544', fg='white'), refresh_label.config(text='', bg='#06140C')))

    # home button creation and placement along with the commands and functions
    def return_home():
        login_window.destroy()
        open_windows_list.clear()
        from main_directory.HomeWindow import home
        home()

    home_label = tk.Label(login_window, text='',
                          bg='#06140C',
                          font=('Georgia', '12'),
                          borderwidth=0)
    home_label.pack()
    home_label.place(x=70, y=155)

    home_button = tk.Button(login_window, text='     \n  Home  \n     ',
                            bg='#127544',
                            activeforeground='white',
                            activebackground='#3b785a',
                            relief=tk.FLAT,
                            fg='white',
                            command=return_home,
                            font=('Georgia', '10'))
    home_button.pack()
    home_button.place(x=2, y=140)
    home_button.bind('<Enter>', func=lambda e: (home_button.config(bg='#66ffaf', fg='black'), home_label.config(text='   Home    ', bg='#127544', fg='white')))
    home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#127544', fg='white'), home_label.config(text='', bg='#06140C')))

    # admin back button creation and placement along with the commands and functions
    def go_admin():
        login_window.destroy()
        from main_directory.admin.admin_login import AdminLogin
        AdminLogin().run()

    admin_label = tk.Label(login_window, text='',
                           bg='#06140C',
                           font=('Georgia', '12'),
                           borderwidth=0)
    admin_label.pack()
    admin_label.place(x=70, y=220)

    admin_button = tk.Button(login_window, text='     \n Admin  \n     ',
                             bg='#127544',
                             activeforeground='white',
                             activebackground='#3b785a',
                             relief=tk.FLAT,
                             fg='white',
                             command=go_admin,
                             font=('Georgia', '10'))
    admin_button.pack()
    admin_button.place(x=2, y=205)
    admin_button.bind('<Enter>', func=lambda e: (admin_button.config(bg='#66ffaf', fg='black'), admin_label.config(text='   Admin    ', bg='#127544', fg='white')))
    admin_button.bind('<Leave>', func=lambda e: (admin_button.config(bg='#127544', fg='white'), admin_label.config(text='', bg='#06140C')))

    def on_closing():

        """
            when the client calls the exit function, the exit prompt is displayed confirming
            whether the user actually wants to exit from the app
        """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            login_window.destroy()
            sys.exit()

    login_window.protocol("WM_DELETE_WINDOW", on_closing)

    # _____________________________________ submit button function ___________________________________
    def submit():

        """
                when the user clicks the submit button, the submit() function is called.
                the function requires both client's username and the password

                once the username is taken, the app connects to the mysql database where it is checked
                if the username entered by the user actually exists or not

                then the password entered is hashed to verify the authenticity of the client and if both the username
                and the hashed password value (sha512) is found in a record, the client is allowed to further continue
                with the account procedures and will be led to the account window in the account_window() object
                located in main_directory.account_window.py

                the login window is destroyed
        """

        username = lw_input_username_field_entry_box.get()
        username = username.lstrip().rstrip()

        if len(username) == 0:
            messagebox.showerror(title='Username Error', message='Enter a valid username')

        else:

            check_pwd = lw_input_password1_field_entry_box.get()
            check_pwd = check_pwd.lstrip().rstrip()

            if len(check_pwd) == 0:
                messagebox.showerror(title='Password Error', message='Enter a valid password')

            elif len(check_pwd) < 8:
                messagebox.showerror(title='Password Length Error', message='Enter a valid password')

            else:

                if username.isascii():
                    import mysql.connector as sql

                    connection = sql.connect(host='localhost',
                                             user='root',
                                             password='dpsbn',
                                             database='client_db')

                    if connection.is_connected() is True:
                        cursor = connection.cursor()
                        cursor.execute(f"SELECT USERNAME FROM client WHERE USERNAME = '{username}'")
                        result = cursor.fetchall()
                        cursor.close()

                        if len(result) != 0:
                            check_username_fn.config(fg='black', text='')
                            password = lw_input_password1_field_entry_box.get()
                            password = password.lstrip().rstrip()

                            if password.isascii():
                                cursor2 = connection.cursor()
                                cursor2.execute(f"SELECT PASSWORD_SALT FROM client WHERE USERNAME='{username}'")
                                salt = cursor2.fetchall()
                                cursor2.close()
                                if len(salt) != 0:

                                    __object__ = threading.Thread(target=loading, daemon=True)
                                    __object__.start()

                                    final_salt = salt[0][0]
                                    final_hash_password = hash_password(final_salt, password)
                                    cursor3 = connection.cursor()
                                    cursor3.execute(f"SELECT PASSWORD FROM client WHERE PASSWORD='{final_hash_password}' AND USERNAME='{username}'")
                                    final_password = cursor3.fetchall()
                                    cursor3.close()
                                    if len(final_password) != 0:
                                        cur = connection.cursor()
                                        cur.execute(f"SELECT NAME FROM client WHERE USERNAME='{username}'")
                                        __name__ = cur.fetchall()
                                        name = __name__[0][0]

                                        cur = connection.cursor()
                                        cur.execute(f"SELECT ACCOUNT_IN_USE_PERMISSION FROM client WHERE USERNAME = '{username}'")
                                        result = cur.fetchall()
                                        cur.close()

                                        __value__ = result[0][0]

                                        if __value__ == 'True':
                                            send_email_verification = messagebox.askyesnocancel(title="Email Verification", message="Do you want email verification?\n\nClick YES for email verification\nClick NO for normal on-device verification")

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

                                                    new_conn = connection.cursor()
                                                    new_conn.execute(f"SELECT NAME, EMAIL FROM client WHERE USERNAME = '{username}'")
                                                    new_conn_result = new_conn.fetchall()
                                                    final_name = new_conn_result[0][0]
                                                    final_email = new_conn_result[0][1]

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
                                                            login_window.destroy()
                                                            email_ver_win.destroy()

                                                            def notify_fn(title='DataSync Intl', message='You have logged in successfully!'):
                                                                from plyer import notification
                                                                notification.notify(title, message, timeout=5)

                                                            __object___n = threading.Thread(target=notify_fn)
                                                            __object___n.start()

                                                            from account_window import account_window
                                                            account_window(username, name)
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
                                                login_window.destroy()
                                                otp(username, name)
                                        else:
                                            login_window.destroy()

                                            def notify(title='DataSync Intl', message='You have logged in successfully!'):
                                                from plyer import notification
                                                notification.notify(title, message, timeout=5)

                                            __object___ = threading.Thread(target=notify)
                                            __object___.start()

                                            from account_window import account_window
                                            account_window(username, name)
                                    else:
                                        check_pwd_fn.config(text='incorrect password', fg='red')
                                        messagebox.showerror(title='Server error', message='Data not found!')

                                    pass
                                else:
                                    messagebox.showerror(title='Server error', message='The server crashed')
                                pass
                            else:
                                messagebox.showerror(title='Password error', message='Enter a valid password')

                        else:
                            check_username_fn.config(text='username not found', fg='red')
                            messagebox.showerror(title='Username error', message='Username not found!')
                    else:
                        messagebox.showerror(title='Server Error', message='The server crashed')
                else:
                    messagebox.showerror(title='Username error', message='Enter valid username !')

    # ____________________________________buttons___________________________________________

    def usr_exit_request():

        """
            when the client calls the exit function, the exit prompt is displayed confirming
            whether the user actually wants to exit from the app
        """

        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            login_window.destroy()
            sys.exit()

    def redirect_to_signup_window():

        """
            when this method is called, the login window is first destroyed and then the signup() function
            is called from main_directory.signup file and the open_windows_list from main_directory.open_windows
            gets appended by 'login'
        """

        open_windows_list.append("login")
        login_window.destroy()
        from main_directory.SignupWindow import signup
        signup()

    def redirect_to_delete_window():

        """
             when this method is called, the login window is first destroyed and then the delete() function
            is called from main_directory.delete file and the open_windows_list from main_directory.open_windows
            gets appended by 'login'
        """

        open_windows_list.append("login")
        login_window.destroy()
        from main_directory.DeleteWindow import delete
        delete()

    def redirect_to_documentation_window():

        """
            when this method is called, the login window is first destroyed and then the documentation() function
            is called from main_directory.documentation file and the open_windows_list from main_directory.open_windows
            gets appended by 'login'
        """

        open_windows_list.append("login")
        login_window.destroy()
        from main_directory.DocumentationWindow import documentation
        documentation()

    # now we start creating the buttons for the clint to visit different windows

    '''
    the buttons created are:
    1. signup
    2. delete account
    3. documentation -- these all are located at the top options menu

    1. refresh
    2. calendar
    3. chat box
    4. chat box BETA
    5. exit -- these all are located at the left-sided option menu
    '''

    # signup button creation and placement along with the commands
    signup_button = tk.Button(login_window, text='          Signup          ',
                              bg='#127544',
                              activeforeground='white',
                              activebackground='#3b785a',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_signup_window,
                              font=('Georgia', '10'))
    signup_button.pack()
    signup_button.place(x=64, y=20)
    signup_button.bind('<Enter>', func=lambda e: signup_button.config(bg='#66ffaf', fg='black'))
    signup_button.bind('<Leave>', func=lambda e: signup_button.config(bg='#127544', fg='white'))

    # doc (documentation) button creation and placement along with the commands
    doc_button = tk.Button(login_window, text=' Documentation ',
                           bg='#127544',
                           activeforeground='white',
                           activebackground='#3b785a',
                           fg='white',
                           relief=tk.FLAT,
                           command=redirect_to_documentation_window,
                           font=('Georgia', '10'))
    doc_button.pack()
    doc_button.place(x=680, y=30)
    doc_button.bind('<Enter>', func=lambda e: doc_button.config(bg='#66ffaf', fg='black'))
    doc_button.bind('<Leave>', func=lambda e: doc_button.config(bg='#127544', fg='white'))

    # delete account button creation and placement along with the commands
    delete_button = tk.Button(login_window, text='     Delete Account     ',
                              bg='#127544',
                              activeforeground='white',
                              activebackground='#3b785a',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_delete_window,
                              font=('Georgia', '10'))
    delete_button.pack()
    delete_button.place(x=184, y=20)
    delete_button.bind('<Enter>', func=lambda e: delete_button.config(bg='#66ffaf', fg='black'))
    delete_button.bind('<Leave>', func=lambda e: delete_button.config(bg='#127544', fg='white'))

    # exit button creation and placement along with the commands
    exit_button = tk.Button(login_window, text='     \n    Exit    \n     ',
                            bg='#127544',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            relief = tk.FLAT,
                            command=usr_exit_request,
                            font=('Georgia', '10'))
    exit_button.pack()
    exit_button.place(x=2, y=537)
    exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
    exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#127544'))

    # __________________________________________ username field  _________________________________________

    # lw_display_username_field_label = tk.Label(login_window,
    #                                            bg='#66ffaf',
    #                                            text="Enter your username  :",
    #                                            font=('aerial', '12'))
    # lw_display_username_field_label.pack()
    # lw_display_username_field_label.place(x=150, y=200)

    lw_input_username_field_entry_box = ttk.Entry(login_window,
                                                  width=25,
                                                  font=('aerial', '12'))
    lw_input_username_field_entry_box.pack()
    lw_input_username_field_entry_box.place(x=460, y=321)

    lw_input_username_field_entry_box.focus_force()

    # __________________________________________ password 1 field  _________________________________________

    # lw_display_password1_field_label = tk.Label(login_window,
    #                                             bg='#66ffaf',
    #                                             text="Enter your password  :",
    #                                             font=('aerial', '12'))
    # lw_display_password1_field_label.pack()
    # lw_display_password1_field_label.place(x=150, y=300)

    lw_input_password1_field_entry_box = ttk.Entry(login_window,
                                                   show='*',
                                                   width=25,
                                                   font=('aerial', '12'))
    lw_input_password1_field_entry_box.pack()
    lw_input_password1_field_entry_box.place(x=460, y=398)

    def hide_pwd():
        pin___label.config(command=show_pwd, text=' ○ ')
        lw_input_password1_field_entry_box.configure(show='*')
        pass

    def show_pwd():
        pin___label.config(command=hide_pwd, text=' — ')
        lw_input_password1_field_entry_box.configure(show='')
        pass

    pin___label = tk.Button(login_window,
                            text=' ○ ',
                            command=show_pwd,
                            relief=tk.FLAT,
                            bg='#364f44',
                            fg='white',
                            borderwidth=0)
    pin___label.pack()
    pin___label.place(x=720, y=397)

    check_username_fn = tk.Label(login_window,
                                 text='',
                                 fg='black',
                                 bg='#06140C',
                                 borderwidth=0)
    check_username_fn.pack()
    check_username_fn.place(x=650, y=350)

    check_pwd_fn = tk.Label(login_window,
                            text='',
                            fg='black',
                            bg='#06140C',
                            borderwidth=0)
    check_pwd_fn.pack()
    check_pwd_fn.place(x=650, y=425)

    def go_to_next_textbox(*args):

        """
                goes to the next entry text field i.e. the password entry box when the return key is pressed
        """

        if len(lw_input_username_field_entry_box.get()) != 0:
            lw_input_password1_field_entry_box.focus_force()
        if len(lw_input_username_field_entry_box.get()) != 0 and len(lw_input_password1_field_entry_box.get()) != 0:
            submit()

    login_window.bind('<Return>', go_to_next_textbox)  # binding the 'return' key to the login_window

    def go_up(*args):
        lw_input_username_field_entry_box.focus_force()

    def go_down(*args):
        lw_input_password1_field_entry_box.focus_force()

    login_window.bind('<Up>', go_up)  # binding the up-arrow key to login_window
    login_window.bind('<Down>', go_down)  # binding the down-arrow key to login_window

    submit_button = tk.Button(login_window, text='\n     Submit     \n',
                              bg='#364f44',
                              activeforeground='white',
                              activebackground='#364f44',
                              fg='white',
                              relief=tk.FLAT,
                              command=submit,
                              font=('Georgia', '10'))
    submit_button.pack()
    submit_button.place(x=370, y=520)
    submit_button.bind('<Enter>', func=lambda e: submit_button.config(bg='#547a6a'))
    submit_button.bind('<Leave>', func=lambda e: submit_button.config(bg='#364f44'))

    # call chat box (scb) button creation and placement along with the commands and functions
    self_chat_box_label = tk.Label(text='',
                                   bg='#06140C',
                                   font=('Georgia', '12'),
                                   borderwidth=0)
    self_chat_box_label.pack()
    self_chat_box_label.place(x=70, y=420)

    def call_scb():

        """
            when the client calls the call_scb() function, the current login_window gets destroyed and
            the ChatApplicationWn() object is called from the main_directory.ChatBox__Reg__utils__.py file
            and is run
        """

        open_windows_list.append('login')
        login_window.destroy()
        from main_directory.ChatBox__reg__utils__ import ChatApplicationWn
        chat_box = ChatApplicationWn()
        chat_box.run()

    self_chat_box_button = tk.Button(login_window, text='     \n    Chat   \n     ',
                                     bg='#127544',
                                     activeforeground='white',
                                     activebackground='#3b785a',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_scb,
                                     font=('Georgia', '10'))
    self_chat_box_button.pack()
    self_chat_box_button.place(x=2, y=400)
    self_chat_box_button.bind('<Enter>', func=lambda e: (self_chat_box_button.config(bg='#66ffaf', fg='black'), self_chat_box_label.config(text='   Chat Bot   ', bg='#127544', fg='white')))
    self_chat_box_button.bind('<Leave>', func=lambda e: (self_chat_box_button.config(bg='#127544', fg='white'), self_chat_box_label.config(text='', bg='#06140C')))

    # call calendar button creation and placement along with the commands and functions
    self_calendar_label = tk.Label(login_window, text='',
                                   bg='#06140C',
                                   font=('Georgia', '12'),
                                   borderwidth=0)
    self_calendar_label.pack()
    self_calendar_label.place(x=70, y=350)

    def call_calendar():

        """
            when the client calls the call_calendar() function, the current login_window gets destroyed and
            the Calendar() object is called from the main_directory.Calendar__reg__utils__.py file
            and is run and the open_windows_list is appended with 'home'
        """

        open_windows_list.append('login')
        login_window.destroy()
        from main_directory.Calendar__reg__utils__ import Calendar
        chat_box = Calendar()
        chat_box.run()

    self_calendar_button = tk.Button(login_window, text='     \n       C       \n     ',
                                     bg='#127544',
                                     activeforeground='white',
                                     activebackground='#3b785a',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_calendar,
                                     font=('Georgia', '10'))
    self_calendar_button.pack()
    self_calendar_button.place(x=2, y=330)
    self_calendar_button.bind('<Enter>', func=lambda e: (self_calendar_button.config(bg='#66ffaf', fg='black'), self_calendar_label.config(text='   Calendar   ', bg='#127544', fg='white')))
    self_calendar_button.bind('<Leave>', func=lambda e: (self_calendar_button.config(bg='#127544', fg='white'), self_calendar_label.config(text='', bg='#06140C')))

    """ 
        creating the context (option) menu for the user when he/she does a right click
        class object -- OptionPaneHome
        right-mouse-button (<Button-3>) bound to home_window
    """

    class OptionsPaneHome:

        def __init__(self):

            """
                creating a context (option) menu when the user right clicks on any part of the login_window
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

            self.options_login_wn = tk.Tk()
            self.options_login_wn.overrideredirect(True)
            self.options_login_wn.config(bg='#1c1c1c')

            abs_coord_x = self.options_login_wn.winfo_pointerx() - self.options_login_wn.winfo_rootx()
            abs_coord_y = self.options_login_wn.winfo_pointery() - self.options_login_wn.winfo_rooty()
            self.options_login_wn.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_login_wn.geometry("100x178")

            # back button creation and placement along with the commands and methods
            opt_back_button = tk.Button(self.options_login_wn,
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
            opt_refresh_button = tk.Button(self.options_login_wn,
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
            opt_home_button = tk.Button(self.options_login_wn,
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
            opt_chat_box_button = tk.Button(self.options_login_wn,
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
            opt_calendar_button = tk.Button(self.options_login_wn,
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
            opt_exit_button = tk.Button(self.options_login_wn,
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

            # binding the left button and the right button to the login window
            login_window.bind('<Button-1>', self.left_button_options__home)
            login_window.bind('<Button-3>', self.right_button_options__home)

            # destroying the context (option) menu if left idle and unused
            self.options_login_wn.after(5000, lambda: self.options_login_wn.destroy())

        def run(self):

            """
                running the class object OptionPaneHome using the <tkinter_window>.mainloop() method
            """

            self.options_login_wn.mainloop()

        def cal_scb__(self):
            self.options_login_wn.destroy()
            call_scb()

        def refresh__(self):
            self.options_login_wn.destroy()
            refresh()

        def return_home__(self):
            self.options_login_wn.destroy()
            return_home()

        def call_calendar__(self):
            self.options_login_wn.destroy()
            call_calendar()

        def exit__(self):
            self.options_login_wn.destroy()
            usr_exit_request()

        def left_button_options__home(self, *args):
            try:
                self.options_login_wn.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_login_wn.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

        def __go_back__(self):

            """
                when the back button is pressed, the function checks the last element of the open windows list
                located in main_directory.open_windows.py. getting the last element, it pops it out og the list
                and then the login window destroys and the last element that is stored in the variable is
                then read and the window is recalled and run .

                eg. if home is the last element of the list, then home is removed and then stored in a variable.
                the login window is destroyed and home is then called by calling the home function located at
                main_directory.home.py file.
            """

            length = len(open_windows_list)
            element = open_windows_list[length - 1]

            if element == 'home':
                open_windows_list.pop()
                from HomeWindow import home
                self.options_login_wn.destroy()
                login_window.destroy()
                home()

            elif element == 'signup':
                open_windows_list.pop()
                from SignupWindow import signup
                self.options_login_wn.destroy()
                login_window.destroy()
                signup()

            elif element == 'delete':
                open_windows_list.pop()
                from DeleteWindow import delete
                self.options_login_wn.destroy()
                login_window.destroy()
                delete()

            elif element == 'docs':
                open_windows_list.pop()
                from DocumentationWindow import documentation
                self.options_login_wn.destroy()
                login_window.destroy()
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

    login_window.bind('<Button-3>', right_button_options__home)  # binding the right button to the login window

    def back_(*args):
        go_back()

    def redirect_to_delete_window_(*args):
        redirect_to_delete_window()

    def redirect_to_signup_window_(*args):
        redirect_to_signup_window()

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

    login_window.bind('<Control-b>', back_)
    login_window.bind('<Control-d>', redirect_to_delete_window_)
    login_window.bind('<Control-s>', redirect_to_signup_window_)
    login_window.bind('<Alt-c>', call_calendar_)
    login_window.bind('<Control-r>', refresh_)
    login_window.bind('<Control-t>', redirect_to_documentation_window_)
    login_window.bind('<Control-h>', call_scb_)
    login_window.bind('<Control-e>', exit_)

    def go_admin_fn(*args):
        go_admin()

    login_window.bind('<Control-a>', go_admin_fn)

    def return_home_(*args):
        return_home()

    login_window.bind('<Alt-h>', return_home_)

    # finally, running the login window (tkinter GUI) using <window_object>.mainloop()
    login_window.mainloop()
