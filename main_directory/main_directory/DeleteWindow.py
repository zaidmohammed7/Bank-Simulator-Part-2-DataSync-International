import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox
import time
import datetime
import sys

from main_directory.refresh_windows_functions_file import delete_refresh_registry
from main_directory.open_windows import open_windows_list
from main_directory.DocumentationWindow import documentation
from main_directory.password_functions_file import loading
from main_directory.password_functions_file import hash_password
from main_directory.operation_functions_pyfiles import del_otp

import threading

PopOutCalender_DELETE = []  # used to check the launch of the pop out calendar while returning to the delete window from the main calendar window
PopOutChatBox_DELETE = []  # used to check the launch of the pop out chat box while returning to the delete window from the main chat box window
REMOTE_SERVER = "one.one.one.one"

del_message="""Hello user, DataSync International is committed to the security and integrity of your credentials and hence, by the laws of the land, certain procedures can be time-consuming. 
    It's noticed that you have decided to delete your bank account. However, due to security reasons, you cannot alone carry out this. It is to notify you that deleting an account from the app ONLY DISABLES YOUR ACCOUNT for 6 months. However, if you want to disable your account briefly, here are some requirements for doing the same:
    -> your account balance should be null
    -> you are not supposed to have any pending loans
    Once you have disabled your account, your reference id shall be sent to you shortly and you are requested to visit your bank branch within the 6 months with the required documents such as a recent photo-id (Aadhar), bank checkbook, etc as mentioned in the bank sop website.

    We wish the best for your future. Happy banking with DataSync International!

    Regards
    Team DSI"""


def delete():
    """
        -> objective: starting the delete account window

        -> we create the delete account window using the modules tkinter and tkinter.ttk

        -> creating a delete account window with labels and buttons
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
            -> the delete account window also has the input boxes for the client to enter his account credentials
               -> entry boxes for: 1. username of the client
                                   2. password of the client

            once the user clicks a particular button, for example, the signup button,
            he/she will be redirected to the signup window.
            for this, the login window is first destroyed using the <tkinter_window>.destroy() method and
            the signup window is called from the signup file located in main_directory.signup

            this way of opening windows is followed by all the buttons be it login, signup,
            open chat box, calendar etc.

            at the last of the left sided menu, we can see the exit button that can be used by the client
            to exit the app

            on the centre of the window, there's the entry boxes for the username and password and also the submit button
            that calls the submit function which then connects to the mysql database and verifies the user credentials
    """

    print('[ INFO ] Tkinter [ Tkinter     ] : delete window loaded successfully')

    delete_window = tk.Tk()
    delete_window.title("Delete Account")
    delete_window.focus_force()
    delete_window.config(bg='#eb6a6a')
    delete_window.resizable(False, False)
    try:
        delete_window.iconbitmap(r'..\main_directory\ico1.ico')

        from PIL import ImageTk, Image
        image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic7.png"))

        img_lb = tk.Label(delete_window, image=image1, borderwidth=0)
        img_lb.pack()
        img_lb.place(x=0, y=500)
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    def run_pop_out_calender_delete():

        """
            we check the PopOutCalendar_DELETE list first.
            if the length of the list is equal to 1, only then will the calendar function further execute
            the function call.

            initially, the length of PopOutCalendar_DELETE list is 0 but when the PopOutCalendar is called from
            the main_directory.PopOutCalendar__reg__utils__ file, the list gets appended and the new length
            becomes 1

            hence, when the length of the list is 1, we again append another value to it to stop it from
            executing the same code again and again everytime the home window is called.

            when the function is called, the PopOutCalendar__reg__utils__ file containing PopOutCalendar
            object gets called and executed
        """

        if len(PopOutCalender_DELETE) == 1:
            PopOutCalender_DELETE.append(1)

            from main_directory.PopOutCalendar__reg__utils__ import PopOutCalendar
            app = PopOutCalendar()
            app.run()

    """
        now we check for running the pop out calendar if it is called by the client. After a certain time, 
        we run the run_pop_out_calendar_delete() function side by side to the actual delete() function.

        this way, the client can have a legitimate access to both the delete window and the calendar window
        at the same time
    """

    delete_window.after(10, lambda: run_pop_out_calender_delete())

    def run_pop_out_chat_box_delete():

        """
            we check the PopOutChatBox_DELETE list first.
            if the length of the list is equal to 1, only then will the chat box function further execute
            the function call.

            initially, the length of PopOutChatBox_DELETE list is 0 but when the PopOutChatBox is called from
            the main_directory.PopOutChatBox__reg__utils__ file, the list gets appended and the new length
            becomes 1

            hence, when the length of the list is 1, we again append another value to it to stop it from
            executing the same code again and again everytime the home window is called.

            when the function is called, the PopOutChatBox__reg__utils__ file containing PopOutChatBox
            object gets called and executed
                        """

        if len(PopOutChatBox_DELETE) == 1:
            PopOutChatBox_DELETE.append(1)

            from main_directory.PopOutChatBox__reg__utils__ import PopOutChatBox
            app = PopOutChatBox()
            app.run()

    """
        now we check for running the pop out chat box if it is called by the client. After a certain time, 
        we run the run_pop_out_chat_box_delete() function side by side to the actual delete() function.

        this way, the client can have a legitimate access to both the delete window and the chat box window
        at the same time
    """

    delete_window.after(10, lambda: run_pop_out_chat_box_delete())

    # ______________fixing window on screen__________credit: stack_overflow

    w = 800  # width for the Tk root
    h = 600  # height for the Tk root

    # get screen width and height
    ws = delete_window.winfo_screenwidth()  # width of the screen
    hs = delete_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    delete_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    # _________________fixing window on screen_END___________________________

    heading = tk.Label(delete_window, text='Delete Account',
                       bg='#eb6a6a',
                       font=('Georgia', '40'))
    heading.pack()
    heading.place(x=250, y=75)

    # _________________________design - start________________________________

    label1 = tk.Label(delete_window, text='',
                      bg='#690a1d',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    label2 = tk.Label(delete_window, text='',
                      bg='#690a1d',
                      width=150,
                      height=2,
                      font=('Georgia', '20'))
    label2.pack()
    label2.place(x=0, y=0)

    # _________________________design - end___________________________________

    # _________________time module display -start___________credit: stack_overflow

    clock = tk.Label(delete_window,
                     bg='#690a1d',
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
    date_label = tk.Label(delete_window,
                          text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                          bg='#690a1d',
                          fg='white',
                          font=('Georgia', '10'))
    date_label.pack()
    date_label.place(x=590, y=0)

    # ________________________date display - end_____________________________

    # mode
    mode = tk.Label(delete_window, text='', bg='#690a1d', font=('Helvetica', '10'))
    mode.pack()
    mode.place(x=510, y=0)

    def mode_function():
        from connection import is_connected as connection

        check_connection = connection(REMOTE_SERVER)

        if check_connection is True:
            mode.config(fg='#34eb43', text='ONLINE')
            mode.after(5000, mode_function)
        else:
            mode.config(fg='#dea9a9', text='OFFLINE')
            mode.after(5000, mode_function)

    threading.Thread(target=mode_function, daemon=True).start()

    # _____________________initial_window_setup_completed____________________

    # __________________________body of the window___________________________

    # back button creation and placement along with the commands and functions
    def go_back():

        """
                when the back button is pressed, the function checks the last element of the open windows list
                located in main_directory.open_windows.py. getting the last element, it pops it out og the list
                and then the delete window destroys and the last element that is stored in the variable is
                then read and the window is recalled and run.

                eg. if home is the last element of the list, then home is removed and then stored in a variable.
                the login window is destroyed and home is then called by calling the home function located at
                main_directory.home.py file.
        """

        length = len(open_windows_list)
        element = open_windows_list[length - 1]

        if element == 'home':
            open_windows_list.pop()
            from main_directory.HomeWindow import home
            delete_window.destroy()
            home()

        elif element == 'signup':
            open_windows_list.pop()
            from main_directory.SignupWindow import signup
            delete_window.destroy()
            signup()

        elif element == 'login':
            open_windows_list.pop()
            from main_directory.LoginWindow import login
            delete_window.destroy()
            login()

        elif element == 'docs':
            open_windows_list.pop()
            from main_directory.DocumentationWindow import documentation
            delete_window.destroy()
            documentation()

    go_back_button = tk.Button(delete_window,
                               text="  Back  ",
                               bg='#690a1d',
                               relief=tk.FLAT,
                               activeforeground='white',
                               activebackground='#9e4a65',
                               fg='white',
                               command=go_back,
                               font=('Georgia', '10'))
    go_back_button.pack()
    go_back_button.place(x=5, y=20)
    go_back_button.bind('<Enter>', func=lambda e: go_back_button.config(bg='#eb6a6a'))
    go_back_button.bind('<Leave>', func=lambda e: go_back_button.config(bg='#690a1d'))

    # refresh button creation and placement along with the commands and functions
    def refresh():
        delete_window.destroy()
        delete_refresh_registry()

    refresh_label = tk.Label(delete_window, text='',
                             bg='#eb6a6a',
                             font=('Georgia', '12'))
    refresh_label.pack()
    refresh_label.place(x=70, y=95)

    refresh_button = tk.Button(delete_window, text='     \n     ♻      \n     ',
                               bg='#690a1d',
                               activeforeground='white',
                               activebackground='#9e4a65',
                               relief=tk.FLAT,
                               fg='white',
                               command=refresh,
                               font=('Georgia', '10'))
    refresh_button.pack()
    refresh_button.place(x=2, y=75)
    refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#eb6a6a'), refresh_label.config(text='   Refresh    ', bg='#690a1d', fg='white')))
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#690a1d'), refresh_label.config(text='', bg='#eb6a6a', fg='white')))

    # home button creation and placement along with the commands and functions
    def return_home():
        delete_window.destroy()
        open_windows_list.clear()
        from main_directory.HomeWindow import home
        home()

    home_label = tk.Label(delete_window, text='',
                          bg='#eb6a6a',
                          font=('Georgia', '12'))
    home_label.pack()
    home_label.place(x=70, y=155)

    home_button = tk.Button(delete_window, text='     \n  Home  \n     ',
                            bg='#690a1d',
                            activeforeground='white',
                            activebackground='#9e4a65',
                            relief=tk.FLAT,
                            fg='white',
                            command=return_home,
                            font=('Georgia', '10'))
    home_button.pack()
    home_button.place(x=2, y=140)
    home_button.bind('<Enter>', func=lambda e: (home_button.config(bg='#eb6a6a'), home_label.config(text='   Home    ', bg='#690a1d', fg='white')))
    home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#690a1d'), home_label.config(text='', bg='#eb6a6a', fg='white')))

    # calendar button creation and placement along with the commands and functions
    self_calendar_label = tk.Label(delete_window, text='',
                                   bg='#eb6a6a',
                                   font=('Georgia', '12'))
    self_calendar_label.pack()
    self_calendar_label.place(x=70, y=350)

    def call_calendar():
        open_windows_list.append('delete')
        delete_window.destroy()
        from main_directory.Calendar__reg__utils__ import Calendar
        chat_box = Calendar()
        chat_box.run()

    self_calendar_button = tk.Button(delete_window, text='     \n       C       \n     ',
                                     bg='#690a1d',
                                     activeforeground='white',
                                     activebackground='#9e4a65',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_calendar,
                                     font=('Georgia', '10'))
    self_calendar_button.pack()
    self_calendar_button.place(x=2, y=330)
    self_calendar_button.bind('<Enter>', func=lambda e: (self_calendar_button.config(bg='#eb6a6a', fg='white'), self_calendar_label.config(text='   Calendar   ', bg='#690a1d', fg='white')))
    self_calendar_button.bind('<Leave>', func=lambda e: (self_calendar_button.config(bg='#690a1d', fg='white'), self_calendar_label.config(text='', bg='#eb6a6a')))

    # chat box button creation and placement along with the commands and functions
    self_chat_box_label = tk.Label(text='',
                                   bg='#eb6a6a',
                                   font=('Georgia', '12'))
    self_chat_box_label.pack()
    self_chat_box_label.place(x=70, y=420)

    def call_scb():
        open_windows_list.append('delete')
        delete_window.destroy()
        from main_directory.ChatBox__reg__utils__ import ChatApplicationWn
        chat_box = ChatApplicationWn()
        chat_box.run()

    self_chat_box_button = tk.Button(delete_window, text='     \n    Chat   \n     ',
                                     bg='#690a1d',
                                     activeforeground='white',
                                     activebackground='#9e4a65',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_scb,
                                     font=('Georgia', '10'))
    self_chat_box_button.pack()
    self_chat_box_button.place(x=2, y=400)
    self_chat_box_button.bind('<Enter>', func=lambda e: (self_chat_box_button.config(bg='#eb6a6a', fg='white'), self_chat_box_label.config(text='   Chat Bot   ', bg='#690a1d', fg='white')))
    self_chat_box_button.bind('<Leave>', func=lambda e: (self_chat_box_button.config(bg='#690a1d', fg='white'), self_chat_box_label.config(text='', bg='#eb6a6a')))

    def on_closing():

        """
            when the client calls the exit function, the exit prompt is displayed confirming
            whether the user actually wants to exit from the app
        """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            delete_window.destroy()
            sys.exit()

    delete_window.protocol("WM_DELETE_WINDOW", on_closing)

    # _________________________________ buttons ___________________________________

    def usr_exit_request():

        """
                when the client calls the exit function, the exit prompt is displayed confirming
                whether the user actually wants to exit from the app
        """

        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            delete_window.destroy()
            sys.exit()

    def redirect_to_login_window():

        """
                    when this method is called, the delete window is first destroyed and then the login() function
                    is called from main_directory.login file and the open_windows_list from main_directory.open_windows
                    gets appended by 'delete'
                """

        open_windows_list.append("delete")
        delete_window.destroy()
        from main_directory.LoginWindow import login
        login()

    def redirect_to_signup_window():

        """
                    when this method is called, the delete window is first destroyed and then the signup() function
                    is called from main_directory.signup file and the open_windows_list from main_directory.open_windows
                    gets appended by 'delete'
                """

        open_windows_list.append("delete")
        delete_window.destroy()
        from main_directory.SignupWindow import signup
        signup()

    def redirect_to_documentation_window():

        """
                    when this method is called, the delete window is first destroyed and then the documentation() function
                    is called from main_directory.documentation file and the open_windows_list from main_directory.open_windows
                    gets appended by 'delete'
                """

        open_windows_list.append("delete")
        delete_window.destroy()
        documentation()

    # login button creation and placement along with the commands and methods
    login_button = tk.Button(delete_window, text='           Log In           ',
                             bg='#690a1d',
                             activeforeground='white',
                             activebackground='#9e4a65',
                             fg='white',
                             relief=tk.FLAT,
                             command=redirect_to_login_window,
                             font=('Georgia', '10'))
    login_button.pack()
    login_button.place(x=64, y=20)
    login_button.bind('<Enter>', func=lambda e: login_button.config(bg='#eb6a6a'))
    login_button.bind('<Leave>', func=lambda e: login_button.config(bg='#690a1d'))

    # signup button creation and placement along with the commands and methods
    signup_button = tk.Button(delete_window, text='          Signup          ',
                              bg='#690a1d',
                              activeforeground='white',
                              activebackground='#9e4a65',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_signup_window,
                              font=('Georgia', '10'))
    signup_button.pack()
    signup_button.place(x=184, y=20)
    signup_button.bind('<Enter>', func=lambda e: signup_button.config(bg='#eb6a6a'))
    signup_button.bind('<Leave>', func=lambda e: signup_button.config(bg='#690a1d'))

    # documentation button creation and placement along with the commands and methods
    doc_button = tk.Button(delete_window, text=' Documentation ',
                           bg='#690a1d',
                           activeforeground='white',
                           activebackground='#9e4a65',
                           fg='white',
                           relief=tk.FLAT,
                           command=redirect_to_documentation_window,
                           font=('Georgia', '10'))
    doc_button.pack()
    doc_button.place(x=680, y=30)
    doc_button.bind('<Enter>', func=lambda e: doc_button.config(bg='#eb6a6a'))
    doc_button.bind('<Leave>', func=lambda e: doc_button.config(bg='#690a1d'))

    # exit button creation and placement along with the commands and methods
    exit_button = tk.Button(delete_window, text='     \n    Exit    \n     ',
                            bg='#690a1d',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            relief=tk.FLAT,
                            command=usr_exit_request,
                            font=('Georgia', '10'))
    exit_button.pack()
    exit_button.place(x=2, y=537)
    exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
    exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#690a1d'))

    # _____________________________________ submit button function ___________________________________
    def submit():

        """
                when the user clicks the submit button, the submit() function is called.
                the function requires both client's username and the password

                once the username is taken, the app connects to the mysql database where it is checked
                if the username entered by the user actually exists or not

                then the password entered is hashed to verify the authenticity of the client and if both the username
                and the hashed password value (sha512) is found in a record, the client is allowed to further continue
                with the account deletion process and will be led to the delete confirmation window in the delete_confirm_window
                located in main_directory.delete_confirm_window.py

                the delete window is destroyed
        """

        username = dw_input_username_field_entry_box.get()
        username = username.lstrip().rstrip()

        if len(username) == 0:
            messagebox.showerror(title='Username Error', message='Enter a valid username')

        else:

            check_pwd = dw_input_password1_field_entry_box.get()
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
                            check_username_fn.config(fg='black', text='', bg='#eb6a6a')
                            password = dw_input_password1_field_entry_box.get()
                            password = password.lstrip().rstrip()

                            check__check_box_value = cb_var.get()

                            if check__check_box_value == 1:

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
                                        if len(final_password) != 0:
                                            check_pwd_fn.config(bg='#eb6a6a', text='')
                                            cur = connection.cursor()
                                            cur.execute(f"SELECT NAME, BALANCE, EMAIL FROM client WHERE USERNAME='{username}'")
                                            __name__ = cur.fetchall()
                                            name = __name__[0][0]
                                            balance = __name__[0][1]
                                            user_email = __name__[0][2]
                                            balance_int_type = balance[3:]

                                            if float(balance_int_type) > 0:
                                                messagebox.showerror(title='Account error', message='You cannot delete your account!')
                                                messagebox.showinfo(title='Info', message="""Hello user, DataSync International is committed to the security and integrity of your credentials and hence, by the laws of the land, certain procedures can be time-consuming. 
                                                It's noticed that you have decided to delete your bank account. However, due to security reasons, you cannot alone carry out this. It is to notify you that deleting an account from the app ONLY DISABLES YOUR ACCOUNT for 6 months. However, if you want to disable your account briefly, here are some requirements for doing the same:
                                                -> your account balance should be null
                                                -> you are not supposed to have any pending loans
                                                Once you have disabled your account, your reference id shall be sent to you shortly and you are requested to visit your bank branch within the 6 months with the required documents such as a recent photo-id (Aadhar), bank checkbook, etc as mentioned in the bank sop website.

                                                We wish the best for your future. Happy banking with DataSync International!

                                                Regards
                                                Team DSI""")

                                            else:
                                                cur___ = connection.cursor()
                                                cur___.execute(f"SELECT ACCOUNT_IN_USE_PERMISSION FROM client WHERE USERNAME = '{username}'")
                                                result___ = cur___.fetchall()
                                                cur.close()

                                                __value__ = result___[0][0]

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

                                                            msg = """Hello user, DataSync International is committed to the security and integrity of your credentials and hence, by the laws of the land, certain procedures can be time-consuming. 
                                                            It's noticed that you have decided to delete your bank account. However, due to security reasons, you cannot alone carry out this. It is to notify you that deleting an account from the app ONLY DISABLES YOUR ACCOUNT for 6 months. However, if you want to disable your account briefly, here are some requirements for doing the same:
                                                            -> your account balance should be null
                                                            -> you are not supposed to have any pending loans
                                                            Once you have disabled your account, your reference id shall be sent to you shortly and you are requested to visit your bank branch within the 6 months with the required documents such as a recent photo-id (Aadhar), bank checkbook, etc as mentioned in the bank sop website.

                                                            We wish the best for your future. Happy banking with DataSync International!"""

                                                            yag = yagmail.SMTP(server_email, server_pwd)
                                                            yag.send(f"{final_email}", 'Verification', f"Hello {final_name}\n\nHere is your one time password: {__otp__}\n\nDO NOT SHARE THIS\n\n\nRegards\nTeam DSI\n\n\n=======================================================\nALSO NOTE:\n{msg}")

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
                                                                    messagebox.showinfo(title="Important", message=del_message)

                                                                    delete_window.destroy()
                                                                    email_ver_win.destroy()

                                                                    from delete_confirm_window import del_confirm
                                                                    del_confirm(username, name, user_email)

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
                                                        messagebox.showinfo(title="Important", message=del_message)

                                                        delete_window.destroy()
                                                        del_otp(username, name, user_email)
                                                else:
                                                    messagebox.showinfo(title="Important", message=del_message)

                                                    delete_window.destroy()
                                                    from delete_confirm_window import del_confirm
                                                    del_confirm(username, name, user_email)
                                        else:
                                            check_pwd_fn.config(text='incorrect password', fg='red', bg='white')
                                            messagebox.showerror(title='Server error', message='Data not found!')

                                        pass
                                    else:
                                        messagebox.showerror(title='Server error', message='The server crashed')
                                    pass
                                else:
                                    messagebox.showerror(title='Password error', message='Enter a valid password')

                            else:
                                messagebox.showerror(title=' Agreement Error', message='You have not agreed to the terms and conditions!')

                        else:
                            check_username_fn.config(text='username not found', fg='red', bg='white')
                            messagebox.showerror(title='Username error', message='Username not found!')
                    else:
                        messagebox.showerror(title='Server Error', message='The server crashed')
                else:
                    messagebox.showerror(title='Username error', message='Enter valid username !')

    # __________________________________________ username field  _________________________________________

    dw_display_username_field_label = tk.Label(delete_window,
                                               bg='#eb6a6a',
                                               text="Enter your username  :",
                                               font=('aerial', '12'))
    dw_display_username_field_label.pack()
    dw_display_username_field_label.place(x=150, y=200)

    dw_input_username_field_entry_box = ttk.Entry(delete_window,
                                                  width=40,
                                                  font=('aerial', '12'))
    dw_input_username_field_entry_box.pack()
    dw_input_username_field_entry_box.place(x=350, y=200)

    dw_input_username_field_entry_box.focus_force()

    # __________________________________________ password 1 field  _________________________________________

    dw_display_password1_field_label = tk.Label(delete_window,
                                                bg='#eb6a6a',
                                                text="Enter your password  :",
                                                font=('aerial', '12'))
    dw_display_password1_field_label.pack()
    dw_display_password1_field_label.place(x=150, y=300)

    dw_input_password1_field_entry_box = ttk.Entry(delete_window,
                                                   show='*',
                                                   width=40,
                                                   font=('aerial', '12'))
    dw_input_password1_field_entry_box.pack()
    dw_input_password1_field_entry_box.place(x=350, y=300)

    def hide_pwd():
        pin___label.config(command=show_pwd, text=' ○ ')
        dw_input_password1_field_entry_box.configure(show='*')
        pass

    def show_pwd():
        pin___label.config(command=hide_pwd, text=' — ')
        dw_input_password1_field_entry_box.configure(show='')
        pass

    pin___label = tk.Button(delete_window,
                            text=' ○ ',
                            command=show_pwd,
                            relief=tk.FLAT,
                            bg='#eb6a6a',
                            activeforeground='black',
                            activebackground='#c73e53'
                            )
    pin___label.pack()
    pin___label.place(x=720, y=300)

    check_username_fn = tk.Label(delete_window,
                                 text='',
                                 fg='black',
                                 bg='#eb6a6a')
    check_username_fn.pack()
    check_username_fn.place(x=650, y=230)

    check_pwd_fn = tk.Label(delete_window,
                            text='',
                            fg='black',
                            bg='#eb6a6a')
    check_pwd_fn.pack()
    check_pwd_fn.place(x=650, y=330)

    # __________________________ check box __________________________________________

    cb_var = tk.IntVar()
    check_box = tk.Checkbutton(delete_window, text='I agree to take responsibility of the current action',
                               variable=cb_var,
                               font=('aerial', '12'),
                               bg='#eb6a6a',
                               activebackground='#a14d70')
    check_box.pack()
    check_box.place(x=250, y=400)

    def go_to_next_textbox(*args):

        """
            goes to the next entry text field i.e. the password entry box when the return key is pressed
        """

        if len(dw_input_username_field_entry_box.get()) != 0:
            dw_input_password1_field_entry_box.focus_force()
        if len(dw_input_username_field_entry_box.get()) != 0 and len(dw_input_password1_field_entry_box.get()) != 0:
            submit()
            pass

    delete_window.bind('<Return>', go_to_next_textbox)  # binding the 'return' key to the delete window

    def go_up(*args):
        dw_input_username_field_entry_box.focus_force()

    def go_down(*args):
        dw_input_password1_field_entry_box.focus_force()

    delete_window.bind('<Up>', go_up)  # binding the up-arrow key to delete window
    delete_window.bind('<Down>', go_down)  # binding the down-arrow key to delete window

    # submit button creation and placement along with the commands and functions
    submit_button = tk.Button(delete_window, text='     Submit     ',
                              bg='#690a1d',
                              activeforeground='black',
                              activebackground='#c73e53',
                              fg='white',
                              relief=tk.FLAT,
                              command=submit,
                              font=('Georgia', '10'))
    submit_button.pack()
    submit_button.place(x=370, y=500)
    submit_button.bind('<Enter>', func=lambda e: submit_button.config(bg='#961b2e', fg='white'))
    submit_button.bind('<Leave>', func=lambda e: submit_button.config(bg='#690a1d', fg='white'))

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

            self.options_delete_wn = tk.Tk()
            self.options_delete_wn.overrideredirect(True)
            self.options_delete_wn.config(bg='#1c1c1c')

            abs_coord_x = self.options_delete_wn.winfo_pointerx() - self.options_delete_wn.winfo_rootx()
            abs_coord_y = self.options_delete_wn.winfo_pointery() - self.options_delete_wn.winfo_rooty()
            self.options_delete_wn.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_delete_wn.geometry("100x178")

            # back button creation and placement along with the commands and methods
            opt_back_button = tk.Button(self.options_delete_wn,
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
            opt_refresh_button = tk.Button(self.options_delete_wn,
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
            opt_home_button = tk.Button(self.options_delete_wn,
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
            opt_chat_box_button = tk.Button(self.options_delete_wn,
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
            opt_calendar_button = tk.Button(self.options_delete_wn,
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
            opt_exit_button = tk.Button(self.options_delete_wn,
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
            delete_window.bind('<Button-1>', self.left_button_options__home)
            delete_window.bind('<Button-3>', self.right_button_options__home)

            # destroying the context (option) menu if left idle and unused
            self.options_delete_wn.after(5000, lambda: self.options_delete_wn.destroy())

        def run(self):

            """
                 running the class object OptionPaneHome using the <tkinter_window>.mainloop() method
            """

            self.options_delete_wn.mainloop()

        def cal_scb__(self):
            self.options_delete_wn.destroy()
            call_scb()

        def refresh__(self):
            self.options_delete_wn.destroy()
            refresh()

        def return_home__(self):
            self.options_delete_wn.destroy()
            return_home()

        def call_calendar__(self):
            self.options_delete_wn.destroy()
            call_calendar()

        def exit__(self):
            self.options_delete_wn.destroy()
            usr_exit_request()

        def left_button_options__home(self, *args):
            try:
                self.options_delete_wn.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_delete_wn.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

        def __go_back__(self):

            """
                when the back button is pressed, the function checks the last element of the open windows list
                located in main_directory.open_windows.py. getting the last element, it pops it out og the list
                and then the delete window destroys and the last element that is stored in the variable is
                then read and the window is recalled and run.

                eg. if home is the last element of the list, then home is removed and then stored in a variable.
                the login window is destroyed and home is then called by calling the home function located at
                main_directory.home.py file.
            """

            length = len(open_windows_list)
            element = open_windows_list[length - 1]

            if element == 'home':
                open_windows_list.pop()
                from main_directory.HomeWindow import home
                self.options_delete_wn.destroy()
                delete_window.destroy()
                home()

            elif element == 'signup':
                open_windows_list.pop()
                from main_directory.SignupWindow import signup
                self.options_delete_wn.destroy()
                delete_window.destroy()
                signup()

            elif element == 'login':
                open_windows_list.pop()
                from main_directory.LoginWindow import login
                self.options_delete_wn.destroy()
                delete_window.destroy()
                login()

            elif element == 'docs':
                open_windows_list.pop()
                from main_directory.DocumentationWindow import documentation
                self.options_delete_wn.destroy()
                delete_window.destroy()
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

    delete_window.bind('<Button-3>', right_button_options__home)  # binding the right button to the login window

    def redirect_to_login_window_(*args):
        redirect_to_login_window()

    def back_(*args):
        go_back()

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

    delete_window.bind('<Control-l>', redirect_to_login_window_)
    delete_window.bind('<Control-b>', back_)
    delete_window.bind('<Control-s>', redirect_to_signup_window_)
    delete_window.bind('<Alt-c>', call_calendar_)
    delete_window.bind('<Control-r>', refresh_)
    delete_window.bind('<Control-t>', redirect_to_documentation_window_)
    delete_window.bind('<Control-h>', call_scb_)
    delete_window.bind('<Control-e>', exit_)

    def return_home_(*args):
        return_home()

    delete_window.bind('<Alt-h>', return_home_)

    # finally, running the login window (tkinter GUI) using <window_object>.mainloop()
    delete_window.mainloop()
