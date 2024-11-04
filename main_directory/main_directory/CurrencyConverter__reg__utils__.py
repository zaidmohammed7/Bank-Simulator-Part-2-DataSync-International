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


class CurrencyConverter:

    def __init__(self):

        import tkinter as tk
        import tkinter.ttk as ttk

        super(CurrencyConverter, self).__init__()
        print('[ INFO ] Tkinter [ Tkinter     ] : Currency Converter loaded successfully')

        self.wn = tk.Tk()
        self.wn.title('Currency Converter')
        self.wn.resizable(False, False)
        self.wn.focus_force()
        self.wn.config(bg='#d1d1d1')
        try:
            self.wn.iconbitmap(r'..\main_directory\ico1.ico')
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        # ______________fixing window on screen__________credit: stack_overflow

        w = 500  # width for the Tk root
        h = 200  # height for the Tk root

        # get screen width and height
        ws = self.wn.winfo_screenwidth()  # width of the screen
        hs = self.wn.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.wn.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________

        self.from_label = tk.Label(self.wn, text='FROM CURRENCY', bg='#d1d1d1', font=('aerial', '10'))
        self.from_label.pack()
        self.from_label.place(x=57, y=10)

        self.to_label = tk.Label(self.wn, text='CONVERT TO', bg='#d1d1d1', font=('aerial', '10'))
        self.to_label.pack()
        self.to_label.place(x=240, y=10)

        # _______________________________ FROM CURRENCY DROPDOWN ______________________________________________

        get_from_currency = tk.StringVar()
        get_from_currency.set('INR')

        self.from_currency_dropdown = ttk.Combobox(self.wn, textvariable=get_from_currency, state='readonly', width=10, font=('aerial', '12'))

        currency_codes = ['AUD', 'INR', 'USD', 'EUR', 'NZD', 'AED', 'LKR', 'SAR']
        self.from_currency_dropdown['values'] = currency_codes
        self.from_currency_dropdown.pack()
        self.from_currency_dropdown.place(x=60, y=50)

        # _________________________________ TO CURRENCY DROPDOWN _____________________________________________

        get_to_currency = tk.StringVar()
        get_to_currency.set('USD')

        self.to_currency_dropdown = ttk.Combobox(self.wn, textvariable=get_to_currency, state='readonly', width=10, font=('aerial', '12'))

        currency_codes = ['AUD', 'INR', 'USD', 'EUR', 'NZD', 'AED', 'LKR', 'SAR']
        self.to_currency_dropdown['values'] = currency_codes
        self.to_currency_dropdown.pack()
        self.to_currency_dropdown.place(x=230, y=50)

        # ___________________________________ FROM CURRENCY INPUT ____________________________________________

        self.from_currency_input = ttk.Entry(self.wn, width=12, font=('aerial', '12'))
        self.from_currency_input.pack()
        self.from_currency_input.place(x=60, y=90)
        self.from_currency_input.focus_force()

        # ___________________________________ TO CURRENCY ENTRY BOX (NON-INPUT) ______________________________

        self.to_currency_input = ttk.Entry(self.wn, width=12, font=('aerial', '12'))
        self.to_currency_input.pack()
        self.to_currency_input.place(x=230, y=90)
        self.to_currency_input.configure(state=tk.DISABLED)

        # _________________________________________ CONVERT BUTTON _____________________________________________

        self.CONVERT_BUTTON = tk.Button(self.wn, text='    Convert    ',
                                        bg='#2d3a4d',
                                        activeforeground='white',
                                        activebackground='#546f7a',
                                        fg='white',
                                        relief=tk.FLAT,
                                        command=self.convert_currency,
                                        font=('aerial', '12'))
        self.CONVERT_BUTTON.pack()
        self.CONVERT_BUTTON.place(x=150, y=160)
        self.CONVERT_BUTTON.bind('<Enter>', func=lambda e: self.CONVERT_BUTTON.config(bg='#58668a'))
        self.CONVERT_BUTTON.bind('<Leave>', func=lambda e: self.CONVERT_BUTTON.config(bg='#2d3a4d'))

        self.wn.bind('<Return>', self.convert_currency_function)

        # ______________________________________________ REFRESH BUTTON ________________________________________

        self.REFRESH_BUTTON = tk.Button(self.wn,
                                        text='    Refresh    ',
                                        bg='#ababab',
                                        activeforeground='white',
                                        activebackground='#ababab',
                                        fg='black',
                                        relief=tk.FLAT,
                                        command=self.refresh,
                                        font=('aerial', '12'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=400, y=1)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: self.REFRESH_BUTTON.config(bg='#c4b9b9'))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: self.REFRESH_BUTTON.config(bg='#ababab'))

        def on_closing():
            from main_directory.banking_class import currency_run
            currency_run.clear()
            self.wn.destroy()

        self.wn.protocol("WM_DELETE_WINDOW", on_closing)

        def right_button_press(*args):
            start_option_menu()

        def start_option_menu(*args):
            root = tk.Tk()

            abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
            abs_coord_y = root.winfo_pointery() - root.winfo_rooty()

            root.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root.geometry("100x58")

            root.overrideredirect(True)
            root.config(bg='#1c1c1c')

            def refresh__():
                self.wn.destroy()
                root.destroy()
                from main_directory.refresh_windows_functions_file import refresh_currency_converter
                refresh_currency_converter()

            def exit__():
                from main_directory.banking_class import currency_run
                currency_run.clear()
                root.destroy()
                self.wn.destroy()

            opt_refresh_button = tk.Button(root,
                                           text='       Refresh       ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=refresh__,
                                           activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=0)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_exit_button___ = tk.Button(root,
                                           text='           Exit             ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=exit__,
                                           activebackground='#3d3d3d')
            opt_exit_button___.pack()
            opt_exit_button___.place(x=0, y=30)
            opt_exit_button___.bind('<Enter>', func=lambda e: opt_exit_button___.config(bg='#ff0314'))
            opt_exit_button___.bind('<Leave>', func=lambda e: opt_exit_button___.config(bg='#1c1c1c'))

            def left_button_press(*args):
                try:
                    root.destroy()
                except tk.TclError:
                    pass

            self.wn.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.wn.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.wn.bind('<Button-3>', start_option_menu)

        def refresh_fn(*args):
            self.refresh()

        def exit_fn(*args):
            on_closing()

        self.wn.bind('<Control-r>', refresh_fn)
        self.wn.bind('<Control-e>', exit_fn)

    def run(self):
        self.wn.mainloop()

    def convert_currency(self):
        import tkinter as tk

        try:
            from_currency_type = self.from_currency_dropdown.get()
            to_currency_type = self.to_currency_dropdown.get()

            from_currency_value = self.from_currency_input.get()
            from_currency_value = float(from_currency_value)

            # print(from_currency_value, from_currency_type, to_currency_value, to_currency_type)

            convert_to_usd = from_currency_value / currency_exchanges[from_currency_type]

            usd_to_currency = convert_to_usd * currency_exchanges[to_currency_type]

            self.to_currency_input.configure(state=tk.NORMAL)
            self.to_currency_input.delete('0', tk.END)
            self.to_currency_input.insert(tk.END, usd_to_currency)
            self.to_currency_input.configure(state=tk.DISABLED)

        except ValueError:
            pass
        except KeyError:
            pass

    def convert_currency_function(self, *args):
        self.convert_currency()

    def refresh(self):
        self.wn.destroy()
        from main_directory.refresh_windows_functions_file import refresh_currency_converter
        refresh_currency_converter()


CurrencyConverter().run()
