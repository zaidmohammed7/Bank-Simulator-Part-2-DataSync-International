import threading
import tkinter as tk
# import tkinter.ttk as ttk
from tkinter import messagebox
from main_directory.open_windows import open_windows_list
from main_directory.refresh_windows_functions_file import banking_wn_refresh_registry

currency_run = []
REMOTE_SERVER = "one.one.one.one"


class Banking(tk.Tk):

    def __init__(self, name, card):

        self.name = name
        self.card = card
        super().__init__()

        self.title(f'{name.title()}\'s Banking Window')
        self.focus_force()
        self.config(bg='#FF9D94')
        self.resizable(False, False)
        try:
            self.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic11.png"))

            self.img_lb = tk.Label(self, image=self.image1, borderwidth=0)
            self.img_lb.pack()
            self.img_lb.place(x=0, y=500)
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        # ___________________fixing window on screen_START_______credit: stack_overflow

        w = 800  # width for the Tk root
        h = 600  # height for the Tk root

        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        y = y - 30

        # set the dimensions of the screen
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # home_window.geometry('800x600')

        # _________________fixing window on screen_END___________________________

        import mysql.connector as sql

        connection = sql.connect(host='localhost',
                                 user='root',
                                 password='dpsbn',
                                 database='client_db')

        if connection.is_connected() is True:
            cur = connection.cursor()
            cur.execute(f"SELECT NAME, EMAIL, USERNAME, PHONE, CARD_NUMBER FROM client WHERE CARD_NUMBER='{card}'")
            user_details = cur.fetchall()
            name = user_details[0][0]
            email = user_details[0][1]
            username = user_details[0][2]
            phone = user_details[0][3]
            card_number = user_details[0][4]

            self.details_label = tk.Label(self,
                                          bg='#FF9D94',
                                          text=f"NAME: {name}\n\nEMAIL: {email}\nUSERNAME: {username}\nPHONE: {phone}\n\nCARD NUMBER: {card_number}",
                                          font=('Courier New', '14'),
                                          fg='black',
                                          anchor='w',
                                          justify='left')
            self.details_label.pack()
            self.details_label.place(x=150, y=200)

            pass
        else:
            messagebox.showerror(title='Server Error', message='The server crashed')

        # _________________________design - start________________________________

        label1 = tk.Label(self, text='',
                          bg='#4e4d73',
                          width=6,
                          height=50,
                          font=('Georgia', '13'))
        label1.pack()
        label1.place(x=0, y=70)

        label2 = tk.Label(self, text='',
                          bg='#4e4d73',
                          width=150,
                          height=2,
                          font=('Georgia', '20'))
        label2.pack()
        label2.place(x=0, y=0)

        heading = tk.Label(self, text='Banking',
                           bg='#4e4d73',
                           fg='white',
                           font=('Georgia', '30'))
        heading.pack()
        heading.place(x=530, y=5)

        # mode
        mode = tk.Label(self, text='', bg='#4e4d73', font=('Helvetica', '10'))
        mode.pack()
        mode.place(x=450, y=0)

        def mode_function():
            from connection import is_connected as connection_

            check_connection = connection_(REMOTE_SERVER)

            if check_connection is True:
                mode.config(fg='#34eb43', text='ONLINE')
                mode.after(5000, mode_function)
            else:
                mode.config(fg='#dea9a9', text='OFFLINE')
                mode.after(5000, mode_function)

        threading.Thread(target=mode_function, daemon=True).start()

        # _________________________design - end___________________________________

        self.DEPOSIT_BUTTON = tk.Button(self,
                                        text='        Deposit         ',
                                        bg='#4e4d73',
                                        activeforeground='white',
                                        activebackground='#545454',
                                        fg='white',
                                        relief=tk.FLAT,
                                        command=self.go_to_deposit_window,
                                        font=('Georgia', '10'))
        self.DEPOSIT_BUTTON.pack()
        self.DEPOSIT_BUTTON.place(x=64, y=20)
        self.DEPOSIT_BUTTON.bind('<Enter>', func=lambda e: self.DEPOSIT_BUTTON.config(bg='#FF9D94', fg='black'))
        self.DEPOSIT_BUTTON.bind('<Leave>', func=lambda e: self.DEPOSIT_BUTTON.config(bg='#4e4d73', fg='white'))

        self.WITHDRAW_BUTTON = tk.Button(self,
                                         text='        Withdraw         ',
                                         bg='#4e4d73',
                                         activeforeground='white',
                                         activebackground='#545454',
                                         fg='white',
                                         relief=tk.FLAT,
                                         command=self.go_to_withdraw_window,
                                         font=('Georgia', '10'))
        self.WITHDRAW_BUTTON.pack()
        self.WITHDRAW_BUTTON.place(x=182, y=20)
        self.WITHDRAW_BUTTON.bind('<Enter>', func=lambda e: self.WITHDRAW_BUTTON.config(bg='#FF9D94', fg='black'))
        self.WITHDRAW_BUTTON.bind('<Leave>', func=lambda e: self.WITHDRAW_BUTTON.config(bg='#4e4d73', fg='white'))

        self.TRANSFER_BUTTON = tk.Button(self,
                                         text='        Transfer         ',
                                         bg='#4e4d73',
                                         activeforeground='white',
                                         activebackground='#545454',
                                         fg='white',
                                         relief=tk.FLAT,
                                         command=self.go_to_transfer_window,
                                         font=('Georgia', '10'))
        self.TRANSFER_BUTTON.pack()
        self.TRANSFER_BUTTON.place(x=314, y=20)
        self.TRANSFER_BUTTON.bind('<Enter>', func=lambda e: self.TRANSFER_BUTTON.config(bg='#FF9D94', fg='black'))
        self.TRANSFER_BUTTON.bind('<Leave>', func=lambda e: self.TRANSFER_BUTTON.config(bg='#4e4d73', fg='white'))

        def go_back():
            self.destroy()
            from main_directory.HomeWindow import home
            home()

        self.GO_BACK_BUTTON = tk.Button(self,
                                        text="  Back  ",
                                        bg='#4e4d73',
                                        relief=tk.FLAT,
                                        activeforeground='white',
                                        activebackground='#787373',
                                        fg='white',
                                        command=go_back,
                                        font=('Georgia', '10'))
        self.GO_BACK_BUTTON.pack()
        self.GO_BACK_BUTTON.place(x=5, y=20)
        self.GO_BACK_BUTTON.bind('<Enter>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#FF9D94', fg='black'))
        self.GO_BACK_BUTTON.bind('<Leave>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#4e4d73', fg='white'))

        def refresh():
            self.destroy()
            banking_wn_refresh_registry(name, card)

        self.REFRESH_LABEL = tk.Label(self, text='',
                                      bg='#FF9D94',
                                      font=('Georgia', '12'))
        self.REFRESH_LABEL.pack()
        self.REFRESH_LABEL.place(x=70, y=95)

        self.REFRESH_BUTTON = tk.Button(self, text='     \n     ♻      \n     ',
                                        bg='#4e4d73',
                                        activeforeground='white',
                                        activebackground='#787373',
                                        relief=tk.FLAT,
                                        fg='white',
                                        command=refresh,
                                        font=('Georgia', '10'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=2, y=75)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#FF9D94', fg='black'), self.REFRESH_LABEL.config(text='   Refresh    ', bg='#4e4d73', fg='white')))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#4e4d73', fg='white'), self.REFRESH_LABEL.config(text='', bg='#FF9D94')))

        def return_home():
            open_windows_list.clear()
            self.destroy()

            from main_directory.HomeWindow import home
            home()

        self.HOME_LABEL = tk.Label(self, text='',
                                   bg='#FF9D94',
                                   font=('Georgia', '12'))
        self.HOME_LABEL.pack()
        self.HOME_LABEL.place(x=70, y=155)

        self.HOME_BUTTON = tk.Button(self, text='     \n  Home  \n     ',
                                     bg='#4e4d73',
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=return_home,
                                     font=('Georgia', '10'))
        self.HOME_BUTTON.pack()
        self.HOME_BUTTON.place(x=2, y=140)
        self.HOME_BUTTON.bind('<Enter>', func=lambda e: (self.HOME_BUTTON.config(bg='#FF9D94', fg='black'), self.HOME_LABEL.config(text='   Home    ', bg='#4e4d73', fg='white')))
        self.HOME_BUTTON.bind('<Leave>', func=lambda e: (self.HOME_BUTTON.config(bg='#4e4d73', fg='white'), self.HOME_LABEL.config(text='', bg='#FF9D94')))

        self.CURRENCY_CONV_LABEL = tk.Label(self, text='',
                                            bg='#FF9D94',
                                            font=('Georgia', '12'))
        self.CURRENCY_CONV_LABEL.pack()
        self.CURRENCY_CONV_LABEL.place(x=70, y=210)

        def open_cc():
            if len(currency_run) == 0:
                currency_run.append(1)

                from main_directory.CurrencyConverter__reg__utils__ import CurrencyConverter
                app = CurrencyConverter()
                app.run()

        self.CURRENCY_CONV_BUTTON = tk.Button(self, text='     \n      CC     \n     ',
                                              bg='#4e4d73',
                                              activeforeground='white',
                                              activebackground='#787373',
                                              relief=tk.FLAT,
                                              fg='white',
                                              command=open_cc,
                                              font=('Georgia', '10'))
        self.CURRENCY_CONV_BUTTON.pack()
        self.CURRENCY_CONV_BUTTON.place(x=2, y=200)
        self.CURRENCY_CONV_BUTTON.bind('<Enter>', func=lambda e: (self.CURRENCY_CONV_BUTTON.config(bg='#FF9D94', fg='black'), self.CURRENCY_CONV_LABEL.config(text='   Currency Converter    ', bg='#4e4d73', fg='white')))
        self.CURRENCY_CONV_BUTTON.bind('<Leave>', func=lambda e: (self.CURRENCY_CONV_BUTTON.config(bg='#4e4d73', fg='white'), self.CURRENCY_CONV_LABEL.config(text='', bg='#FF9D94')))

        self_calendar_label = tk.Label(self, text='',
                                       bg='#FF9D94',
                                       font=('Georgia', '12'))
        self_calendar_label.pack()
        self_calendar_label.place(x=70, y=350)

        def call_calendar():
            self.destroy()
            from main_directory.Banking_Calendar__reg__sub__utils__ import BankingCalendar
            chat_box = BankingCalendar(self.name, self.card)
            chat_box.run()

        self_calendar_button = tk.Button(self, text='     \n       C       \n     ',
                                         bg='#4e4d73',
                                         activeforeground='white',
                                         activebackground='#787373',
                                         relief=tk.FLAT,
                                         fg='white',
                                         command=call_calendar,
                                         font=('Georgia', '10'))
        self_calendar_button.pack()
        self_calendar_button.place(x=2, y=330)
        self_calendar_button.bind('<Enter>', func=lambda e: (self_calendar_button.config(bg='#FF9D94', fg='black'), self_calendar_label.config(text='   Calendar   ', bg='#4e4d73', fg='white')))
        self_calendar_button.bind('<Leave>', func=lambda e: (self_calendar_button.config(bg='#4e4d73', fg='white'), self_calendar_label.config(text='', bg='#FF9D94')))

        self_chat_box_label = tk.Label(self, text='',
                                       bg='#FF9D94',
                                       font=('Georgia', '12'))
        self_chat_box_label.pack()
        self_chat_box_label.place(x=70, y=420)

        def call_scb():
            self.destroy()
            from main_directory.Banking_ChatBox__reg__sub__utils__ import BankingChatApplicationWn
            chat_box = BankingChatApplicationWn(self.name, self.card)
            chat_box.run()

        self_chat_box_button = tk.Button(self, text='     \n    Chat   \n     ',
                                         bg='#4e4d73',
                                         activeforeground='white',
                                         activebackground='#787373',
                                         relief=tk.FLAT,
                                         fg='white',
                                         command=call_scb,
                                         font=('Georgia', '10'))
        self_chat_box_button.pack()
        self_chat_box_button.place(x=2, y=400)
        self_chat_box_button.bind('<Enter>', func=lambda e: (self_chat_box_button.config(bg='#FF9D94', fg='black'), self_chat_box_label.config(text='   Chat Bot   ', bg='#4e4d73', fg='white')))
        self_chat_box_button.bind('<Leave>', func=lambda e: (self_chat_box_button.config(bg='#4e4d73', fg='white'), self_chat_box_label.config(text='', bg='#FF9D94')))

        exit_button = tk.Button(self, text='     \n    Exit    \n     ',
                                bg='#4e4d73',
                                activeforeground='white',
                                activebackground='maroon',
                                fg='white',
                                command=self.usr_exit_request,
                                relief=tk.FLAT,
                                font=('Georgia', '10'))
        exit_button.pack()
        exit_button.place(x=2, y=537)
        exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
        exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#4e4d73'))

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.destroy()
                import sys
                sys.exit()

        self.protocol("WM_DELETE_WINDOW", on_closing)

        def right_button_press(*args):
            start_option_menu()

        def start_option_menu(*args):
            root = tk.Tk()

            abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
            abs_coord_y = root.winfo_pointery() - root.winfo_rooty()

            root.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root.geometry("100x208")

            root.overrideredirect(True)
            root.config(bg='#1c1c1c')

            def __go_back__():
                self.destroy()
                root.destroy()
                from HomeWindow import home
                home()

            def refresh__():
                self.destroy()
                root.destroy()
                banking_wn_refresh_registry(name, card)

            def return_home__():
                open_windows_list.clear()
                self.destroy()
                root.destroy()

                from HomeWindow import home
                home()

            opt_back_button = tk.Button(root, text='         Back           ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=__go_back__, activebackground='#3d3d3d')
            opt_back_button.pack()
            opt_back_button.place(x=0, y=0)
            opt_back_button.bind('<Enter>', func=lambda e: opt_back_button.config(bg='#3d3d3d'))
            opt_back_button.bind('<Leave>', func=lambda e: opt_back_button.config(bg='#1c1c1c'))

            opt_refresh_button = tk.Button(root, text='       Refresh       ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=refresh__, activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=30)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_home_button = tk.Button(root, text=' Return Home     ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=return_home__, activebackground='#3d3d3d')
            opt_home_button.pack()
            opt_home_button.place(x=0, y=60)
            opt_home_button.bind('<Enter>', func=lambda e: opt_home_button.config(bg='#3d3d3d'))
            opt_home_button.bind('<Leave>', func=lambda e: opt_home_button.config(bg='#1c1c1c'))

            def exit__():
                response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
                if response is True:
                    import sys
                    sys.exit()

            def deposit__():
                self.destroy()
                root.destroy()
                from main_directory.Deposit__reg__utils__ import Deposit
                dep_wn = Deposit(self.name, self.card)
                dep_wn.mainloop()

            opt_deposit_button = tk.Button(root, text='      Deposit        ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=deposit__, activebackground='#3d3d3d')
            opt_deposit_button.pack()
            opt_deposit_button.place(x=0, y=90)
            opt_deposit_button.bind('<Enter>', func=lambda e: opt_deposit_button.config(bg='#3d3d3d'))
            opt_deposit_button.bind('<Leave>', func=lambda e: opt_deposit_button.config(bg='#1c1c1c'))

            def transfer__():
                self.destroy()
                root.destroy()
                from main_directory.Transfer__reg__utils__ import TransferWn
                dep_wn = TransferWn(self.name, self.card)
                dep_wn.run()

            opt_transfer_button = tk.Button(root, text='      Transfer        ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=transfer__, activebackground='#3d3d3d')
            opt_transfer_button.pack()
            opt_transfer_button.place(x=0, y=120)
            opt_transfer_button.bind('<Enter>', func=lambda e: opt_transfer_button.config(bg='#3d3d3d'))
            opt_transfer_button.bind('<Leave>', func=lambda e: opt_transfer_button.config(bg='#1c1c1c'))

            def withdraw__():
                self.destroy()
                root.destroy()
                from main_directory.Withdraw__reg__utils__ import WithdrawWn
                dep_wn = WithdrawWn(self.name, self.card)
                dep_wn.run()

            opt_withdraw_button = tk.Button(root, text='     Withdraw         ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=withdraw__, activebackground='#3d3d3d')
            opt_withdraw_button.pack()
            opt_withdraw_button.place(x=0, y=150)
            opt_withdraw_button.bind('<Enter>', func=lambda e: opt_withdraw_button.config(bg='#3d3d3d'))
            opt_withdraw_button.bind('<Leave>', func=lambda e: opt_withdraw_button.config(bg='#1c1c1c'))

            opt_exit_button = tk.Button(root, text='           Exit          ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=exit__, activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=180)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            def left_button_press(*args):
                try:
                    root.destroy()
                except tk.TclError:
                    pass

            self.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.bind('<Button-3>', start_option_menu)

        def refresh_fn(*args):
            refresh()

        def return_home_fn(*args):
            return_home()

        def open_cc_fn(*args):
            open_cc()

        def open_calendar_fn(*args):
            call_calendar()

        def open_scb_fn(*args):
            call_scb()

        def exit_fn(*args):
            on_closing()

        def go_back_fn(*args):
            go_back()

        self.bind('<Control-r>', refresh_fn)
        self.bind('<Alt-h>', return_home_fn)
        self.bind('<Control-f>', open_cc_fn)
        self.bind('<Alt-c>', open_calendar_fn)
        self.bind('<Control-h>', open_scb_fn)
        self.bind('<Control-e>', exit_fn)
        self.bind('<Control-b>', go_back_fn)

        def go_to_deposit_wn_fn(*args):
            self.go_to_deposit_window()

        def go_to_transfer_wn_fn(*args):
            self.go_to_transfer_window()

        def go_to_withdraw_wn_fn(*args):
            self.go_to_withdraw_window()

        self.bind('<Alt-d>', go_to_deposit_wn_fn)
        self.bind('<Alt-t>', go_to_transfer_wn_fn)
        self.bind('<Alt-w>', go_to_withdraw_wn_fn)

    def go_to_deposit_window(self):
        self.destroy()
        from main_directory.Deposit__reg__utils__ import Deposit
        dep_wn = Deposit(self.name, self.card)
        dep_wn.mainloop()

    def go_to_transfer_window(self):
        self.destroy()
        from main_directory.Transfer__reg__utils__ import TransferWn
        dep_wn = TransferWn(self.name, self.card)
        dep_wn.run()

    def go_to_withdraw_window(self):
        self.destroy()
        from main_directory.Withdraw__reg__utils__ import WithdrawWn
        wn = WithdrawWn(self.name, self.card)
        wn.run()

    def usr_exit_request(self):
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            self.destroy()
            import sys
            sys.exit()
