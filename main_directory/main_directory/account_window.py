import tkinter as tk
from main_directory.open_windows import open_windows_list
from main_directory.refresh_windows_functions_file import account_window_refresh_registry
from tkinter import messagebox
import threading
import sys
import datetime
import calendar

BG_BUTTON_COLOR = "#2f5873"
REMOTE_SERVER = "one.one.one.one"


def account_window(username, name):

    print('[ INFO ] Tkinter [ Tkinter     ] : account window loaded successfully')

    root = tk.Tk()
    root.title(f"{name.title()}'s Account")
    root.focus_force()
    root.config(bg='#66ffaf')
    root.resizable(False, False)
    try:
        root.iconbitmap(r'..\main_directory\ico1.ico')

        from PIL import ImageTk, Image
        image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic1.png"))

        img_lb = tk.Label(root, image=image1, borderwidth=0)
        img_lb.pack()
        img_lb.place(x=(-120), y=500)
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    # ______________fixing window on screen__________credit: stack_overflow

    w = 800  # width for the Tk root
    h = 600  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    # _________________fixing window on screen_END___________________________
    # _________________________design - start________________________________

    label3 = tk.Label(root, text='',
                      bg='#bddec9',
                      width=150,
                      height=150,
                      font=('Georgia', '20'))
    label3.pack()
    label3.place(x=450, y=63)

    label1 = tk.Label(root, text='',
                      bg='#127544',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    label2 = tk.Label(root, text='',
                      bg='#127544',
                      width=150,
                      height=2,
                      font=('Georgia', '20'))
    label2.pack()
    label2.place(x=0, y=0)

    label1 = tk.Label(root, text='',
                      bg='#739e90',
                      width=150,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=450, y=370)

    # _________________________design - end___________________________________

    def go_back():
        root.destroy()
        from LoginWindow import login
        login()

    go_back_button = tk.Button(root,
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

    def refresh():
        root.destroy()
        account_window_refresh_registry(username, name)

    refresh_label = tk.Label(text='',
                             bg='#66ffaf',
                             font=('Georgia', '12'))
    refresh_label.pack()
    refresh_label.place(x=70, y=95)

    refresh_button = tk.Button(root, text='     \n     ♻      \n     ',
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
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#127544', fg='white'), refresh_label.config(text='', bg='#66ffaf')))

    def return_home():
        root.destroy()
        open_windows_list.clear()
        from HomeWindow import home
        home()

    home_label = tk.Label(text='',
                          bg='#66ffaf',
                          font=('Georgia', '12'))
    home_label.pack()
    home_label.place(x=70, y=155)

    home_button = tk.Button(root, text='     \n  Home  \n     ',
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
    home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#127544', fg='white'), home_label.config(text='', bg='#66ffaf')))

    def usr_exit_request():
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            root.destroy()
            sys.exit()

    exit_button = tk.Button(root, text='     \n    Exit    \n     ',
                            bg='#127544',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            command=usr_exit_request,
                            relief=tk.FLAT,
                            font=('Georgia', '10'))
    exit_button.pack()
    exit_button.place(x=2, y=537)
    exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
    exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#127544'))

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            sys.exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    def change_password_func():
        root.destroy()
        from account_wn_change_password__reg__utils__ import ChangePassword
        app = ChangePassword(username, name)
        app.run()

    change_password_button = tk.Button(root, text='     \n  Change Password                                        \n     ',
                                       bg='#127544',
                                       activeforeground='white',
                                       activebackground='#3b785a',
                                       relief=tk.FLAT,
                                       fg='white',
                                       command=change_password_func,
                                       font=('Georgia', '10'))
    change_password_button.pack()
    change_password_button.place(x=150, y=100)
    change_password_button.bind('<Enter>', func=lambda e: change_password_button.config(bg='#d9cf91', fg='black'))
    change_password_button.bind('<Leave>', func=lambda e: change_password_button.config(bg='#127544', fg='white'))

    def change_pin_func():
        root.destroy()
        from account_wn_change_pin__reg__utils__ import ChangePin
        app = ChangePin(username, name)
        app.run()

    change_pin_button = tk.Button(root, text='     \n  Change Pin                                                     \n     ',
                                  bg='#127544',
                                  activeforeground='white',
                                  activebackground='#3b785a',
                                  relief=tk.FLAT,
                                  fg='white',
                                  command=change_pin_func,
                                  font=('Georgia', '10'))
    change_pin_button.pack()
    change_pin_button.place(x=150, y=200)
    change_pin_button.bind('<Enter>', func=lambda e: change_pin_button.config(bg='#d9cf91', fg='black'))
    change_pin_button.bind('<Leave>', func=lambda e: change_pin_button.config(bg='#127544', fg='white'))

    def change_phone_and_address():
        root.destroy()
        from account_wn_change_phone_and_address__reg__utils__ import ChangePhoneAndAddress
        app = ChangePhoneAndAddress(username, name)
        app.run()

    change_phone_and_address_button = tk.Button(root, text='     \n  Change Phone & Address                         \n     ',
                                                bg='#127544',
                                                activeforeground='white',
                                                activebackground='#3b785a',
                                                relief=tk.FLAT,
                                                fg='white',
                                                command=change_phone_and_address,
                                                font=('Georgia', '10'))
    change_phone_and_address_button.pack()
    change_phone_and_address_button.place(x=150, y=300)
    change_phone_and_address_button.bind('<Enter>', func=lambda e: change_phone_and_address_button.config(bg='#d9cf91', fg='black'))
    change_phone_and_address_button.bind('<Leave>', func=lambda e: change_phone_and_address_button.config(bg='#127544', fg='white'))

    def turn_off_2fa():
        response = messagebox.askokcancel(title='Security Alert', message="Turn off Two-Factor Authentication?")
        if response is True:
            import mysql.connector as mysql_

            connection_ = mysql_.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')
            if connection_.is_connected() is True:
                cur2 = connection_.cursor()
                cur2.execute(f"UPDATE client SET ACCOUNT_IN_USE_PERMISSION = 'False' WHERE USERNAME = '{username}'")
                cur2.close()
                connection_.commit()
                connection_.close()

                def notify(title='DataSync Intl', message='You have turned off Two-Factor Authentication!'):
                    from plyer import notification
                    notification.notify(title, message, timeout=5)

                obj = threading.Thread(target=notify)
                obj.start()

                refresh()

    def turn_on_2fa():
        response = messagebox.askokcancel(title='Security Alert', message="Turn on Two-Factor Authentication?")
        if response is True:
            import mysql.connector as mysql_

            connection_ = mysql_.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')
            if connection_.is_connected() is True:
                cur2 = connection_.cursor()
                cur2.execute(f"UPDATE client SET ACCOUNT_IN_USE_PERMISSION = 'True' WHERE USERNAME = '{username}'")
                cur2.close()
                connection_.commit()
                connection_.close()

                def notify(title='DataSync Intl', message='You have turned on Two-Factor Authentication successfully!'):
                    from plyer import notification
                    notification.notify(title, message, timeout=5)

                obj = threading.Thread(target=notify)
                obj.start()

                refresh()

    import mysql.connector as mysql

    connection = mysql.connect(host='localhost',
                               user='root',
                               password='dpsbn',
                               database='client_db')

    if connection.is_connected() is True:
        cur = connection.cursor()
        cur.execute(f"SELECT ACCOUNT_IN_USE_PERMISSION FROM client WHERE USERNAME = '{username}'")
        result = cur.fetchall()
        cur.close()
        __value__ = result[0][0]
        if __value__ == 'True':
            turn_off_otp_button = tk.Button(root, text='     \n  Turn Off Two-Factor Authentication \n     ',
                                            bg='#127544',
                                            activeforeground='white',
                                            activebackground='#3b785a',
                                            relief=tk.FLAT,
                                            fg='white',
                                            command=turn_off_2fa,
                                            font=('Georgia', '10'))
            turn_off_otp_button.pack()
            turn_off_otp_button.place(x=150, y=400)
            turn_off_otp_button.bind('<Enter>', func=lambda e: turn_off_otp_button.config(bg='#d9cf91', fg='black'))
            turn_off_otp_button.bind('<Leave>', func=lambda e: turn_off_otp_button.config(bg='#127544', fg='white'))
        else:
            turn_on_otp_button = tk.Button(root, text='     \n  Turn On Two-Factor Authentication  \n     ',
                                           bg='#127544',
                                           activeforeground='white',
                                           activebackground='#3b785a',
                                           relief=tk.FLAT,
                                           fg='white',
                                           command=turn_on_2fa,
                                           font=('Georgia', '10'))
            turn_on_otp_button.pack()
            turn_on_otp_button.place(x=150, y=400)
            turn_on_otp_button.bind('<Enter>', func=lambda e: turn_on_otp_button.config(bg='#d9cf91', fg='black'))
            turn_on_otp_button.bind('<Leave>', func=lambda e: turn_on_otp_button.config(bg='#127544', fg='white'))
    else:
        messagebox.showerror(title='Server Error', message='The server crashed')

    # _____________________________ block unblock card ________________________________________

    def block_card():
        response = messagebox.askokcancel(title='Security Alert', message='Block your card?')
        if response is True:
            import mysql.connector as mysql_

            connection_ = mysql_.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')
            if connection_.is_connected() is True:
                cur3 = connection_.cursor()
                cur3.execute(f"UPDATE client SET CARD_NUMBER_IN_USE_PERMISSION = 'False' WHERE USERNAME = '{username}'")
                cur3.close()
                connection_.commit()
                connection_.close()

                def notify(title='DataSync Intl', message='You have blocked your card!'):
                    from plyer import notification
                    notification.notify(title, message, timeout=5)

                obj = threading.Thread(target=notify)
                obj.start()

                refresh()

    def unblock_card():
        response = messagebox.askokcancel(title='Security Alert', message='Unblock your card?')
        if response is True:
            import mysql.connector as mysql_

            connection_ = mysql_.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')
            if connection_.is_connected() is True:
                cur3 = connection_.cursor()
                cur3.execute(f"UPDATE client SET CARD_NUMBER_IN_USE_PERMISSION = 'True' WHERE USERNAME = '{username}'")
                cur3.close()
                connection_.commit()
                connection_.close()

                def notify(title='DataSync Intl', message='You have unblocked your card!'):
                    from plyer import notification
                    notification.notify(title, message, timeout=5)

                obj = threading.Thread(target=notify)
                obj.start()

                refresh()

    if connection.is_connected() is True:

        cur_ = connection.cursor()
        cur_.execute(f"SELECT CARD_NUMBER_IN_USE_PERMISSION FROM client WHERE USERNAME = '{username}'")
        result_ = cur_.fetchall()
        cur_.close()
        ___value___ = result_[0][0]
        if ___value___ == 'True':
            block_card_button = tk.Button(root, text='     \n  Block Card                                                      \n     ',
                                          bg='#127544',
                                          activeforeground='white',
                                          activebackground='#3b785a',
                                          relief=tk.FLAT,
                                          fg='white',
                                          command=block_card,
                                          font=('Georgia', '10'))
            block_card_button.pack()
            block_card_button.place(x=150, y=500)
            block_card_button.bind('<Enter>', func=lambda e: block_card_button.config(bg='#d9cf91', fg='black'))
            block_card_button.bind('<Leave>', func=lambda e: block_card_button.config(bg='#127544', fg='white'))
        elif ___value___ == 'False':
            unblock_card_button = tk.Button(root, text='     \n  Unblock Card                                                \n     ',
                                            bg='#127544',
                                            activeforeground='white',
                                            activebackground='#3b785a',
                                            relief=tk.FLAT,
                                            fg='white',
                                            command=unblock_card,
                                            font=('Georgia', '10'))
            unblock_card_button.pack()
            unblock_card_button.place(x=150, y=500)
            unblock_card_button.bind('<Enter>', func=lambda e: unblock_card_button.config(bg='#d9cf91', fg='black'))
            unblock_card_button.bind('<Leave>', func=lambda e: unblock_card_button.config(bg='#127544', fg='white'))

        else:
            messagebox.showerror(title='Security Alert', message='Your card is blocked by the administrator')
    else:
        messagebox.showerror(title='Server Error', message='The server crashed')

    class OptionPane:
        def __init__(self):
            super(OptionPane, self).__init__()
            self.options_pane = tk.Tk()
            self.options_pane.overrideredirect(True)
            self.options_pane.config(bg='#1c1c1c')

            abs_coord_x = self.options_pane.winfo_pointerx() - self.options_pane.winfo_rootx()
            abs_coord_y = self.options_pane.winfo_pointery() - self.options_pane.winfo_rooty()
            self.options_pane.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_pane.geometry("100x118")

            opt_back_button = tk.Button(self.options_pane,
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

            opt_refresh_button = tk.Button(self.options_pane,
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

            opt_home_button = tk.Button(self.options_pane,
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

            opt_exit_button = tk.Button(self.options_pane,
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

            root.bind('<Button-1>', self.left_button_options__home)
            root.bind('<Button-3>', self.right_button_options__home)

            self.options_pane.after(5000, lambda: self.options_pane.destroy())

        def run(self):
            self.options_pane.mainloop()

        def refresh__(self):
            self.options_pane.destroy()
            refresh()

        def return_home__(self):
            self.options_pane.destroy()
            return_home()

        def exit__(self):
            self.options_pane.destroy()
            usr_exit_request()

        def __go_back__(self):
            self.options_pane.destroy()
            go_back()

        def left_button_options__home(self, *args):
            try:
                self.options_pane.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_pane.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

    def relaunch_options_pane():
        options_pane = OptionPane()
        options_pane.run()

    def right_button_options__home(*args):
        options_pane = OptionPane()
        options_pane.run()

    root.bind('<Button-3>', right_button_options__home)

    def back_fn(*args):
        go_back()

    def refresh_fn(*args):
        refresh()

    def return_home_fn(*args):
        return_home()

    def exit_fn(*args):
        on_closing()

    root.bind('<Control-b>', back_fn)
    root.bind('<Control-r>', refresh_fn)
    root.bind('<Alt-h>', return_home_fn)
    root.bind('<Control-e>', exit_fn)

    class Calendar:
        def __init__(self):

            super(Calendar, self).__init__()

            date = datetime.date.today()
            self.__today__ = datetime.datetime.strptime(str(date), '%Y-%m-%d')
            self.__month__ = self.__today__.month
            self.__year__ = self.__today__.year
            self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))

            self.label = tk.Label(root, text=self.__month_calendar__, bg='#bddec9', font=('Courier New', '15'), anchor='w', justify='left')
            self.label.pack()
            self.label.place(x=500, y=100)

            __date__ = datetime.datetime.now()
            date_in_words = __date__.strftime('%A %d %B %Y')

            self.date_ = tk.Label(root, text=('Today: ' + str(date_in_words)), font=('Georgia', '12'), bg='#bddec9', fg='black')
            self.date_.pack()
            self.date_.place(x=500, y=280)

            self.NEXT_BTN = tk.Button(root, text=' > ', command=self.next_function, bg='#bddec9', activebackground='#bab197', relief=tk.FLAT)
            self.NEXT_BTN.pack()
            self.NEXT_BTN.place(x=740, y=320)
            self.NEXT_BTN.bind('<Enter>', func=lambda e: self.NEXT_BTN.configure(bg='#baaa7f'))
            self.NEXT_BTN.bind('<Leave>', func=lambda e: self.NEXT_BTN.configure(bg='#bddec9'))

            self.PREV_BTN2 = tk.Button(root, text=' < ', command=self.prev_function, bg='#bddec9', activebackground='#bab197', relief=tk.FLAT)
            self.PREV_BTN2.pack()
            self.PREV_BTN2.place(x=500, y=320)
            self.PREV_BTN2.bind('<Enter>', func=lambda e: self.PREV_BTN2.configure(bg='#baaa7f'))
            self.PREV_BTN2.bind('<Leave>', func=lambda e: self.PREV_BTN2.configure(bg='#bddec9'))

            self.TODAY_CALENDAR = tk.Button(root, text=' Today ', relief=tk.FLAT, bg='#bddec9', font=('Calibre', '10'), command=self.get_today_function, activebackground='#bab197')
            self.TODAY_CALENDAR.pack()
            self.TODAY_CALENDAR.place(x=605, y=320)
            self.TODAY_CALENDAR.bind('<Enter>', func=lambda e: self.TODAY_CALENDAR.configure(bg='#baaa7f'))
            self.TODAY_CALENDAR.bind('<Leave>', func=lambda e: self.TODAY_CALENDAR.configure(bg='#bddec9'))

            def prev_fn(*args):
                self.prev_function()

            def next_fn(*args):
                self.next_function()

            def today_fn(*args):
                self.get_today_function()

            root.bind('<Left>', prev_fn)
            root.bind('<Right>', next_fn)
            root.bind('<Control-t>', today_fn)

        def next_function(self):

            self.__month__ = self.__month__ + 1

            if self.__month__ == 13:
                self.__month__ = 1
                self.__year__ += 1
                self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))
                self.label.configure(text=self.__month_calendar__)
            else:
                self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))
                self.label.configure(text=self.__month_calendar__)

        def prev_function(self):

            self.__month__ = self.__month__ - 1

            if self.__month__ == 0:
                self.__month__ = 12
                self.__year__ -= 1
                self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))
                self.label.configure(text=self.__month_calendar__)

            else:
                self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))
                self.label.configure(text=self.__month_calendar__)

        def get_today_function(self):
            date = datetime.date.today()

            self.__today__ = datetime.datetime.strptime(str(date), '%Y-%m-%d')
            self.__month__ = self.__today__.month
            self.__year__ = self.__today__.year
            self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))

            self.label.configure(text=self.__month_calendar__)

    Calendar()

    class ChatBox:

        def __init__(self):
            super(ChatBox, self).__init__()

            self.TEXT_BOX = tk.Text(root,
                                    width=20,
                                    height=8,
                                    bg='#ebebeb',
                                    wrap=tk.WORD,
                                    font=('Georgia', '12'))
            self.TEXT_BOX.pack()
            self.TEXT_BOX.place(x=500, y=400)
            self.TEXT_BOX.configure(state=tk.DISABLED)

            self.TEXT_BOX.configure(state=tk.NORMAL)
            self.TEXT_BOX.insert(tk.END, 'How may I help you?\n\n')
            self.TEXT_BOX.configure(state=tk.DISABLED)

            self.SCROLL_BAR = tk.Scrollbar(self.TEXT_BOX)
            self.SCROLL_BAR.pack()
            self.SCROLL_BAR.place(relheight=1, relx=0.97)

            self.ENTRY_BOX = tk.Entry(root,
                                      width=20,
                                      bg='#ebebeb',
                                      font=('Georgia', '13'))
            self.ENTRY_BOX.pack()
            self.ENTRY_BOX.place(x=500, y=560)
            self.ENTRY_BOX.focus_force()

            self.SEND_QUERY_BUTTON = tk.Button(root, text='Send Query',
                                               bg=BG_BUTTON_COLOR,
                                               activeforeground='white',
                                               activebackground='#787373',
                                               relief=tk.FLAT,
                                               fg='white',
                                               command=self.get_text,
                                               font=('Georgia', '8'))
            self.SEND_QUERY_BUTTON.pack()
            self.SEND_QUERY_BUTTON.place(x=710, y=560)
            self.SEND_QUERY_BUTTON.bind('<Enter>', func=lambda e: (self.SEND_QUERY_BUTTON.config(bg='#57bdba', fg='black')))
            self.SEND_QUERY_BUTTON.bind('<Leave>', func=lambda e: (self.SEND_QUERY_BUTTON.config(bg=BG_BUTTON_COLOR, fg='white')))

            self.CLEAR_MSG_BUTTON = tk.Button(root, text='      Clear      ',
                                              bg=BG_BUTTON_COLOR,
                                              activeforeground='white',
                                              activebackground='#787373',
                                              relief=tk.FLAT,
                                              fg='white',
                                              command=self.clear_text,
                                              font=('Georgia', '8'))
            self.CLEAR_MSG_BUTTON.pack()
            self.CLEAR_MSG_BUTTON.place(x=710, y=500)
            self.CLEAR_MSG_BUTTON.bind('<Enter>', func=lambda e: (self.CLEAR_MSG_BUTTON.config(text='      Clear      ', bg='#57bdba', fg='black')))
            self.CLEAR_MSG_BUTTON.bind('<Leave>', func=lambda e: (self.CLEAR_MSG_BUTTON.config(text='      Clear      ', bg=BG_BUTTON_COLOR, fg='white')))

            def delete_text(*args):
                self.clear_text()

            root.bind('<Delete>', delete_text)

            def get__text__(*args):
                self.get_text()

            root.bind('<Return>', get__text__)

            self.CLEAR_CHAT_BUTTON = tk.Button(root, text=' Clear Chat ',
                                               bg=BG_BUTTON_COLOR,
                                               activeforeground='white',
                                               activebackground='#787373',
                                               relief=tk.FLAT,
                                               fg='white',
                                               command=self.clear_chat,
                                               font=('Georgia', '8'))
            self.CLEAR_CHAT_BUTTON.pack()
            self.CLEAR_CHAT_BUTTON.place(x=710, y=450)
            self.CLEAR_CHAT_BUTTON.bind('<Enter>', func=lambda e: (self.CLEAR_CHAT_BUTTON.config(text=' Clear Chat ', bg='#57bdba', fg='black')))
            self.CLEAR_CHAT_BUTTON.bind('<Leave>', func=lambda e: (self.CLEAR_CHAT_BUTTON.config(text=' Clear Chat ', bg=BG_BUTTON_COLOR, fg='white')))

        def get_text(self):

            from multi_char_chat_tokens import tokens
            import random

            text = self.ENTRY_BOX.get()
            text = text.lower().lstrip().rstrip()
            if len(text) <= 1:
                query_text = "** Please enter a valid query\n"
                self.TEXT_BOX.configure(state=tk.NORMAL)
                self.TEXT_BOX.insert(tk.END, query_text)
                self.TEXT_BOX.configure(state=tk.DISABLED)
                self.TEXT_BOX.see(tk.END)

            else:
                self.TEXT_BOX.tag_config('__query__', background='#bcdce6')
                self.ENTRY_BOX.delete(0, tk.END)

                msg1 = f"You: {text.capitalize()}\n\n"

                self.TEXT_BOX.configure(state=tk.NORMAL)
                self.TEXT_BOX.insert(tk.END, msg1, '__query__')
                self.TEXT_BOX.configure(state=tk.DISABLED)

                original_text = text

                text = text.lower()
                trim = [char for char in text if char.isalpha() or char.isdigit() or char.isspace()]
                trim = ''.join(trim)

                split_words = trim.split()

                if len(split_words) == 1:

                    check = []
                    check.clear()

                    from main_directory.single_char_chat_tokens import single_tokens

                    for i in split_words:
                        for k, v in single_tokens.items():
                            if i in k:
                                check.append(1)
                                response = random.choice(v)
                                self.insert_query(response)

                    if len(check) == 0:
                        self.insert_query("I don't understand that. I'm learning you see")

                else:

                    messages = []
                    messages.clear()

                    check = []
                    check.clear()

                    res_len = []
                    res_len.clear()

                    for i in split_words:
                        for key, value in tokens.items():
                            if i not in messages:
                                if i in key:
                                    for j in key:
                                        messages.append(j)

                                    check.append(1)
                                    res_len.append(1)
                                    if len(res_len) >= 1:
                                        response = random.choice(value)
                                        self.insert_query(response)

                    trim2 = [char for char in original_text if char.isalpha() or char.isdigit()]
                    trim2 = ''.join(trim2)

                    for key_, values_ in tokens.items():
                        for i in key_:
                            if i not in messages:
                                if i in trim2:
                                    for j in key_:
                                        messages.append(j)
                                    check.append(1)
                                    res_len.append(1)
                                    if len(res_len) >= 1:
                                        response = random.choice(values_)
                                        self.insert_query(response)

                    if len(check) == 0:
                        self.insert_query("I don't understand that. I'm learning you see")

        def insert_query(self, reply):
            self.TEXT_BOX.tag_config('__reply__', background='#e0b9b6')
            self.ENTRY_BOX.delete(0, tk.END)

            reply_ = f"Bob: {reply}\n\n"
            self.TEXT_BOX.configure(state=tk.NORMAL)
            self.TEXT_BOX.insert(tk.END, reply_, '__reply__')
            self.TEXT_BOX.configure(state=tk.DISABLED)

            self.TEXT_BOX.see(tk.END)

        def clear_text(self):
            self.ENTRY_BOX.delete(0, tk.END)

        def clear_chat(self):
            self.TEXT_BOX.configure(state=tk.NORMAL)
            self.TEXT_BOX.delete(1.0, tk.END)
            self.TEXT_BOX.insert(tk.END, 'How may I help you?\n\n')
            self.TEXT_BOX.configure(state=tk.DISABLED)

    ChatBox()

    heading = tk.Label(root, text='Your Account',
                       bg='#127544',
                       fg='white',
                       font=('Georgia', '30'))
    heading.pack()
    heading.place(x=500, y=5)
    # mode
    mode = tk.Label(root, text='', bg='#127544', font=('Helvetica', '10'))
    mode.pack()
    mode.place(x=440, y=28)

    def mode_function():
        from connection import is_connected as connection_

        check_connection = connection_(REMOTE_SERVER)

        if check_connection is True:
            mode.config(fg='#34eb43', text='ONLINE')
            mode.after(5000, mode_function)
        else:
            mode.config(fg='#ff0000', text='OFFLINE')
            mode.after(5000, mode_function)

    threading.Thread(target=mode_function, daemon=True).start()

    root.mainloop()
