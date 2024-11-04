import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import datetime
import sys

from main_directory.LoginWindow import login
from main_directory.open_windows import open_windows_list
from main_directory.SignupWindow import signup
from main_directory.DeleteWindow import delete
from main_directory.DocumentationWindow import documentation
from main_directory.refresh_windows_functions_file import home_refresh_registry
from main_directory.card_number import hash_pin
from main_directory.password_functions_file import loading
from main_directory.operation_functions_pyfiles import card_otp
import threading

PopOutCalender_HOME = []  # used to check the launch of the pop out calendar while returning to the home window from the main calendar window
PopOutChatBox_HOME = []  # used to check the launch of the pop out chat box while returning to the home window from the main chat box window
dsi_check = []
chat_box_check = []
REMOTE_SERVER = "one.one.one.one"


def home():
    """
    -> objective: starting the home window

    -> we create the home window using the modules tkinter and tkinter.ttk

    -> creating a home window with labels and buttons
       -> labels include visual displays and details when the client reacts with the app
       -> buttons can be used by the client to visit various other windows:
                           1. login window button
                           2. signup window button
                           3. delete account window button
                           4. documentation window buttons
                           5. refresh home window buttons
                           6. launch calendar button
                           7. launch chat box button
                           8. launch chat box BETA button
                           9. exit button
    -> the home window also has the input boxes for the client to enter his banking credentials
       -> entry boxes for: 1. Card number of the client
                           2. Pin number of the client

    once the user clicks a particular button, for example, the login button,
    he/she will be redirected to the login window.
    for this, the home window is first destroyed using the <tkinter_window>.destroy() method and
    the login window is called from the login file located in main_directory.login

    this way of opening windows is followed by all the buttons be it sighup, delete account,
    open chat box, calendar etc.

    at the last of the left sided menu, we can see the exit button that can be used byt he client
    to exit the app

    on the right half of the window, there's the entry boxes for the card and in numbers and also the submit button
    that call the submit function which then connects to the mysql database and verifies the user credentials
    """

    print('[ INFO ] Tkinter [ Tkinter     ] : home window loaded successfully')

    # _____________________initial_window_setup____________________________

    """
    first we create the home window named the home_window and perform certain operations on it
    like resize, adding title, put a background colour and make in non-resizable since tkinter does not
    change the positions of hard-coded accessories placement on the window
    """

    home_window = tk.Tk()
    home_window.focus_force()
    home_window.title("Welcome Home")
    home_window.config(bg='#5E17EB')
    home_window.resizable(False, False)
    try:
        home_window.iconbitmap(r'..\main_directory\ico1.ico')  # we add an icon image

        # ________________________________   images   __________________________________

        from PIL import ImageTk, Image
        image2 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic2.png"))

        img_lb = tk.Label(image=image2, borderwidth=0)
        img_lb.pack()
        img_lb.place(x=0, y=0)
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    def run_pop_out_calender_home():

        """
        we check the PopOutCalendar_HOME list first.
        if the length of the list is equal to 1, only then will the calendar function further execute
        the function call.

        initially, the length of PopOutCalendar_HOME list is 0 but when the PopOutCalendar is called from
        the main_directory.PopOutCalendar__reg__utils__ file, the list gets appended and the new length
        becomes 1

        hence, when the length of the list is 1, we again append another value to it to stop it from
        executing the same code again and again everytime the home window is called.

        when the function is called, the PopOutCalendar__reg__utils__ file containing PopOutCalendar
        object gets called and executed
        """

        if len(PopOutCalender_HOME) == 1:
            PopOutCalender_HOME.append(1)

            from main_directory.PopOutCalendar__reg__utils__ import PopOutCalendar
            app = PopOutCalendar()
            app.run()

    """
    now we check for running the pop out calendar if it is called by the client. After a certain time, 
    we run the run_pop_out_calendar_home() function side by side to the actual home() function.

    this way, the client can have a legitimate access to both the home window and the calendar window
    at the same time
    """

    home_window.after(10, lambda: run_pop_out_calender_home())

    def run_pop_out_chat_box_home():

        """
        we check the PopOutChatBox_HOME list first.
        if the length of the list is equal to 1, only then will the chat box function further execute
        the function call.

        initially, the length of PopOutChatBox_HOME list is 0 but when the PopOutChatBox is called from
        the main_directory.PopOutChatBox__reg__utils__ file, the list gets appended and the new length
        becomes 1

        hence, when the length of the list is 1, we again append another value to it to stop it from
        executing the same code again and again everytime the home window is called.

        when the function is called, the PopOutChatBox__reg__utils__ file containing PopOutChatBox
        object gets called and executed
        """

        if len(PopOutChatBox_HOME) == 1:
            PopOutChatBox_HOME.append(1)

            from main_directory.PopOutChatBox__reg__utils__ import PopOutChatBox
            app = PopOutChatBox()
            app.run()

    """
    now we check for running the pop out chat box if it is called by the client. After a certain time, 
    we run the run_pop_out_chat_box_home() function side by side to the actual home() function.

    this way, the client can have a legitimate access to both the home window and the chat box window
    at the same time
    """

    home_window.after(10, lambda: run_pop_out_chat_box_home())

    # ___________________fixing window on screen_START_______credit: stack_overflow

    w = 800  # width for the Tk root
    h = 600  # height for the Tk root

    # get screen width and height
    ws = home_window.winfo_screenwidth()  # width of the screen
    hs = home_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    home_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # home_window.geometry('800x600')

    # _________________fixing window on screen_END___________________________

    # _________________________design - start________________________________

    # here we start designing the home_window window with different colors and labels and texts

    label1 = tk.Label(home_window, text='',
                      bg='#6F6135',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    label2 = tk.Label(home_window, text='',
                      bg='#6F6135',
                      width=150,
                      height=2,
                      font=('Georgia', '20'))
    label2.pack()
    label2.place(x=0, y=0)

    # _________________________design - end___________________________________

    # _________________time module display - START___________credit: stack_overflow

    clock = tk.Label(home_window,
                     bg='#6F6135',
                     fg='white',
                     font=('Georgia', '10'))
    clock.pack()
    clock.place(x=720, y=0)

    def tick():  # credit: StackOverflow
        updated_time = time.strftime('%H:%M:%S')
        clock.config(text=updated_time + '   ')
        clock.after(200, tick)

    threading.Thread(target=tick, daemon=True).start()

    # ________________________time display - END_____________________________

    # ________________________date display - START__________credit: stack_overflow

    date = datetime.datetime.now()
    date_label = tk.Label(home_window,
                          text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                          bg='#6F6135',
                          fg='white',
                          font=('Georgia', '10'))
    date_label.pack()
    date_label.place(x=590, y=0)

    # ________________________date display - END_____________________________

    # mode
    mode = tk.Label(home_window, text='', bg='#6F6135', font=('Helvetica', '10'))
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

    def usr_exit_request():

        """
        when the client calls the exit function, the exit prompt is displayed confirming
        whether the user actually wants to exit from the app
        """

        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            home_window.destroy()
            sys.exit()

    def redirect_to_login_window():

        """
        when this method is called, the home window is first destroyed and then the login() function
        is called from main_directory.login file and the open_windows_list from main_directory.open_windows
        gets appended by 'home'
        """

        open_windows_list.append("home")
        home_window.destroy()
        login()

    def redirect_to_signup_window():

        """
        when this method is called, the home window is first destroyed and then the signup() function
        is called from main_directory.signup file and the open_windows_list from main_directory.open_windows
        gets appended by 'home'
        """

        open_windows_list.append("home")
        home_window.destroy()
        signup()

    def redirect_to_delete_window():

        """
        when this method is called, the home window is first destroyed and then the delete() function
        is called from main_directory.delete file and the open_windows_list from main_directory.open_windows
        gets appended by 'home'
         """

        open_windows_list.append("home")
        home_window.destroy()
        delete()

    def redirect_to_documentation_window():

        """
        when this method is called, the home window is first destroyed and then the documentation() function
        is called from main_directory.documentation file and the open_windows_list from main_directory.open_windows
        gets appended by 'home'
        """

        open_windows_list.append("home")
        home_window.destroy()
        documentation()

    # now we start creating the buttons for the clint to visit different windows

    '''
    the buttons created are:
    1. login
    2. signup
    3. delete account
    4. documentation -- these all are located at the top options menu

    1. refresh
    2. calendar
    3. chat box
    4. chat box BETA
    5. exit -- these all are located at the left-sided option menu
    '''

    # login button creation and placement along with the commands
    login_button = tk.Button(home_window, text='           Log In           ',
                             bg='#6F6135',
                             activeforeground='white',
                             activebackground='#6D5406',
                             fg='white',
                             relief=tk.FLAT,
                             command=redirect_to_login_window,
                             font=('Georgia', '10'))
    login_button.pack()
    login_button.place(x=64, y=20)
    login_button.bind('<Enter>', func=lambda e: login_button.config(bg='#C4B071', fg='black'))
    login_button.bind('<Leave>', func=lambda e: login_button.config(bg='#6F6135', fg='white'))

    # signup button creation and placement along with the commands
    signup_button = tk.Button(home_window, text='          Signup          ',
                              bg='#6F6135',
                              activeforeground='white',
                              activebackground='#6D5406',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_signup_window,
                              font=('Georgia', '10'))
    signup_button.pack()
    signup_button.place(x=184, y=20)
    signup_button.bind('<Enter>', func=lambda e: signup_button.config(bg='#C4B071', fg='black'))
    signup_button.bind('<Leave>', func=lambda e: signup_button.config(bg='#6F6135', fg='white'))

    # delete account button creation and placement along with the commands
    delete_button = tk.Button(home_window, text='   Delete Account   ',
                              bg='#6F6135',
                              activeforeground='white',
                              activebackground='#6D5406',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_delete_window,
                              font=('Georgia', '10'))
    delete_button.pack()
    delete_button.place(x=304, y=20)
    delete_button.bind('<Enter>', func=lambda e: delete_button.config(bg='#C4B071', fg='black'))
    delete_button.bind('<Leave>', func=lambda e: delete_button.config(bg='#6F6135', fg='white'))

    # doc (documentation) button creation and placement along with the commands
    doc_button = tk.Button(home_window, text=' Documentation ',
                           bg='#6F6135',
                           activeforeground='white',
                           activebackground='#6D5406',
                           fg='white',
                           relief=tk.FLAT,
                           command=redirect_to_documentation_window,
                           font=('Georgia', '10'))
    doc_button.pack()
    doc_button.place(x=680, y=30)
    doc_button.bind('<Enter>', func=lambda e: doc_button.config(bg='#C4B071', fg='black'))
    doc_button.bind('<Leave>', func=lambda e: doc_button.config(bg='#6F6135', fg='white'))

    # exit button creation and placement along with the commands
    exit_button = tk.Button(home_window, text='     \n    Exit    \n     ',
                            bg='#6F6135',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            command=usr_exit_request,
                            relief=tk.FLAT,
                            font=('Georgia', '10'))
    exit_button.pack()
    exit_button.place(x=2, y=537)
    exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
    exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#6F6135'))

    def on_closing():

        """
        when the client calls the exit function, the exit prompt is displayed confirming
        whether the user actually wants to exit from the app
        """

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            home_window.destroy()
            sys.exit()

    home_window.protocol("WM_DELETE_WINDOW", on_closing)

    # refresh button creation and placement along with the commands and methods
    def refresh():

        """
        when the client calls the refresh function, the current home_window gets destroyed and
        the home_refresh_registry() method is called from the main_directory.refresh_registry.py file
        """

        home_window.destroy()
        home_refresh_registry()

    refresh_label = tk.Label(home_window, text='',
                             bg='#6F6135',
                             font=('Georgia', '12'),
                             borderwidth=0)
    refresh_label.pack()
    refresh_label.place(x=65, y=95)

    refresh_button = tk.Button(home_window, text='     \n     ♻      \n     ',
                               bg='#6F6135',
                               activeforeground='white',
                               activebackground='#6D5406',
                               relief=tk.FLAT,
                               fg='white',
                               command=refresh,
                               font=('Georgia', '10'))
    refresh_button.pack()
    refresh_button.place(x=2, y=75)
    refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#C4B071', fg='black'), refresh_label.config(text='   Refresh    ', bg='#C4B071', fg='black')))
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#6F6135', fg='white'), refresh_label.config(text='', bg='#6F6135')))

    # call chat box button creation and placement along with the commands
    # call chat box (scb) button creation and placement along with the commands and functions
    self_chat_box_label = tk.Label(home_window, text='',
                                   bg='#121317',
                                   font=('Georgia', '12'),
                                   borderwidth=0)
    self_chat_box_label.pack()
    self_chat_box_label.place(x=70, y=420)

    def call_scb():

        """
        when the client calls the call_scb() function, the current home_window gets destroyed and
        the ChatApplicationWn() object is called from the main_directory.ChatBox__Reg__utils__.py file
        and is run
        """

        open_windows_list.append('home')
        home_window.destroy()
        from main_directory.ChatBox__reg__utils__ import ChatApplicationWn
        chat_box = ChatApplicationWn()
        chat_box.run()

    self_chat_box_button = tk.Button(home_window, text='     \n    Chat   \n     ',
                                     bg='#6F6135',
                                     activeforeground='white',
                                     activebackground='#6D5406',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_scb,
                                     font=('Georgia', '10'))
    self_chat_box_button.pack()
    self_chat_box_button.place(x=2, y=400)
    self_chat_box_button.bind('<Enter>', func=lambda e: (self_chat_box_button.config(bg='#C4B071', fg='black'), self_chat_box_label.config(text='   Chat Bot    ', bg='#C4B071', fg='black')))
    self_chat_box_button.bind('<Leave>', func=lambda e: (self_chat_box_button.config(bg='#6F6135', fg='white'), self_chat_box_label.config(text='', bg='#121317')))

    # call calendar button creation and placement along with the commands and functions
    self_calendar_label = tk.Label(home_window, text='',
                                   bg='#121317',
                                   font=('Georgia', '12'),
                                   borderwidth=0)
    self_calendar_label.pack()
    self_calendar_label.place(x=70, y=350)

    def call_calendar():

        """
        when the client calls the call_calendar() function, the current home_window gets destroyed and
        the Calendar() object is called from the main_directory.Calendar__reg__utils__.py file
        and is run and the open_windows_list is appended with 'home'
        """

        open_windows_list.append('home')
        home_window.destroy()
        from main_directory.Calendar__reg__utils__ import Calendar
        chat_box = Calendar()
        chat_box.run()

    self_calendar_button = tk.Button(home_window, text='     \n       C       \n     ',
                                     bg='#6F6135',
                                     activeforeground='white',
                                     activebackground='#6D5406',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_calendar,
                                     font=('Georgia', '10'))
    self_calendar_button.pack()
    self_calendar_button.place(x=2, y=330)
    self_calendar_button.bind('<Enter>', func=lambda e: (self_calendar_button.config(bg='#C4B071', fg='black'), self_calendar_label.config(text='   Calendar   ', bg='#C4B071', fg='black')))
    self_calendar_button.bind('<Leave>', func=lambda e: (self_calendar_button.config(bg='#6F6135', fg='white'), self_calendar_label.config(text='', bg='#121317')))

    # ___________________________ submit button _______________________________
    #
    # vertical_line = tk.Label(home_window, text=' ',
    #                          bg='#8C52FF',
    #                          height=50,
    #                          width=100)
    # vertical_line.pack()
    # vertical_line.place(x=430, y=70)

    def call_banking(__name__, __card__):

        """
        when the client calls the call_banking() function, the current home_window gets destroyed and
        the Banking() object is called from the main_directory.banking_class.py file
        and is run
        """

        from main_directory.banking_class import Banking
        bank_connect = Banking(__name__, __card__)
        bank_connect.mainloop()

    def submit():

        """
        when the user clicks the submit button, the submit() function is called.
        the function requires both client's card number which is of 16 characters - all digits
        and the pin number which is of 4 characters - all digits

        once the card number is taken, the app connects to the mysql database where it is checked
        if the card number entered by the user actually exists or not

        then the function check is the card_in_use_permission is enabled or not.
            -> if it is turned on, the client can use it
            -> if it is turned off, this means the card is blocked

            (special) if the value is 'None', this means the administrator has blocked the card
                      and the client cannot unblock the card on their own.

        then the pin entered is hashed to verify the authenticity of the client and if both the card number
        and the hashed pin value (sha512) is found in a record, the client is allowed to further continue
        with the banking procedures and will be led to the banking window in the Banking() object
        located in main_directory.banking_class.py

        the home window is destroyed
        """

        card_number = card_number_input.get()
        card_number = card_number.lstrip().rstrip()

        if len(card_number) != 16:
            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            elif 16 > len(card_number) > 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

            elif len(card_number) > 16:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

            elif len(card_number) == 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

        else:
            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            else:

                import mysql.connector as sql

                __connection__ = sql.connect(host='localhost',
                                             user='root',
                                             password='dpsbn',
                                             database='client_db')

                if __connection__.is_connected() is True:
                    __cur = __connection__.cursor()
                    __cur.execute(f"SELECT * FROM client WHERE CARD_NUMBER = '{card_number}'")
                    __result = __cur.fetchall()
                    __cur.close()

                    if len(__result) != 0:
                        check_cn.config(fg='black', text='', bg='#A6A6A6')

                        import mysql.connector as sql

                        connection__ = sql.connect(host='localhost',
                                                   user='root',
                                                   password='dpsbn',
                                                   database='client_db')

                        if connection__.is_connected() is True:
                            cur_ = connection__.cursor()
                            cur_.execute(f"SELECT CARD_NUMBER_IN_USE_PERMISSION FROM client WHERE CARD_NUMBER = '{card_number}'")
                            __result__ = cur_.fetchall()

                            if __result__[0][0] == 'False':
                                messagebox.showerror(title='Security', message='This card is blocked')

                            elif __result__[0][0] == 'None':
                                messagebox.showerror(title='Security', message='Your card is blocked by the administrator')

                            else:

                                if card_number.isdigit():

                                    if len(card_number) == 16:

                                        pin = pin_number_input.get()
                                        pin = pin.lstrip().rstrip()

                                        if pin.isdigit():

                                            if len(pin) == 4:

                                                __object__ = threading.Thread(target=loading, daemon=True)
                                                __object__.start()

                                                final_pin = hash_pin(pin)
                                                print(final_pin)
                                                import mysql.connector as sql

                                                connection = sql.connect(host='localhost',
                                                                         user='root',
                                                                         password='dpsbn',
                                                                         database='client_db')

                                                if connection.is_connected() is True:
                                                    cursor = connection.cursor()
                                                    cursor.execute(f"SELECT NAME, CARD_NUMBER FROM client WHERE CARD_NUMBER='{card_number}' AND PIN_NUMBER='{final_pin}'")
                                                    result_set = cursor.fetchall()
                                                    cursor.close()
                                                    if len(result_set) != 0:

                                                        check_pin.config(text='', fg='black', bg='#A6A6A6')

                                                        name = result_set[0][0]
                                                        card = result_set[0][1]

                                                        cur = connection.cursor()
                                                        cur.execute(f"SELECT ACCOUNT_IN_USE_PERMISSION FROM client WHERE CARD_NUMBER = '{card_number}'")
                                                        result__ = cur.fetchall()
                                                        cur.close()

                                                        __value__ = result__[0][0]
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
                                                                    new_conn.execute(f"SELECT NAME, EMAIL FROM client WHERE CARD_NUMBER = '{card_number}'")
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

                                                                    w_ = 470  # width for the Tk root
                                                                    h_ = 300  # height for the Tk root

                                                                    # get screen width and height
                                                                    ws_ = email_ver_win.winfo_screenwidth()  # width of the screen
                                                                    hs_ = email_ver_win.winfo_screenheight()  # height of the screen

                                                                    # calculate x and y coordinates for the Tk root window
                                                                    x_ = (ws_ / 2) - (w_ / 2)
                                                                    y_ = (hs_ / 2) - (h_ / 2)

                                                                    # set the dimensions of the screen
                                                                    # and where it is placed
                                                                    email_ver_win.geometry('%dx%d+%d+%d' % (w_, h_, x_, y_))
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
                                                                            home_window.destroy()
                                                                            email_ver_win.destroy()

                                                                            def notify_(title='DataSync Intl', message='You have logged in successfully!'):
                                                                                from plyer import notification
                                                                                notification.notify(title, message, timeout=5)

                                                                            obj_ = threading.Thread(target=notify_)
                                                                            obj_.start()

                                                                            call_banking(name, card)
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
                                                                home_window.destroy()
                                                                card_otp(name, card)
                                                        else:
                                                            home_window.destroy()

                                                            def notify(title='DataSync Intl', message='You have logged in successfully!'):
                                                                from plyer import notification
                                                                notification.notify(title, message, timeout=5)

                                                            obj = threading.Thread(target=notify)
                                                            obj.start()

                                                            call_banking(name, card)
                                                    else:
                                                        check_pin.config(text='incorrect pin', fg='red', bg='#A6A6A6')
                                                        messagebox.showerror(title='Database Error', message='No such data exists')
                                                else:
                                                    messagebox.showerror(title='Server Error', message='The server crashed')
                                            else:

                                                if 4 > len(pin) > 0:
                                                    messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number\nThe given pin number has less than 4 characters')

                                                elif len(pin) > 4:
                                                    messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number\nThe given pin number has more than 4 characters')

                                                elif len(pin) == 0:
                                                    messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number')

                                        else:
                                            messagebox.showerror(title='Pin number error', message='Enter a valid Pin Number')

                                    else:
                                        messagebox.showerror(title='Card number error', message='Enter a valid Card Number')

                                else:
                                    messagebox.showerror(title='Card number error', message='Enter a valid Card Number')
                        else:
                            messagebox.showerror(title='Server Error', message='The server crashed')
                    else:
                        check_cn.config(fg='red', text='invalid card number', bg='#A6A6A6')
                        messagebox.showerror(title='Card number error', message='Card Number not found')

    # # card number entry box creation and placement
    # card_number_label = tk.Label(home_window,
    #                              bg='#8C52FF',
    #                              fg='white',
    #                              text="Enter your card number ",
    #                              font=('Georgia', '14'))
    # card_number_label.pack()
    # card_number_label.place(x=500, y=150)

    card_number_input = ttk.Entry(home_window,
                                  width=31,
                                  font=('aerial', '12'))
    card_number_input.pack()
    card_number_input.place(x=435, y=220)

    card_number_input.focus_force()

    # ______________________ pin

    # # pin number entry box creation and placement
    # pin_number_label = tk.Label(home_window,
    #                             bg='#8C52FF',
    #                             fg='white',
    #                             text="Enter your PIN ",
    #                             font=('Georgia', '14'))
    # pin_number_label.pack()
    # pin_number_label.place(x=500, y=240)

    pin_number_input = ttk.Entry(home_window,
                                 show='*',
                                 width=31,
                                 font=('aerial', '12'))
    pin_number_input.pack()
    pin_number_input.place(x=435, y=416)

    def hide_pin():

        """
        hides the pin number when user wants it to
        """

        pin___label.config(command=show_pin, text=' ○ ')
        pin_number_input.configure(show='*')
        pass

    def show_pin():

        """
        shows the pin to the user when the user wants it to
        """

        pin___label.config(command=hide_pin, text=' — ')
        pin_number_input.configure(show='')
        pass

    pin___label = tk.Button(home_window,
                            text=' ○ ',
                            command=show_pin,
                            relief=tk.FLAT,
                            fg='white',
                            bg='#17171C',
                            activebackground='purple',
                            borderwidth=0)
    pin___label.pack()
    pin___label.place(x=697, y=417)

    check_cn = tk.Label(home_window,
                        text='',
                        bg='#A6A6A6',
                        fg='black',
                        borderwidth=0)
    check_cn.pack()
    check_cn.place(x=580, y=250)

    check_pin = tk.Label(home_window,
                         text='',
                         bg='#A6A6A6',
                         fg='black',
                         borderwidth=0)
    check_pin.pack()
    check_pin.place(x=640, y=445)

    # # submit button creation and placement along with the commands and functions
    submit_button = tk.Button(home_window, text='\n     Submit     \n',
                              bg='#6F6135',
                              activeforeground='black',
                              activebackground='#9e9e9e',
                              fg='white',
                              relief=tk.FLAT,
                              command=submit,
                              font=('Georgia', '10'))
    submit_button.pack()
    submit_button.place(x=535, y=500)
    submit_button.bind('<Enter>', func=lambda e: submit_button.config(bg='#81a343'))
    submit_button.bind('<Leave>', func=lambda e: submit_button.config(bg='#6F6135'))

    def go_to_next_textbox(*args):

        """
        goes to the next entry text field i.e. the pin number entry box when the return key is pressed
        """

        if len(card_number_input.get()) != 0:
            pin_number_input.focus_force()
        if len(card_number_input.get()) != 0 and len(pin_number_input.get()) != 0:
            submit()

    home_window.bind('<Return>', go_to_next_textbox)  # binding the 'return' key to the home_window

    def go_up(*args):
        card_number_input.focus_force()  # when the up-arrow key is pressed, the cursor jumps from pin entry box to card number entry box

    def go_down(*args):
        pin_number_input.focus_force()  # when the down-arrow key is pressed, the cursor jumps from card number entry box to pin entry box

    home_window.bind('<Up>', go_up)  # binding the up-arrow key to home_window
    home_window.bind('<Down>', go_down)  # binding the down-arrow key the home_window

    """ 
    creating the context (option) menu for the user when he/she does a right click
    class object -- OptionPaneHome
    right-mouse-button (<Button-3>) bound to home_window
    """

    class OptionsPaneHome:
        def __init__(self):

            """
            creating a context (option) menu when the user right clicks on any part of the home_window
            __init__ is used to initialise the class object named OptionPaneHome

            available options for the user:
                1. refresh
                2.chat box
                3. calendar
                4. exit

            if the context menu is left idle and unused, it will be destroyed after 5 seconds
            """

            super(OptionsPaneHome, self).__init__()

            self.options_home = tk.Tk()
            self.options_home.overrideredirect(True)
            self.options_home.config(bg='#1c1c1c')

            abs_coord_x = self.options_home.winfo_pointerx() - self.options_home.winfo_rootx()
            abs_coord_y = self.options_home.winfo_pointery() - self.options_home.winfo_rooty()
            self.options_home.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_home.geometry("100x118")

            # refresh button creation and placement along with the commands and methods
            opt_refresh_button = tk.Button(self.options_home,
                                           text='       Refresh       ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=self.refresh__,
                                           activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=0)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            # open chat box button creation and placement along with the commands and methods
            opt_chat_box_button = tk.Button(self.options_home,
                                            text='Open Chat Box  ',
                                            relief=tk.FLAT,
                                            font=('Georgia', '10'),
                                            bg='#1c1c1c',
                                            fg='white',
                                            command=self.cal_scb__,
                                            activebackground='#3d3d3d')
            opt_chat_box_button.pack()
            opt_chat_box_button.place(x=0, y=30)
            opt_chat_box_button.bind('<Enter>', func=lambda e: opt_chat_box_button.config(bg='#3d3d3d'))
            opt_chat_box_button.bind('<Leave>', func=lambda e: opt_chat_box_button.config(bg='#1c1c1c'))

            # open calendar button creation and placement along with the commands and methods
            opt_calendar_button = tk.Button(self.options_home,
                                            text='Open Calendar  ',
                                            relief=tk.FLAT,
                                            font=('Georgia', '10'),
                                            bg='#1c1c1c',
                                            fg='white',
                                            command=self.call_calendar__,
                                            activebackground='#3d3d3d')
            opt_calendar_button.pack()
            opt_calendar_button.place(x=0, y=60)
            opt_calendar_button.bind('<Enter>', func=lambda e: opt_calendar_button.config(bg='#3d3d3d'))
            opt_calendar_button.bind('<Leave>', func=lambda e: opt_calendar_button.config(bg='#1c1c1c'))

            # exit button creation and placement along with the commands and methods
            opt_exit_button = tk.Button(self.options_home,
                                        text='           Exit          ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.exit__,
                                        activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=90)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            # binding the left button and the right button to the home_window
            home_window.bind('<Button-1>', self.left_button_options__home)
            home_window.bind('<Button-3>', self.right_button_options__home)

            # destroying the context (option) menu if left idle and unused
            self.options_home.after(5000, lambda: self.options_home.destroy())

        def run(self):

            """
            running the class object OptionPaneHome using the <tkinter_window>.mainloop() method
            """

            self.options_home.mainloop()

        def cal_scb__(self):
            self.options_home.destroy()
            call_scb()

        def refresh__(self):
            self.options_home.destroy()
            refresh()

        def call_calendar__(self):
            self.options_home.destroy()
            call_calendar()

        def exit__(self):
            self.options_home.destroy()
            usr_exit_request()

        def left_button_options__home(self, *args):
            try:
                self.options_home.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_home.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

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

    home_window.bind('<Button-3>', right_button_options__home)  # binding the right button to the home_window

    def redirect_to_login_window_(*args):
        redirect_to_login_window()

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

    home_window.bind('<Control-l>', redirect_to_login_window_)
    home_window.bind('<Control-d>', redirect_to_delete_window_)
    home_window.bind('<Control-s>', redirect_to_signup_window_)
    home_window.bind('<Alt-c>', call_calendar_)
    home_window.bind('<Control-r>', refresh_)
    home_window.bind('<Control-t>', redirect_to_documentation_window_)
    home_window.bind('<Control-h>', call_scb_)
    home_window.bind('<Control-e>', exit_)

    # # creating display text for the left half of the screen
    # text = tk.Label(text='Welcome to \nDataSync Intl',
    #                 bg='#5E17EB',
    #                 fg='white',
    #                 font=('Courier New', 30))
    # text.pack()
    # text.place(x=90, y=120)

    info_label = tk.Label(home_window, text='',
                          bg='#616865',
                          font=('Georgia', '12'),
                          borderwidth=0)
    info_label.pack()
    info_label.place(x=70, y=155)

    def call_dsi_win_ver():
        if len(dsi_check) == 0:
            dsi_check.append(1)
            from main_directory.dsi_win_ver_launch import DSIWinVer
            window = DSIWinVer()
            window.run()
        pass

    info = tk.Button(home_window, text='     \n    info    \n     ',
                     bg='#6F6135',
                     activeforeground='white',
                     activebackground='#6D5406',
                     relief=tk.FLAT,
                     fg='white',
                     command=call_dsi_win_ver,
                     font=('Georgia', '10'))
    info.pack()
    info.place(x=2, y=140)
    info.bind('<Enter>', func=lambda e: (info.config(bg='#C4B071', fg='black'), info_label.config(text='   INFO    ', bg='#C4B071', fg='black')))
    info.bind('<Leave>', func=lambda e: (info.config(bg='#6F6135', fg='white'), info_label.config(text='', bg='#616865')))

    # finally, running the home_window (tkinter GUI) using <window_object>.mainloop()
    home_window.mainloop()


pass
