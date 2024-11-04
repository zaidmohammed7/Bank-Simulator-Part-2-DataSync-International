import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from main_directory.open_windows import open_windows_list

currency_exchanges = {
    'USD': 1,
    'INR': 74.30,
    'AUD': 1.40,
    'EUR': 0.85,
    'NZD': 1.46,
    'AED': 3.67,
    'LKR': 199.58,
    'SAR': 3.75

}


class TransferWn:

    def __init__(self, name, card):

        self.name = name
        self.card = card

        super(TransferWn, self).__init__()

        self.root = tk.Tk()
        self.root.title(f'{self.name.title()}\'s Transfer Window')

        self.root.config(bg='#97BC62')
        self.root.resizable(False, False)
        try:
            self.root.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic9.png"))

            self.img_lb = tk.Label(self.root, image=self.image1, borderwidth=0)
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
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        y = y - 30

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # home_window.geometry('800x600')

        # _________________fixing window on screen_END___________________________

        label1 = tk.Label(self.root, text='',
                          bg='#2C5F2D',
                          width=6,
                          height=50,
                          font=('Georgia', '13'))
        label1.pack()
        label1.place(x=0, y=70)

        label2 = tk.Label(self.root, text='',
                          bg='#2C5F2D',
                          width=150,
                          height=2,
                          font=('Georgia', '20'))
        label2.pack()
        label2.place(x=0, y=0)

        heading = tk.Label(self.root, text='Transfer',
                           bg='#2C5F2D',
                           fg='white',
                           font=('Georgia', '30'))
        heading.pack()
        heading.place(x=530, y=5)

        import mysql.connector as sql
        connection = sql.connect(host='localhost',
                                 user='root',
                                 password='dpsbn',
                                 database='client_db')

        if connection.is_connected() is True:
            cur = connection.cursor()
            cur.execute(f"SELECT BALANCE, TRANSFERS FROM client WHERE CARD_NUMBER='{card}'")
            result = cur.fetchall()
            cur.close()
            if len(result) != 0:
                available_balance = result[0][0]
                currency_sort = available_balance[:3]

                self.currency_info = tk.Label(self.root,
                                              bg='#97BC62',
                                              text=f"Your balance type is {currency_sort}\nYour available balance is \n{available_balance} ",
                                              font=('Courier New', '15'),
                                              justify='left')
                self.currency_info.pack()
                self.currency_info.place(x=85, y=150)

                total_transfers = result[0][1]

                self.d_currency_info = tk.Label(self.root,
                                                bg='#97BC62',
                                                text=f"Your total transfers are \n{total_transfers} ",
                                                font=('Courier New', '15'),
                                                justify='left')
                self.d_currency_info.pack()
                self.d_currency_info.place(x=85, y=300)

        self.user_card_number_label = tk.Label(self.root,
                                               bg='#97BC62',
                                               text="Enter your card number ",
                                               font=('Georgia', '14'))
        self.user_card_number_label.pack()
        self.user_card_number_label.place(x=500, y=150)

        self.user_card_number_input = ttk.Entry(self.root,
                                                width=25,
                                                font=('aerial', '12'))
        self.user_card_number_input.pack()
        self.user_card_number_input.place(x=504, y=190)

        self.cn_u_check = tk.Label(self.root,
                                   text='',
                                   bg='#97BC62',
                                   fg='black')
        self.cn_u_check.pack()
        self.cn_u_check.place(x=650, y=220)

        self.user_card_number_input.focus_force()

        self.user_pin_number_label = tk.Label(self.root,
                                              bg='#97BC62',
                                              text="Enter your PIN ",
                                              font=('Georgia', '14'))
        self.user_pin_number_label.pack()
        self.user_pin_number_label.place(x=500, y=240)

        self.user_pin_number_input = ttk.Entry(self.root,
                                               show='*',
                                               width=25,
                                               font=('aerial', '12'))
        self.user_pin_number_input.pack()
        self.user_pin_number_input.place(x=504, y=280)

        self.pin_check = tk.Label(self.root,
                                   text='',
                                   bg='#97BC62',
                                   fg='black')
        self.pin_check.pack()
        self.pin_check.place(x=650, y=310)

        def hide_pin():
            pin___label.config(command=show_pin, text='○')
            self.user_pin_number_input.configure(show='*')
            pass

        def show_pin():
            pin___label.config(command=hide_pin, text='—')
            self.user_pin_number_input.configure(show='')
            pass

        pin___label = tk.Button(self.root,
                                text='○',
                                command=show_pin,
                                relief=tk.FLAT,
                                bg='#97BC62')
        pin___label.pack()
        pin___label.place(x=740, y=280)

        self.receivers_card_number_label = tk.Label(self.root,
                                                    bg='#97BC62',
                                                    text="Enter receiver's card number ",
                                                    font=('Georgia', '14'))
        self.receivers_card_number_label.pack()
        self.receivers_card_number_label.place(x=500, y=330)

        self.receivers_card_number_input = ttk.Entry(self.root,
                                                     width=25,
                                                     font=('aerial', '12'))
        self.receivers_card_number_input.pack()
        self.receivers_card_number_input.place(x=504, y=370)

        self.cn_r_check = tk.Label(self.root,
                                   text='',
                                   bg='#97BC62',
                                   fg='black')
        self.cn_r_check.pack()
        self.cn_r_check.place(x=650, y=400)

        self.enter_amount_label = tk.Label(self.root,
                                           bg='#97BC62',
                                           text="Enter your Amount ",
                                           font=('Georgia', '14'))
        self.enter_amount_label.pack()
        self.enter_amount_label.place(x=500, y=420)

        self.amount_input = ttk.Entry(self.root,
                                      width=25,
                                      font=('aerial', '12'))
        self.amount_input.pack()
        self.amount_input.place(x=504, y=460)

        def go_back():
            self.root.destroy()
            from main_directory.banking_class import Banking
            back_wn = Banking(name, card)
            back_wn.mainloop()

        self.GO_BACK_BUTTON = tk.Button(self.root,
                                        text="  Back  ",
                                        bg='#2C5F2D',
                                        relief=tk.FLAT,
                                        activeforeground='white',
                                        activebackground='#787373',
                                        fg='white',
                                        command=go_back,
                                        font=('Georgia', '10'))
        self.GO_BACK_BUTTON.pack()
        self.GO_BACK_BUTTON.place(x=5, y=20)
        self.GO_BACK_BUTTON.bind('<Enter>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#97BC62', fg='black'))
        self.GO_BACK_BUTTON.bind('<Leave>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#2C5F2D', fg='white'))

        def refresh():
            self.root.destroy()
            from main_directory.refresh_windows_functions_file import transfer_wn_refresh_registry
            transfer_wn_refresh_registry(name, card)

        self.REFRESH_LABEL = tk.Label(self.root, text='',
                                      bg='#97BC62',
                                      font=('Georgia', '12'))
        self.REFRESH_LABEL.pack()
        self.REFRESH_LABEL.place(x=70, y=95)

        self.REFRESH_BUTTON = tk.Button(self.root, text='     \n     ♻      \n     ',
                                        bg='#2C5F2D',
                                        activeforeground='white',
                                        activebackground='#787373',
                                        relief=tk.FLAT,
                                        fg='white',
                                        command=refresh,
                                        font=('Georgia', '10'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=2, y=75)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#97BC62', fg='black'), self.REFRESH_LABEL.config(text='   Refresh    ', bg='#2C5F2D', fg='white')))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#2C5F2D', fg='white'), self.REFRESH_LABEL.config(text='', bg='#97BC62')))

        def return_home():
            open_windows_list.clear()
            self.root.destroy()

            from main_directory.HomeWindow import home
            home()

        self.HOME_LABEL = tk.Label(self.root, text='',
                                   bg='#97BC62',
                                   font=('Georgia', '12'))
        self.HOME_LABEL.pack()
        self.HOME_LABEL.place(x=70, y=155)

        self.HOME_BUTTON = tk.Button(self.root, text='     \n  Home  \n     ',
                                     bg='#2C5F2D',
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=return_home,
                                     font=('Georgia', '10'))
        self.HOME_BUTTON.pack()
        self.HOME_BUTTON.place(x=2, y=140)
        self.HOME_BUTTON.bind('<Enter>', func=lambda e: (self.HOME_BUTTON.config(bg='#97BC62', fg='black'), self.HOME_LABEL.config(text='   Home    ', bg='#2C5F2D', fg='white')))
        self.HOME_BUTTON.bind('<Leave>', func=lambda e: (self.HOME_BUTTON.config(bg='#2C5F2D', fg='white'), self.HOME_LABEL.config(text='', bg='#97BC62')))

        self.CURRENCY_CONV_LABEL = tk.Label(self.root, text='',
                                            bg='#97BC62',
                                            font=('Georgia', '12'))
        self.CURRENCY_CONV_LABEL.pack()
        self.CURRENCY_CONV_LABEL.place(x=70, y=210)

        def open_cc():
            from main_directory.banking_class import currency_run
            if len(currency_run) == 0:
                currency_run.append(1)

                from main_directory.CurrencyConverter__reg__utils__ import CurrencyConverter
                app = CurrencyConverter()
                app.run()

        self.CURRENCY_CONV_BUTTON = tk.Button(self.root, text='     \n      CC     \n     ',
                                              bg='#2C5F2D',
                                              activeforeground='white',
                                              activebackground='#787373',
                                              relief=tk.FLAT,
                                              fg='white',
                                              command=open_cc,
                                              font=('Georgia', '10'))
        self.CURRENCY_CONV_BUTTON.pack()
        self.CURRENCY_CONV_BUTTON.place(x=2, y=200)
        self.CURRENCY_CONV_BUTTON.bind('<Enter>', func=lambda e: (self.CURRENCY_CONV_BUTTON.config(bg='#97BC62', fg='black'), self.CURRENCY_CONV_LABEL.config(text='   Currency Converter    ', bg='#2C5F2D', fg='white')))
        self.CURRENCY_CONV_BUTTON.bind('<Leave>', func=lambda e: (self.CURRENCY_CONV_BUTTON.config(bg='#2C5F2D', fg='white'), self.CURRENCY_CONV_LABEL.config(text='', bg='#97BC62')))

        self.SUBMIT_BUTTON = tk.Button(self.root, text='     Submit     ',
                                       bg='#364f44',
                                       activeforeground='black',
                                       activebackground='#364f44',
                                       fg='white',
                                       relief=tk.FLAT,
                                       command=self.submit,
                                       font=('Georgia', '10'))
        self.SUBMIT_BUTTON.pack()
        self.SUBMIT_BUTTON.place(x=570, y=540)
        self.SUBMIT_BUTTON.bind('<Enter>', func=lambda e: self.SUBMIT_BUTTON.config(bg='#547a6a'))
        self.SUBMIT_BUTTON.bind('<Leave>', func=lambda e: self.SUBMIT_BUTTON.config(bg='#364f44'))

        self.EXIT_BUTTON = tk.Button(self.root, text='     \n    Exit    \n     ',
                                     bg='#2C5F2D',
                                     activeforeground='white',
                                     activebackground='maroon',
                                     fg='white',
                                     command=self.usr_exit_request,
                                     relief=tk.FLAT,
                                     font=('Georgia', '10'))
        self.EXIT_BUTTON.pack()
        self.EXIT_BUTTON.place(x=2, y=537)
        self.EXIT_BUTTON.bind('<Enter>', func=lambda e: self.EXIT_BUTTON.config(bg='#ff0314'))
        self.EXIT_BUTTON.bind('<Leave>', func=lambda e: self.EXIT_BUTTON.config(bg='#2C5F2D'))

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                import sys
                sys.exit()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        def go_to_next_textbox(*args):
            if len(self.user_card_number_input.get()) != 0:
                self.user_pin_number_input.focus_force()
            if len(self.user_card_number_input.get()) != 0 and len(self.user_pin_number_input.get()) != 0:
                self.receivers_card_number_input.focus_force()
            if len(self.user_card_number_input.get()) != 0 and len(self.user_pin_number_input.get()) != 0 and len(self.receivers_card_number_input.get()) != 0:
                self.amount_input.focus_force()
            if len(self.user_card_number_input.get()) != 0 and len(self.user_pin_number_input.get()) != 0 and len(self.receivers_card_number_input.get()) != 0 and len(self.amount_input.get()) != 0:
                self.submit()

        self.root.bind('<Return>', go_to_next_textbox)

        def right_button_press(*args):
            start_option_menu()

        def start_option_menu(*args):
            root_ = tk.Tk()

            abs_coord_x = root_.winfo_pointerx() - root_.winfo_rootx()
            abs_coord_y = root_.winfo_pointery() - root_.winfo_rooty()

            root_.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root_.geometry("100x118")

            root_.overrideredirect(True)
            root_.config(bg='#1c1c1c')

            def __go_back__():
                self.root.destroy()
                root_.destroy()
                from main_directory.banking_class import Banking
                back_wn = Banking(name, card)
                back_wn.mainloop()

            def refresh__():
                self.root.destroy()
                root_.destroy()
                from main_directory.refresh_windows_functions_file import transfer_wn_refresh_registry
                transfer_wn_refresh_registry(name, card)

            def return_home__():
                open_windows_list.clear()
                self.root.destroy()
                root_.destroy()

                from main_directory.HomeWindow import home
                home()

            opt_back_button = tk.Button(root_,
                                        text='         Back           ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=__go_back__,
                                        activebackground='#3d3d3d')
            opt_back_button.pack()
            opt_back_button.place(x=0, y=0)
            opt_back_button.bind('<Enter>', func=lambda e: opt_back_button.config(bg='#3d3d3d'))
            opt_back_button.bind('<Leave>', func=lambda e: opt_back_button.config(bg='#1c1c1c'))

            opt_refresh_button = tk.Button(root_,
                                           text='       Refresh       ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white', command=refresh__,
                                           activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=30)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_home_button = tk.Button(root_,
                                        text=' Return Home     ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=return_home__,
                                        activebackground='#3d3d3d')
            opt_home_button.pack()
            opt_home_button.place(x=0, y=60)
            opt_home_button.bind('<Enter>', func=lambda e: opt_home_button.config(bg='#3d3d3d'))
            opt_home_button.bind('<Leave>', func=lambda e: opt_home_button.config(bg='#1c1c1c'))

            def exit__():
                response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
                if response is True:
                    import sys
                    sys.exit()

            opt_exit_button = tk.Button(root_,
                                        text='           Exit          ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=exit__,
                                        activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=90)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            def left_button_press(*args):
                try:
                    root_.destroy()
                except tk.TclError:
                    pass

            self.root.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root_.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.root.bind('<Button-3>', right_button_press__)

            root_.after(4000, lambda: root_.destroy())

        self.root.bind('<Button-3>', start_option_menu)

        def back_fn(*args):
            go_back()

        def refresh_fn(*args):
            refresh()

        def return_home_fn(*args):
            return_home()

        def exit_fn(*args):
            on_closing()

        def open_cc_fn(*args):
            open_cc()

        self.root.bind('<Control-b>', back_fn)
        self.root.bind('<Control-r>', refresh_fn)
        self.root.bind('<Alt-h>', return_home_fn)
        self.root.bind('<Control-e>', exit_fn)
        self.root.bind('<Control-f>', open_cc_fn)

    def run(self):
        self.root.mainloop()

    def usr_exit_request(self):
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            self.root.destroy()
            import sys
            sys.exit()

    def submit(self):
        from main_directory.password_functions_file import loading
        import threading
        from main_directory.card_number import hash_pin

        user_card_number_ = self.user_card_number_input.get()
        user_card_number_ = user_card_number_.lstrip().rstrip()

        if user_card_number_.isdigit():

            if len(user_card_number_) != 0:

                if len(user_card_number_) != 16:
                    self.cn_u_check.config(text='invalid card number', fg='red')

                    if len(user_card_number_) < 16:
                        messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

                    elif len(user_card_number_) > 16:
                        messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

                else:
                    self.cn_u_check.config(text='', fg='black')

                    user_pin_ = self.user_pin_number_input.get()
                    user_pin_ = user_pin_.lstrip().rstrip()

                    if len(user_pin_) != 4:
                        if not user_pin_.isdigit():
                            messagebox.showerror(title='Pin Error', message='Enter a valid Pin')
                            self.pin_check.config(text='incorrect pin number', fg='red')

                        elif 4 > len(user_pin_) > 0:
                            messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number\nThe given pin number has less than 4 characters')
                            self.pin_check.config(text='incorrect pin number', fg='red')

                        elif len(user_pin_) > 4:
                            messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number\nThe given pin number has more than 4 characters')
                            self.pin_check.config(text='incorrect pin number', fg='red')

                        elif len(user_pin_) == 0:
                            messagebox.showerror(title='Pin Error', message='Enter a valid Pin')
                            self.pin_check.config(text='incorrect pin number', fg='red')

                    else:
                        if not user_pin_.isdigit():
                            messagebox.showerror(title='Pin Error', message='Enter a valid Pin')
                            self.pin_check.config(text='incorrect pin number', fg='red')

                        else:
                            self.pin_check.config(text='', fg='black')

                            check_amount = self.amount_input.get()
                            check_amount = check_amount.lstrip().rstrip()

                            if len(check_amount) == 0:
                                messagebox.showerror(title='Amount Error', message='Enter a valid amount')

                            elif not check_amount.isdigit():
                                messagebox.showerror(title='Amount Error', message='Enter a valid amount')

                            else:

                                check_receivers_card_number = self.receivers_card_number_input.get()
                                check_receivers_card_number = check_receivers_card_number.lstrip().rstrip()

                                if len(check_receivers_card_number) != 16:
                                    if not check_receivers_card_number.isdigit():
                                        messagebox.showerror(title='Receiver\'s Card Number Error', message='Enter a valid card number')
                                        self.cn_r_check.config(text='invalid card number', fg='red')

                                    elif 16 > len(check_receivers_card_number) > 0:
                                        messagebox.showerror(title='Receiver\'s Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')
                                        self.cn_r_check.config(text='invalid card number', fg='red')

                                    elif len(check_receivers_card_number) > 16:
                                        messagebox.showerror(title='Receiver\'s Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')
                                        self.cn_r_check.config(text='invalid card number', fg='red')

                                    elif len(check_receivers_card_number) == 0:
                                        messagebox.showerror(title='Receiver\'s Card Number Error', message='Enter a valid card number')
                                        self.cn_r_check.config(text='invalid card number', fg='red')

                                else:
                                    if not check_receivers_card_number.isdigit():
                                        messagebox.showerror(title='Receiver\'s Card Number Error', message='Enter a valid card number')
                                        self.cn_r_check.config(text='invalid card number', fg='red')

                                    else:
                                        self.cn_r_check.config(text='', fg='black')

                                        if user_pin_.isdigit():
                                            if len(user_pin_) != 0:
                                                __object__ = threading.Thread(target=loading)
                                                __object__.start()

                                                final_pin = hash_pin(user_pin_)

                                                import mysql.connector as sql

                                                connection = sql.connect(host='localhost',
                                                                         user='root',
                                                                         password='dpsbn',
                                                                         database='client_db')

                                                if connection.is_connected() is True:
                                                    cur = connection.cursor()
                                                    cur.execute(f"SELECT BALANCE, TRANSFERS FROM client WHERE CARD_NUMBER='{user_card_number_}' AND PIN_NUMBER='{final_pin}'")
                                                    result = cur.fetchall()
                                                    cur.close()

                                                    if len(result) != 0:
                                                        self.cn_u_check.config(text='', fg='black')

                                                        net_balance = result[0][0]  # INR45
                                                        user_country_code = net_balance[0:3]

                                                        user_balance = net_balance[3:]
                                                        user_balance = float(user_balance)

                                                        amount_transferred = result[0][1]
                                                        transfers_user_country_code = amount_transferred[0:3]

                                                        transfers_user_balance = amount_transferred[3:]
                                                        transfers_user_balance = float(transfers_user_balance)

                                                        receivers_card_number_ = self.receivers_card_number_input.get()
                                                        receivers_card_number_ = receivers_card_number_.lstrip().rstrip()

                                                        cur2 = connection.cursor()
                                                        cur2.execute(f"SELECT NAME, BALANCE FROM client WHERE CARD_NUMBER = '{receivers_card_number_}'")
                                                        result2 = cur2.fetchall()
                                                        cur2.close()
                                                        if len(result2) != 0:
                                                            if user_card_number_ == receivers_card_number_:
                                                                messagebox.showerror(title='Card Number Error', message='Card numbers can not be the same')
                                                                self.cn_r_check.config(text='card number can\'t \nbe same', fg='red')
                                                            else:
                                                                self.cn_r_check.config(text='', fg='black')
                                                                receivers_name = result2[0][0]

                                                                receivers_net_balance = result2[0][1]
                                                                receivers_country_code = receivers_net_balance[0:3]

                                                                receivers_balance = receivers_net_balance[3:]
                                                                receivers_balance = float(receivers_balance)

                                                                transfer_amount = self.amount_input.get()
                                                                transfer_amount = transfer_amount.lstrip().rstrip()

                                                                if transfer_amount.isdigit():

                                                                    transfer_amount = float(transfer_amount)

                                                                    if transfer_amount > user_balance:

                                                                        messagebox.showinfo(title='Alert!', message='You have low balance')

                                                                    else:

                                                                        convert_to_usd = transfer_amount/currency_exchanges[user_country_code]
                                                                        usd_to_other_currency = convert_to_usd * currency_exchanges[receivers_country_code]

                                                                        new_user_balance = user_balance - transfer_amount
                                                                        new_receiver_balance = receivers_balance + usd_to_other_currency
                                                                        new_receiver_balance = round(new_receiver_balance, 2)

                                                                        net_user_balance = str(user_country_code) + str(new_user_balance)
                                                                        net_receivers_balance = str(receivers_country_code) + str(new_receiver_balance)

                                                                        new_transfers = transfers_user_balance + transfer_amount
                                                                        net_transfers_done = str(transfers_user_country_code) + str(new_transfers)

                                                                        user_response = messagebox.askokcancel(title='Confirm Transaction?', message=f'Do you want to continue with the transaction of {user_country_code}{transfer_amount} to {receivers_name}')

                                                                        if user_response is True:

                                                                            cur3 = connection.cursor()
                                                                            cur3.execute(f"UPDATE client SET BALANCE = '{net_user_balance}' WHERE CARD_NUMBER = '{user_card_number_}'")
                                                                            cur3.close()

                                                                            cur3_ = connection.cursor()
                                                                            cur3_.execute(f"UPDATE client SET TRANSFERS = '{net_transfers_done}' WHERE CARD_NUMBER = '{user_card_number_}'")
                                                                            cur3_.close()

                                                                            cur4 = connection.cursor()
                                                                            cur4.execute(f"UPDATE client SET BALANCE = '{net_receivers_balance}' WHERE CARD_NUMBER = '{receivers_card_number_}'")
                                                                            cur4.close()
                                                                            connection.commit()
                                                                            connection.close()

                                                                            self.root.destroy()
                                                                            from main_directory.operation_functions_pyfiles import transfer_successful
                                                                            transfer_successful()

                                                                        else:
                                                                            messagebox.showinfo(title='Alert!', message='You have not transferred the amount')
                                                                    pass
                                                                else:
                                                                    messagebox.showerror(title='Amount Error', message='Enter numbers only!')

                                                        else:
                                                            self.cn_r_check.config(text='card number not found', fg='red')
                                                            messagebox.showerror(title='Receiver Error', message='Receiver not found!')

                                                    else:
                                                        self.cn_u_check.config(text='invalid card number or \ninvalid pin number', fg='red')
                                                        messagebox.showerror(title='User Error', message='No data found')
                                            else:
                                                messagebox.showerror(title='Pin Number Error', message='Enter a valid Pin')
                                        else:
                                            messagebox.showerror(title='Pin Number Error', message='Enter a valid Pin')

                pass
            else:
                self.cn_u_check.config(text='invalid card number', fg='red')
                messagebox.showerror(title='Card Number Error', message='Enter a valid Card Number')
        else:
            self.cn_u_check.config(text='invalid card number', fg='red')
            messagebox.showerror(title='Card Number Error', message='Enter a valid Card Number')
