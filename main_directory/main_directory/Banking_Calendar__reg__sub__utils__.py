import calendar
import datetime
import tkinter as tk
import tkinter.ttk as ttk

from main_directory.open_windows import open_windows_list
from tkinter import messagebox

check_list = []

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

months_names_to_values = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}


class BankingCalendar:

    def __init__(self, name, card):
        self.name = name
        self.card = card

        super(BankingCalendar, self).__init__()

        print('[ INFO ] Tkinter [ Tkinter     ] : Calender [ __main__     ] loaded successfully')

        self.wn = tk.Tk()
        self.wn.title('Calendar')
        self.wn.config(bg='#bab197')
        self.wn.resizable(False, False)
        try:
            self.wn.iconbitmap(r'..\main_directory\ico1.ico')
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass
        self.wn.focus_force()

        # ___________________fixing window on screen_START_______credit: stack_overflow

        w = 800  # width for the Tk root
        h = 600  # height for the Tk root

        # get screen width and height
        ws = self.wn.winfo_screenwidth()  # width of the screen
        hs = self.wn.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        y = y - 30

        # set the dimensions of the screen
        # and where it is placed
        self.wn.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # home_window.geometry('800x600')

        # _________________fixing window on screen_END___________________________

        # _________________________window design - START ________________________

        self.right_half_color = tk.Label(self.wn, text=' ', bg='#544e40', width=400, height=100)
        self.right_half_color.pack()
        self.right_half_color.place(x=370, y=0)

        self.left_side_bar_color = tk.Label(self.wn, text=' ', bg='#544e40', width=6, height=100, font=('Georgia', '13'))
        self.left_side_bar_color.pack()
        self.left_side_bar_color.place(x=0, y=0)

        # _________________________ window design - END _________________________

        date = datetime.date.today()

        self.__today__ = datetime.datetime.strptime(str(date), '%Y-%m-%d')
        self.__month__ = self.__today__.month
        self.__year__ = self.__today__.year
        self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))  # creates calendar like display

        self.label = tk.Label(self.wn, text=self.__month_calendar__, font=('Courier New', '25'), bg='#544e40', fg='white', justify='left')
        self.label.pack()
        self.label.place(x=380, y=50)

        __date__ = datetime.datetime.now()
        date_in_words = __date__.strftime('%A %d %B %Y')

        self.date_ = tk.Label(self.wn, text=('Today:  ' + str(date_in_words)), font=('Georgia', '15'), bg='#544e40', fg='white')
        self.date_.pack()
        self.date_.place(x=410, y=400)

        self.NEXT_BTN = tk.Button(self.wn, text='    >    ', command=self.next_function, font=('Calibre', '20'), relief=tk.FLAT, bg='#9c8f6b', activebackground='#bab197')
        self.NEXT_BTN.pack()
        self.NEXT_BTN.place(x=656, y=500)
        self.NEXT_BTN.bind('<Enter>', func=lambda e: self.NEXT_BTN.configure(bg='#baaa7f'))
        self.NEXT_BTN.bind('<Leave>', func=lambda e: self.NEXT_BTN.configure(bg='#9c8f6b'))

        self.PREV_BTN2 = tk.Button(self.wn, text='    <    ', command=self.prev_function, font=('Calibre', '20'), relief=tk.FLAT, bg='#9c8f6b', activebackground='#bab197')
        self.PREV_BTN2.pack()
        self.PREV_BTN2.place(x=415, y=500)
        self.PREV_BTN2.bind('<Enter>', func=lambda e: self.PREV_BTN2.configure(bg='#baaa7f'))
        self.PREV_BTN2.bind('<Leave>', func=lambda e: self.PREV_BTN2.configure(bg='#9c8f6b'))

        # ________________________________ user entry boxes ___________________________________

        self.m_label = tk.Label(self.wn, text='Month', bg='#bab197', font=('aerial', '12'))
        self.m_label.pack()
        self.m_label.place(x=150, y=50)

        self.y_label = tk.Label(self.wn, text='Year', bg='#bab197', font=('aerial', '12'))
        self.y_label.pack()
        self.y_label.place(x=150, y=100)

        get_month = tk.StringVar()
        get_month.set(months[self.__month__])

        self.months_dropdown = ttk.Combobox(self.wn, textvariable=get_month, state='readonly', width=10, font=('aerial', '12'))
        self.months_dropdown['values'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.months_dropdown.pack()
        self.months_dropdown.place(x=200, y=50)

        get_year = tk.StringVar()
        get_year.set(months[self.__month__])

        self.years_dropdown = ttk.Combobox(self.wn, textvariable=get_year, width=10, font=('aerial', '12'))
        self.years_dropdown['values'] = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        self.years_dropdown.pack()
        self.years_dropdown.place(x=200, y=100)

        self.GET_CALENDAR = tk.Button(self.wn, text='  Get Calendar   ', relief=tk.FLAT, bg='#9c8f6b', font=('Calibre', '15'), command=self.get_calendar_func)
        self.GET_CALENDAR.pack()
        self.GET_CALENDAR.place(x=150, y=150)
        self.GET_CALENDAR.bind('<Enter>', func=lambda e: self.GET_CALENDAR.configure(bg='#baaa7f'))
        self.GET_CALENDAR.bind('<Leave>', func=lambda e: self.GET_CALENDAR.configure(bg='#9c8f6b'))

        self.TODAY_CALENDAR = tk.Button(self.wn, text=' Today ', relief=tk.FLAT, bg='#9c8f6b', font=('Calibre', '20'), command=self.get_today_function, activebackground='#bab197')
        self.TODAY_CALENDAR.pack()
        self.TODAY_CALENDAR.place(x=530, y=500)
        self.TODAY_CALENDAR.bind('<Enter>', func=lambda e: self.TODAY_CALENDAR.configure(bg='#baaa7f'))
        self.TODAY_CALENDAR.bind('<Leave>', func=lambda e: self.TODAY_CALENDAR.configure(bg='#9c8f6b'))

        def next_fn(*args):
            self.next_function()

        self.wn.bind('<Right>', next_fn)

        def prev_fn(*args):
            self.prev_function()

        self.wn.bind('<Left>', prev_fn)

        def today_fn(*args):
            self.get_today_function()

        self.wn.bind('<Control-t>', today_fn)

        def return_home():
            self.wn.destroy()
            open_windows_list.clear()
            from main_directory.HomeWindow import home
            home()

        self.HOME_LABEL = tk.Label(self.wn, text='',
                                   bg='#bab197',
                                   font=('Georgia', '12'))
        self.HOME_LABEL.pack()
        self.HOME_LABEL.place(x=70, y=155)

        self.HOME_BUTTON = tk.Button(self.wn, text='     \n  Home  \n     ',
                                     bg='#544e40',
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=return_home,
                                     font=('Georgia', '10'))
        self.HOME_BUTTON.pack()
        self.HOME_BUTTON.place(x=2, y=140)
        self.HOME_BUTTON.bind('<Enter>', func=lambda e: (self.HOME_BUTTON.config(bg='#bab197', fg='black'), self.HOME_LABEL.config(text='   Home    ', bg='#cfb476', fg='black')))
        self.HOME_BUTTON.bind('<Leave>', func=lambda e: (self.HOME_BUTTON.config(bg='#544e40', fg='white'), self.HOME_LABEL.config(text='', bg='#bab197')))

        self.EXIT_BUTTON = tk.Button(self.wn, text='     \n    Exit    \n     ',
                                     bg='#544e40',
                                     activeforeground='white',
                                     activebackground='maroon',
                                     fg='white',
                                     command=self.usr_exit_request,
                                     relief=tk.FLAT,
                                     font=('Georgia', '10'))
        self.EXIT_BUTTON.pack()
        self.EXIT_BUTTON.place(x=2, y=537)
        self.EXIT_BUTTON.bind('<Enter>', func=lambda e: self.EXIT_BUTTON.config(bg='#ff0314'))
        self.EXIT_BUTTON.bind('<Leave>', func=lambda e: self.EXIT_BUTTON.config(bg='#544e40'))

        def refresh():
            self.wn.destroy()
            from main_directory.refresh_windows_functions_file import refresh_banking_calendar__utils__
            refresh_banking_calendar__utils__(self.name, self.card)

        self.REFRESH_LABEL = tk.Label(self.wn, text='',
                                      bg='#bab197',
                                      font=('Georgia', '12'))
        self.REFRESH_LABEL.pack()
        self.REFRESH_LABEL.place(x=70, y=95)

        self.REFRESH_BUTTON = tk.Button(self.wn, text='     \n     ♻      \n     ',
                                        bg='#544e40',
                                        activeforeground='white',
                                        activebackground='#787373',
                                        relief=tk.FLAT,
                                        fg='white',
                                        command=refresh,
                                        font=('Georgia', '10'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=2, y=75)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#bab197', fg='black'), self.REFRESH_LABEL.config(text='   Refresh    ', bg='#cfb476', fg='black')))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#544e40', fg='white'), self.REFRESH_LABEL.config(text='', bg='#bab197')))

        self.wn.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.GO_BACK_BUTTON = tk.Button(self.wn,
                                        text="  Back  ",
                                        bg='#cfb476',
                                        relief=tk.FLAT,
                                        activeforeground='white',
                                        activebackground='#787373',
                                        fg='black',
                                        command=self.go_back,
                                        font=('Georgia', '10'))
        self.GO_BACK_BUTTON.pack()
        self.GO_BACK_BUTTON.place(x=5, y=20)
        self.GO_BACK_BUTTON.bind('<Enter>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#dbdbdb', fg='black'))
        self.GO_BACK_BUTTON.bind('<Leave>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#cfb476', fg='black'))

        self.POP_OUT_WN_LABEL = tk.Label(self.wn, text='',
                                         bg='#544e40',
                                         fg='white',
                                         font=('Georgia', '12'))
        self.POP_OUT_WN_LABEL.pack()
        self.POP_OUT_WN_LABEL.place(x=730, y=40)

        self.POP_OUT_WN_BUTTON = tk.Button(self.wn,
                                           text="➰",
                                           bg='#cfb476',
                                           relief=tk.FLAT,
                                           activeforeground='white',
                                           activebackground='#787373',
                                           fg='black',
                                           command=self.pop_out,
                                           font=('Georgia', '10'))
        self.POP_OUT_WN_BUTTON.pack()
        self.POP_OUT_WN_BUTTON.place(x=750, y=10)
        self.POP_OUT_WN_BUTTON.bind('<Enter>', func=lambda e: (self.POP_OUT_WN_BUTTON.config(bg='#dbdbdb', fg='black'), self.POP_OUT_WN_LABEL.config(text='Pop Out')))
        self.POP_OUT_WN_BUTTON.bind('<Leave>', func=lambda e: (self.POP_OUT_WN_BUTTON.config(bg='#cfb476', fg='black'), self.POP_OUT_WN_LABEL.config(text='', bg='#544e40')))

        def right_button_press(*args):
            start_option_menu()

        def start_option_menu(*args):
            root = tk.Tk()

            abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
            abs_coord_y = root.winfo_pointery() - root.winfo_rooty()

            root.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root.geometry("100x148")

            root.overrideredirect(True)
            root.config(bg='#1c1c1c')

            def refresh__():
                root.destroy()
                refresh()

            def return_home__():
                root.destroy()
                return_home()

            def __go_back__():

                self.wn.destroy()

                from main_directory.banking_class import Banking
                connect_banking_class = Banking(self.name, self.card)
                connect_banking_class.mainloop()

            opt_back_button = tk.Button(root, text='         Back           ',
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

            opt_refresh_button = tk.Button(root, text='       Refresh       ',
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

            opt_home_button = tk.Button(root, text=' Return Home     ',
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

            def pop_out__():
                from main_directory.Calendar__reg__utils__ import value_list

                if len(value_list) == 0:
                    if len(check_list) == 0:
                        value_list.append(1)
                        check_list.append(1)

                        self.wn.destroy()

                        from main_directory.BankingPopOutCalendar__reg__sub__utils__ import BankingPopOutCalendar

                        def run_banking_pop_out_calendar():
                            app = BankingPopOutCalendar(self.name, self.card)
                            app.run()

                        self.wn.after(10, lambda: run_banking_pop_out_calendar())
                        root.destroy()

                        from main_directory.banking_class import Banking
                        connect_banking_class = Banking(self.name, self.card)
                        connect_banking_class.mainloop()

            opt_pop_out_button = tk.Button(root, text='       Pop Out      ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=pop_out__,
                                           activebackground='#3d3d3d')
            opt_pop_out_button.pack()
            opt_pop_out_button.place(x=0, y=90)
            opt_pop_out_button.bind('<Enter>', func=lambda e: opt_pop_out_button.config(bg='#3d3d3d'))
            opt_pop_out_button.bind('<Leave>', func=lambda e: opt_pop_out_button.config(bg='#1c1c1c'))

            def exit__():
                response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
                if response is True:
                    import sys
                    sys.exit()

            opt_exit_button = tk.Button(root, text='           Exit          ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=exit__,
                                        activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=120)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

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

        def get_calendar(*args):
            self.get_calendar_func()

        self.wn.bind('<Return>', get_calendar)

        def get_today(*args):
            self.get_today_function()

        self.wn.bind('<Control-t>', get_today)

        def refresh__(*args):
            refresh()

        def return_home__(*args):
            return_home()

        def exit__fn(*args):
            self.on_closing()

        def pop_out__fn(*args):
            self.pop_out()

        def back__fn(*args):
            self.go_back()

        self.wn.bind('<Control-r>', refresh__)
        self.wn.bind('<Alt-h>', return_home__)
        self.wn.bind('<Control-e>', exit__fn)
        self.wn.bind('<Control-p>', pop_out__fn)
        self.wn.bind('<Control-b>', back__fn)

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

    def get_calendar_func(self):

        try:
            month__get = self.months_dropdown.get()
            year__get = self.years_dropdown.get()

            self.__month__ = months_names_to_values[month__get]
            self.__year__ = int(year__get)

            self.__month_calendar__ = (calendar.month(int(year__get), months_names_to_values[month__get]))
            self.label.configure(text=self.__month_calendar__)

        except ValueError:
            pass
        except KeyError:
            pass

        pass

    def get_today_function(self):
        date = datetime.date.today()

        self.__today__ = datetime.datetime.strptime(str(date), '%Y-%m-%d')
        self.__month__ = self.__today__.month
        self.__year__ = self.__today__.year
        self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))

        self.label.configure(text=self.__month_calendar__)

    def go_back(self):
        self.wn.destroy()

        from main_directory.banking_class import Banking
        connect_banking_class = Banking(self.name, self.card)
        connect_banking_class.mainloop()

    def pop_out(self):
        from main_directory.Calendar__reg__utils__ import value_list

        if len(value_list) == 0:
            if len(check_list) == 0:

                value_list.append(1)
                check_list.append(1)

                self.wn.destroy()

                from main_directory.BankingPopOutCalendar__reg__sub__utils__ import BankingPopOutCalendar

                def run_banking_pop_out_calendar():
                    app = BankingPopOutCalendar(self.name, self.card)
                    app.run()

                self.wn.after(10, lambda: run_banking_pop_out_calendar())

                from main_directory.banking_class import Banking
                connect_banking_class = Banking(self.name, self.card)
                connect_banking_class.mainloop()

    def on_closing(self):

        if messagebox.askokcancel("Quit", "Do you want to quit?") is True:
            self.wn.destroy()
            import sys
            sys.exit()

    def usr_exit_request(self):

        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            self.wn.destroy()
            import sys
            sys.exit()

    def run(self):

        self.wn.mainloop()
