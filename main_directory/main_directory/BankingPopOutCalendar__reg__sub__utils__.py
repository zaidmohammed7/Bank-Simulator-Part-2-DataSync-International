import calendar
import datetime
import tkinter as tk


class BankingPopOutCalendar:

    def __init__(self, name, card):
        self.name = name
        self.card = card

        super().__init__()

        print('\n[ INFO ] Tkinter [ Tkinter     ] : Calendar [ pop_out     ] loaded successfully')

        self.wn2 = tk.Tk()
        self.wn2.title('Calendar')
        self.wn2.geometry("+50+40")
        self.wn2.geometry('300x300')
        self.wn2.config(bg='#bab197')
        self.wn2.resizable(False, False)
        try:
            self.wn2.iconbitmap(r'..\main_directory\ico1.ico')
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        self.wn2.focus_force()

        date = datetime.date.today()
        self.__today__ = datetime.datetime.strptime(str(date), '%Y-%m-%d')
        self.__month__ = self.__today__.month
        self.__year__ = self.__today__.year
        self.__month_calendar__ = (calendar.month(self.__year__, self.__month__))

        self.label = tk.Label(self.wn2, text=self.__month_calendar__, bg='#bab197', font=('Courier New', '15'), anchor='w', justify='left')
        self.label.pack()

        __date__ = datetime.datetime.now()
        date_in_words = __date__.strftime('%A %d %B %Y')

        self.date_ = tk.Label(self.wn2, text=('Today: ' + str(date_in_words)), font=('Georgia', '12'), bg='#bab197', fg='black')
        self.date_.pack()
        self.date_.place(x=5, y=200)

        self.NEXT_BTN = tk.Button(self.wn2, text=' > ', command=self.next_function, bg='#9c8f6b', activebackground='#bab197', relief=tk.FLAT)
        self.NEXT_BTN.pack()
        self.NEXT_BTN.place(x=270, y=270)
        self.NEXT_BTN.bind('<Enter>', func=lambda e: self.NEXT_BTN.configure(bg='#baaa7f'))
        self.NEXT_BTN.bind('<Leave>', func=lambda e: self.NEXT_BTN.configure(bg='#9c8f6b'))

        self.PREV_BTN2 = tk.Button(self.wn2, text=' < ', command=self.prev_function, bg='#9c8f6b', activebackground='#bab197', relief=tk.FLAT)
        self.PREV_BTN2.pack()
        self.PREV_BTN2.place(x=10, y=270)
        self.PREV_BTN2.bind('<Enter>', func=lambda e: self.PREV_BTN2.configure(bg='#baaa7f'))
        self.PREV_BTN2.bind('<Leave>', func=lambda e: self.PREV_BTN2.configure(bg='#9c8f6b'))

        self.wn2.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.TODAY_CALENDAR = tk.Button(self.wn2, text=' Today ', relief=tk.FLAT, bg='#9c8f6b', font=('Calibre', '10'), command=self.get_today_function, activebackground='#bab197')
        self.TODAY_CALENDAR.pack()
        self.TODAY_CALENDAR.place(x=120, y=268)
        self.TODAY_CALENDAR.bind('<Enter>', func=lambda e: self.TODAY_CALENDAR.configure(bg='#baaa7f'))
        self.TODAY_CALENDAR.bind('<Leave>', func=lambda e: self.TODAY_CALENDAR.configure(bg='#9c8f6b'))

        def next_fn(*args):
            self.next_function()

        self.wn2.bind('<Right>', next_fn)

        def prev_fn(*args):
            self.prev_function()

        self.wn2.bind('<Left>', prev_fn)

        def today_fn(*args):
            self.get_today_function()

        self.wn2.bind('<Control-t>', today_fn)

        def right_button_press(*args):
            start_option_pane()

        def start_option_pane(*args):
            root = tk.Tk()
            root.overrideredirect(True)
            root.config(bg='#1c1c1c')

            abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
            abs_coord_y = root.winfo_pointery() - root.winfo_rooty()

            root.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root.geometry("100x58")

            def exit__():
                from main_directory.Calendar__reg__utils__ import value_list
                from main_directory.Banking_Calendar__reg__sub__utils__ import check_list
                from main_directory.HomeWindow import PopOutCalender_HOME
                from main_directory.LoginWindow import PopOutCalender_LOGIN
                from main_directory.SignupWindow import PopOutCalender_SIGNUP
                from main_directory.DeleteWindow import PopOutCalender_DELETE
                from main_directory.DocumentationWindow import PopOutCalender_DOCUMENTATION

                value_list.clear()
                check_list.clear()
                PopOutCalender_HOME.clear()
                PopOutCalender_LOGIN.clear()
                PopOutCalender_SIGNUP.clear()
                PopOutCalender_DELETE.clear()
                PopOutCalender_DOCUMENTATION.clear()

                root.destroy()
                self.wn2.destroy()

            def refresh__():
                from main_directory.refresh_windows_functions_file import refresh_banking_pop_up_calendar__utils__
                self.wn2.destroy()
                root.destroy()
                refresh_banking_pop_up_calendar__utils__(self.name, self.card)

            opt_refresh_button = tk.Button(root, text='       Refresh       ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=refresh__, activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=0)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_exit_button = tk.Button(root, text='           Exit          ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=exit__, activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=30)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            def left_button_press(*args):
                try:
                    root.destroy()
                except tk.TclError:
                    pass

            self.wn2.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.wn2.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.wn2.bind('<Button-3>', start_option_pane)

        def exit_(*args):
            self.on_closing()

        def refresh(*args):
            from main_directory.refresh_windows_functions_file import refresh_pop_up_calendar__utils__
            self.wn2.destroy()
            refresh_pop_up_calendar__utils__()

        self.wn2.bind('<Control-e>', exit_)
        self.wn2.bind('<Control-r>', refresh)

    def on_closing(self):

        from main_directory.Calendar__reg__utils__ import value_list
        from main_directory.Banking_Calendar__reg__sub__utils__ import check_list
        from main_directory.HomeWindow import PopOutCalender_HOME
        from main_directory.LoginWindow import PopOutCalender_LOGIN
        from main_directory.SignupWindow import PopOutCalender_SIGNUP
        from main_directory.DeleteWindow import PopOutCalender_DELETE
        from main_directory.DocumentationWindow import PopOutCalender_DOCUMENTATION

        value_list.clear()
        check_list.clear()
        PopOutCalender_HOME.clear()
        PopOutCalender_LOGIN.clear()
        PopOutCalender_SIGNUP.clear()
        PopOutCalender_DELETE.clear()
        PopOutCalender_DOCUMENTATION.clear()

        self.wn2.destroy()

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

    def run(self):

        self.wn2.mainloop()
