import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from main_directory.open_windows import open_windows_list


class WithdrawWn:

    def __init__(self, name, card):
        self.name = name
        self.card = card

        super(WithdrawWn, self).__init__()

        self.window = tk.Tk()
        self.window.title(f'{self.name.title()}\'s Withdraw Window')

        self.window.config(bg='#ADEFD1')
        self.window.resizable(False, False)
        try:
            self.window.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic8.png"))

            self.img_lb = tk.Label(self.window, image=self.image1, borderwidth=0)
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
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        y = y - 30

        # set the dimensions of the screen
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # home_window.geometry('800x600')

        # _________________fixing window on screen_END___________________________

        label1 = tk.Label(self.window, text='',
                          bg='#00203F',
                          width=6,
                          height=50,
                          font=('Georgia', '13'))
        label1.pack()
        label1.place(x=0, y=70)

        label2 = tk.Label(self.window, text='',
                          bg='#00203F',
                          width=150,
                          height=2,
                          font=('Georgia', '20'))
        label2.pack()
        label2.place(x=0, y=0)

        heading = tk.Label(self.window, text='Withdraw',
                           bg='#00203F',
                           fg='white',
                           font=('Georgia', '30'))
        heading.pack()
        heading.place(x=520, y=5)

        import mysql.connector as sql
        connection = sql.connect(host='localhost',
                                 user='root',
                                 password='dpsbn',
                                 database='client_db')

        if connection.is_connected() is True:
            cur = connection.cursor()
            cur.execute(f"SELECT BALANCE, WITHDRAWALS FROM client WHERE CARD_NUMBER='{card}'")
            result = cur.fetchall()
            cur.close()
            if len(result) != 0:
                available_balance = result[0][0]
                currency_sort = available_balance[:3]

                self.currency_info = tk.Label(self.window,
                                              bg='#ADEFD1',
                                              text=f"Your balance type is {currency_sort}\nYour available balance is \n{available_balance} ",
                                              font=('Courier New', '15'),
                                              justify='left')
                self.currency_info.pack()
                self.currency_info.place(x=85, y=150)

                total_withdrawals = result[0][1]

                self.d_currency_info = tk.Label(self.window,
                                                bg='#ADEFD1',
                                                text=f"Your total withdrawals are \n{total_withdrawals} ",
                                                font=('Courier New', '15'),
                                                justify='left')
                self.d_currency_info.pack()
                self.d_currency_info.place(x=85, y=300)

        self.user_card_number_label = tk.Label(self.window,
                                               bg='#ADEFD1',
                                               text="Enter your card number ",
                                               font=('Georgia', '14'))
        self.user_card_number_label.pack()
        self.user_card_number_label.place(x=500, y=150)

        self.user_card_number_input = ttk.Entry(self.window,
                                                width=25,
                                                font=('aerial', '12'))
        self.user_card_number_input.pack()
        self.user_card_number_input.place(x=504, y=190)

        self.user_card_number_input.focus_force()

        self.cn_check = tk.Label(self.window,
                                 text='',
                                 bg='#ADEFD1',
                                 fg='black')
        self.cn_check.pack()
        self.cn_check.place(x=650, y=220)

        self.user_pin_number_label = tk.Label(self.window,
                                              bg='#ADEFD1',
                                              text="Enter your PIN ",
                                              font=('Georgia', '14'))
        self.user_pin_number_label.pack()
        self.user_pin_number_label.place(x=500, y=240)

        self.user_pin_number_input = ttk.Entry(self.window,
                                               show='*',
                                               width=25,
                                               font=('aerial', '12'))
        self.user_pin_number_input.pack()
        self.user_pin_number_input.place(x=504, y=280)

        self.pin_check = tk.Label(self.window,
                                  text='',
                                  bg='#ADEFD1',
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

        pin___label = tk.Button(self.window,
                                text='○',
                                command=show_pin,
                                relief=tk.FLAT,
                                bg='#ADEFD1')
        pin___label.pack()
        pin___label.place(x=740, y=280)

        self.enter_amount_label = tk.Label(self.window,
                                           bg='#ADEFD1',
                                           text="Enter your Amount ",
                                           font=('Georgia', '14'))
        self.enter_amount_label.pack()
        self.enter_amount_label.place(x=500, y=330)

        self.amount_input = ttk.Entry(self.window,
                                      width=25,
                                      font=('aerial', '12'))
        self.amount_input.pack()
        self.amount_input.place(x=504, y=370)

        self.SUBMIT_BUTTON = tk.Button(self.window, text='     Submit     ',
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

        def go_to_next_textbox(*args):
            if len(self.user_card_number_input.get()) != 0:
                self.user_pin_number_input.focus_force()
            if len(self.user_card_number_input.get()) != 0 and len(self.user_pin_number_input.get()) != 0:
                self.amount_input.focus_force()
            if len(self.user_card_number_input.get()) != 0 and len(self.user_pin_number_input.get()) != 0 and len(self.amount_input.get()) != 0:
                self.submit()

        self.window.bind('<Return>', go_to_next_textbox)

        def go_back():
            self.window.destroy()
            from main_directory.banking_class import Banking
            back_wn = Banking(name, card)
            back_wn.mainloop()

        self.GO_BACK_BUTTON = tk.Button(self.window,
                                        text="  Back  ",
                                        bg='#00203F',
                                        relief=tk.FLAT,
                                        activeforeground='white',
                                        activebackground='#787373',
                                        fg='white',
                                        command=go_back,
                                        font=('Georgia', '10'))
        self.GO_BACK_BUTTON.pack()
        self.GO_BACK_BUTTON.place(x=5, y=20)
        self.GO_BACK_BUTTON.bind('<Enter>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#ADEFD1', fg='black'))
        self.GO_BACK_BUTTON.bind('<Leave>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#00203F', fg='white'))

        def refresh():
            self.window.destroy()
            from main_directory.refresh_windows_functions_file import withdraw_wn_refresh_registry
            withdraw_wn_refresh_registry(name, card)

        self.REFRESH_LABEL = tk.Label(self.window, text='',
                                      bg='#ADEFD1',
                                      font=('Georgia', '12'))
        self.REFRESH_LABEL.pack()
        self.REFRESH_LABEL.place(x=70, y=95)

        self.REFRESH_BUTTON = tk.Button(self.window, text='     \n     ♻      \n     ',
                                        bg='#00203F',
                                        activeforeground='white',
                                        activebackground='#787373',
                                        relief=tk.FLAT,
                                        fg='white',
                                        command=refresh,
                                        font=('Georgia', '10'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=2, y=75)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#ADEFD1', fg='black'), self.REFRESH_LABEL.config(text='   Refresh    ', bg='#00203F', fg='white')))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#00203F', fg='white'), self.REFRESH_LABEL.config(text='', bg='#ADEFD1')))

        exit_button = tk.Button(self.window, text='     \n    Exit    \n     ',
                                bg='#00203F',
                                activeforeground='white',
                                activebackground='maroon',
                                fg='white',
                                command=self.usr_exit_request,
                                relief=tk.FLAT,
                                font=('Georgia', '10'))
        exit_button.pack()
        exit_button.place(x=2, y=537)
        exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
        exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#00203F'))

        def return_home():
            open_windows_list.clear()
            self.window.destroy()

            from main_directory.HomeWindow import home
            home()

        self.HOME_LABEL = tk.Label(self.window, text='',
                                   bg='#ADEFD1',
                                   font=('Georgia', '12'))
        self.HOME_LABEL.pack()
        self.HOME_LABEL.place(x=70, y=155)

        self.HOME_BUTTON = tk.Button(self.window, text='     \n  Home  \n     ',
                                     bg='#00203F',
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=return_home,
                                     font=('Georgia', '10'))
        self.HOME_BUTTON.pack()
        self.HOME_BUTTON.place(x=2, y=140)
        self.HOME_BUTTON.bind('<Enter>', func=lambda e: (self.HOME_BUTTON.config(bg='#ADEFD1', fg='black'), self.HOME_LABEL.config(text='   Home    ', bg='#00203F', fg='white')))
        self.HOME_BUTTON.bind('<Leave>', func=lambda e: (self.HOME_BUTTON.config(bg='#00203F', fg='white'), self.HOME_LABEL.config(text='', bg='#ADEFD1')))

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.window.destroy()
                import sys
                sys.exit()

        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        def right_button_press(*args):
            start_option_menu()

        def start_option_menu(*args):
            root = tk.Tk()

            abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
            abs_coord_y = root.winfo_pointery() - root.winfo_rooty()

            root.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root.geometry("100x118")

            root.overrideredirect(True)
            root.config(bg='#1c1c1c')

            def __go_back__():
                self.window.destroy()
                root.destroy()
                from main_directory.banking_class import Banking
                back_wn = Banking(name, card)
                back_wn.mainloop()

            def refresh__():
                self.window.destroy()
                root.destroy()
                from main_directory.refresh_windows_functions_file import withdraw_wn_refresh_registry
                withdraw_wn_refresh_registry(name, card)

            def return_home__():
                open_windows_list.clear()
                self.window.destroy()
                root.destroy()

                from main_directory.HomeWindow import home
                home()

            opt_back_button = tk.Button(root,
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

            opt_refresh_button = tk.Button(root,
                                           text='       Refresh       ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=refresh__,
                                           activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=30)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_home_button = tk.Button(root,
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

            opt_exit_button = tk.Button(root,
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
                    root.destroy()
                except tk.TclError:
                    pass

            self.window.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.window.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.window.bind('<Button-3>', start_option_menu)

        def back_fn(*args):
            go_back()

        def refresh_fn(*args):
            refresh()

        def return_home_fn(*args):
            return_home()

        def exit_fn(*args):
            on_closing()

        self.window.bind('<Control-b>', back_fn)
        self.window.bind('<Control-r>', refresh_fn)
        self.window.bind('<Alt-h>', return_home_fn)
        self.window.bind('<Control-e>', exit_fn)

    def run(self):
        self.window.mainloop()

    def usr_exit_request(self):
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            self.window.destroy()
            import sys
            sys.exit()

    def submit(self):
        from main_directory.password_functions_file import loading
        import threading
        from main_directory.card_number import hash_pin
        from main_directory.operation_functions_pyfiles import withdraw_successful

        card_number = self.user_card_number_input.get()
        card_number = card_number.lstrip().rstrip()

        if card_number.isdigit():
            if len(card_number) != 0:

                if len(card_number) != 16:
                    self.cn_check.config(text='invalid card number', fg='red')

                    if len(card_number) < 16:
                        messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

                    elif len(card_number) > 16:
                        messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

                else:
                    self.cn_check.config(text='', fg='black')

                    pin = self.user_pin_number_input.get()
                    pin = pin.lstrip().rstrip()

                    if len(pin) != 4:

                        if not pin.isdigit():
                            self.pin_check.config(text='incorrect pin', fg='red')
                            messagebox.showerror(title='Pin Error', message='Enter a valid Pin')

                        elif 4 > len(pin) > 0:
                            self.pin_check.config(text='incorrect pin', fg='red')
                            messagebox.showerror(title='Pin Error', message='Enter a valid pin number\nThe given pin number has less than 4 characters')

                        elif len(pin) > 4:
                            self.pin_check.config(text='incorrect pin', fg='red')
                            messagebox.showerror(title='Pin Error', message='Enter a valid pin number\nThe given pin number has more than 4 characters')

                        elif len(pin) == 0:
                            self.pin_check.config(text='incorrect pin', fg='red')
                            messagebox.showerror(title='Pin Error', message='Enter a valid Pin')

                    else:
                        if not pin.isdigit():
                            self.pin_check.config(text='incorrect pin', fg='red')
                            messagebox.showerror(title='Pin Error', message='Enter a valid Pin')

                        else:
                            self.pin_check.config(text='', fg='black')

                            check_amount = self.amount_input.get()
                            check_amount = check_amount.lstrip().rstrip()

                            if len(check_amount) == 0:
                                messagebox.showerror(title='Amount Error', message='Enter a valid amount')

                            elif not check_amount.isdigit():
                                messagebox.showerror(title='Amount Error', message='Enter a valid amount')

                            else:

                                if pin.isdigit():

                                    __object__ = threading.Thread(target=loading)
                                    __object__.start()

                                    final_pin = hash_pin(pin)

                                    amount = self.amount_input.get()
                                    amount = amount.lstrip().rstrip()

                                    if amount.isdigit():

                                        import mysql.connector as sql

                                        connection = sql.connect(host='localhost',
                                                                 user='root',
                                                                 password='dpsbn',
                                                                 database='client_db')

                                        if connection.is_connected() is True:

                                            cur = connection.cursor()
                                            cur.execute(f"SELECT BALANCE , WITHDRAWALS FROM client WHERE CARD_NUMBER='{card_number}' AND PIN_NUMBER='{final_pin}'")
                                            result = cur.fetchall()
                                            cur.close()

                                            if len(result) != 0:

                                                self.cn_check.config(text='', fg='black')

                                                available_balance = result[0][0]
                                                currency_sort = available_balance[:3]
                                                integer_sort = available_balance[3:]

                                                int_balance = float(integer_sort)
                                                if float(amount) > int_balance:
                                                    messagebox.showinfo(title='Withdraw Error', message='You are low on balance')

                                                else:

                                                    balance = float(integer_sort) - float(amount)
                                                    overall_balance = currency_sort + str(balance)

                                                    withdrawals = result[0][1]
                                                    withdrawals_currency_sort = withdrawals[:3]

                                                    withdrawals_integer_part = withdrawals[3:]
                                                    withdrawals_done = float(withdrawals_integer_part) + float(amount)

                                                    overall_withdrawals_done = withdrawals_currency_sort + str(withdrawals_done)

                                                    response = messagebox.askokcancel(title='Confirm', message='Continue to withdraw?')

                                                    if response is True:
                                                        cur2 = connection.cursor()
                                                        cur2.execute(f"UPDATE client SET BALANCE='{overall_balance}' WHERE CARD_NUMBER='{card_number}'")
                                                        cur2.close()

                                                        cur3 = connection.cursor()
                                                        cur3.execute(f"UPDATE client SET WITHDRAWALS='{overall_withdrawals_done}' WHERE CARD_NUMBER='{card_number}'")
                                                        cur3.close()

                                                        connection.commit()
                                                        connection.close()

                                                        self.window.destroy()
                                                        withdraw_successful()

                                            else:
                                                self.cn_check.config(text='invalid card number or \ninvalid pin number', fg='red')
                                                messagebox.showerror(title='User Error', message='No data found')
                                        else:
                                            messagebox.showerror(title='Server Error', message='The server crashed')
                                    else:
                                        messagebox.showerror(title='Amount Error', message='Enter a number')
                                else:
                                    messagebox.showerror(title='PIN Error', message='Enter a valid PIN')
            else:
                self.cn_check.config(text='invalid card number', fg='red')
                messagebox.showerror(title='Card Number Error', message='Enter a valid Card Number')
        else:
            self.cn_check.config(text='invalid card number', fg='red')
            messagebox.showerror(title='Card Number Error', message='Enter a valid Card Number')
