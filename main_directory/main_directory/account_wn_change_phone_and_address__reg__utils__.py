import threading
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import time
import datetime
import sys

from main_directory.open_windows import open_windows_list
from main_directory.country_codes_file import country_codes


class ChangePhoneAndAddress:

    def __init__(self, username, name):

        self.username = username
        self.name = name

        super(ChangePhoneAndAddress, self).__init__()

        self.window = tk.Tk()
        self.window.title("Change Phone and Address")
        self.window.focus_force()
        self.window.config(bg='#66ffaf')
        self.window.resizable(False, False)
        try:
            self.window.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic1.png"))

            self.img_lb = tk.Label(self.window, image=self.image1, borderwidth=0)
            self.img_lb.pack()
            self.img_lb.place(x=0, y=500)
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        # ______________fixing window on screen__________credit: stack_overflow

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
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________

        heading = tk.Label(self.window, text='Change Phone And Address',
                           bg='#66ffaf',
                           font=('Georgia', '35'))
        heading.pack()
        heading.place(x=110, y=75)

        # _________________________design - start________________________________

        label1 = tk.Label(self.window, text='',
                          bg='#127544',
                          width=6,
                          height=50,
                          font=('Georgia', '13'))
        label1.pack()
        label1.place(x=0, y=70)

        label2 = tk.Label(self.window, text='',
                          bg='#127544',
                          width=150,
                          height=2,
                          font=('Georgia', '20'))
        label2.pack()
        label2.place(x=0, y=0)

        # _________________________design - end___________________________________

        # _________________time module display -start___________credit: stack_overflow

        clock = tk.Label(self.window,
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
        date_label = tk.Label(self.window,
                              text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                              bg='#127544',
                              fg='white',
                              font=('Georgia', '10'))
        date_label.pack()
        date_label.place(x=590, y=0)

        # ________________________date display - end_____________________________

        # _____________________initial_window_setup_completed____________________

        def go_back():
            self.window.destroy()
            from main_directory.account_window import account_window
            account_window(self.username, self.name)

        self.go_back_button = tk.Button(self.window,
                                        text="  Back  ",
                                        bg='#127544',
                                        relief=tk.FLAT,
                                        activeforeground='white',
                                        activebackground='#3b785a',
                                        fg='white',
                                        command=go_back,
                                        font=('Georgia', '10'))
        self.go_back_button.pack()
        self.go_back_button.place(x=5, y=20)
        self.go_back_button.bind('<Enter>', func=lambda e: self.go_back_button.config(bg='#66ffaf', fg='black'))
        self.go_back_button.bind('<Leave>', func=lambda e: self.go_back_button.config(bg='#127544', fg='white'))

        def refresh():
            self.window.destroy()
            from main_directory.refresh_windows_functions_file import refresh_phone_and_address_window
            refresh_phone_and_address_window(self.username, self.name)

        self.refresh_label = tk.Label(self.window, text='',
                                      bg='#66ffaf',
                                      font=('Georgia', '12'))
        self.refresh_label.pack()
        self.refresh_label.place(x=70, y=95)

        self.refresh_button = tk.Button(self.window, text='     \n     ♻      \n     ',
                                        bg='#127544',
                                        activeforeground='white',
                                        activebackground='#3b785a',
                                        relief=tk.FLAT,
                                        fg='white',
                                        command=refresh,
                                        font=('Georgia', '10'))
        self.refresh_button.pack()
        self.refresh_button.place(x=2, y=75)
        self.refresh_button.bind('<Enter>', func=lambda e: (self.refresh_button.config(bg='#66ffaf', fg='black'), self.refresh_label.config(text='   Refresh    ', bg='#127544', fg='white')))
        self.refresh_button.bind('<Leave>', func=lambda e: (self.refresh_button.config(bg='#127544', fg='white'), self.refresh_label.config(text='', bg='#66ffaf')))

        def return_home():
            self.window.destroy()
            open_windows_list.clear()
            from main_directory.HomeWindow import home
            home()

        home_label = tk.Label(self.window, text='',
                              bg='#66ffaf',
                              font=('Georgia', '12'))
        home_label.pack()
        home_label.place(x=70, y=155)

        home_button = tk.Button(self.window, text='     \n  Home  \n     ',
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
                self.window.destroy()
                sys.exit()

        exit_button = tk.Button(self.window, text='     \n    Exit    \n     ',
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
                self.window.destroy()
                sys.exit()

        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        self.clicked = tk.StringVar()
        self.clicked.set("91::")
        self.drop = ttk.Combobox(self.window, textvariable=self.clicked, state='readonly', width=5, font=('aerial', '12'))
        self.drop['values'] = country_codes
        self.drop.pack()
        self.drop.place(x=300, y=200)

        self.sw_display_phone_field_label = tk.Label(self.window,
                                                     bg='#66ffaf',
                                                     text="Enter your phone  :",
                                                     font=('aerial', '12'))
        self.sw_display_phone_field_label.pack()
        self.sw_display_phone_field_label.place(x=140, y=200)

        self.sw_input_phone_field_entry_box = ttk.Entry(self.window,
                                                        width=20,
                                                        font=('aerial', '12'))
        self.sw_input_phone_field_entry_box.pack()
        self.sw_input_phone_field_entry_box.place(x=400, y=200)

        self.sw_input_phone_field_entry_box.focus_force()

        def submit_phone(*args):
            if len(self.sw_input_phone_field_entry_box.get()) != 0:
                self.update_phone()

        self.window.bind('<Return>', submit_phone)

        self.update_phone_button = tk.Button(self.window, text='     Update Phone     ',
                                             bg='#364f44',
                                             activeforeground='black',
                                             activebackground='#364f44',
                                             fg='white',
                                             relief=tk.FLAT,
                                             command=self.update_phone,
                                             font=('Georgia', '10'))
        self.update_phone_button.pack()
        self.update_phone_button.place(x=650, y=200)
        self.update_phone_button.bind('<Enter>', func=lambda e: self.update_phone_button.config(bg='#547a6a'))
        self.update_phone_button.bind('<Leave>', func=lambda e: self.update_phone_button.config(bg='#364f44'))

        # __________________________________________ address1 field  _________________________________________

        self.sw_display_address1_field_label = tk.Label(self.window,
                                                        bg='#66ffaf',
                                                        text="Enter your address  :",
                                                        font=('aerial', '12'))
        self.sw_display_address1_field_label.pack()
        self.sw_display_address1_field_label.place(x=140, y=320)

        self.sw_input_address1_field_entry_box = ttk.Entry(self.window,
                                                           width=40,
                                                           font=('aerial', '12'))
        self.sw_input_address1_field_entry_box.pack()
        self.sw_input_address1_field_entry_box.place(x=350, y=320)

        # __________________________________________ address2 field  _________________________________________

        self.sw_input_address2_field_entry_box = ttk.Entry(self.window,
                                                           width=40,
                                                           font=('aerial', '12'))
        self.sw_input_address2_field_entry_box.pack()
        self.sw_input_address2_field_entry_box.place(x=350, y=350)

        # __________________________________________ address2 field  _________________________________________

        self.sw_input_address3_field_entry_box = ttk.Entry(self.window,
                                                           width=40,
                                                           font=('aerial', '12'))
        self.sw_input_address3_field_entry_box.pack()
        self.sw_input_address3_field_entry_box.place(x=350, y=380)

        def go_to_next(*args):
            if len(self.sw_input_address1_field_entry_box.get()) != 0:
                self.sw_input_address2_field_entry_box.focus_force()
            if len(self.sw_input_address1_field_entry_box.get()) != 0 and len(self.sw_input_address2_field_entry_box.get()) != 0:
                self.sw_input_address3_field_entry_box.focus_force()
            if len(self.sw_input_address1_field_entry_box.get()) != 0 and len(self.sw_input_address2_field_entry_box.get()) != 0 and len(self.sw_input_address3_field_entry_box.get()) != 0:
                self.update_address()

        self.window.bind('<Return>', go_to_next)

        self.update_address_button = tk.Button(self.window, text='     Update address     ',
                                               bg='#364f44',
                                               activeforeground='black',
                                               activebackground='#364f44',
                                               fg='white',
                                               relief=tk.FLAT,
                                               command=self.update_address,
                                               font=('Georgia', '10'))
        self.update_address_button.pack()
        self.update_address_button.place(x=370, y=460)
        self.update_address_button.bind('<Enter>', func=lambda e: self.update_address_button.config(bg='#547a6a'))
        self.update_address_button.bind('<Leave>', func=lambda e: self.update_address_button.config(bg='#364f44'))

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
                root.destroy()
                go_back()

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

            def refresh__():
                root.destroy()
                refresh()

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

            def return_home__():
                root.destroy()
                return_home()

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

    def update_phone(self):
        code = self.clicked.get()
        phone = self.sw_input_phone_field_entry_box.get()
        phone = phone.lstrip().rstrip()
        if len(phone) == 10:

            contains_other_char_phone = False
            for i in phone:
                if not i.isdigit():
                    contains_other_char_phone = True

            if contains_other_char_phone is True:
                messagebox.showerror(title='Phone Number Error', message='Enter numbers only')
            else:
                __phone__ = code + str(phone)

                import mysql.connector as sql

                connection = sql.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')

                if connection.is_connected():
                    cur = connection.cursor()
                    cur.execute(f"SELECT PHONE FROM client WHERE USERNAME = '{self.username}'")
                    result = cur.fetchall()
                    cur.close()

                    original_phone = result[0][0]

                    if original_phone == __phone__:
                        messagebox.showerror(title='Phone error', message='You have entered the same number')

                    else:
                        new_cur = connection.cursor()
                        new_cur.execute(f"SELECT NAME, PHONE FROM client WHERE PHONE='{__phone__}'")
                        check_phone = new_cur.fetchall()
                        new_cur.close()

                        if len(check_phone) != 0:
                            messagebox.showerror(title='Phone Error', message='Phone already exists\nEnter a valid phone number')

                        else:
                            cur2 = connection.cursor()
                            cur2.execute(f"UPDATE client SET PHONE = '{__phone__}' WHERE USERNAME = '{self.username}'")
                            cur2.close()

                            connection.commit()
                            connection.close()

                            self.window.destroy()
                            from operation_functions_pyfiles import phone_update_successful
                            phone_update_successful()

                else:
                    messagebox.showerror(title='Server Error', message='The server crashed')
        else:
            messagebox.showerror(title='Phone Error', message='Enter a valid phone number')

    def update_address(self):

        address1 = self.sw_input_address1_field_entry_box.get()
        address1 = address1.replace(', ', ' ')
        address1 = address1.replace(',', ' ')
        address1 = address1.lstrip().rstrip()

        address2 = self.sw_input_address2_field_entry_box.get()
        address2 = address2.replace(', ', ' ')
        address2 = address2.replace(',', ' ')
        address2 = address2.lstrip().rstrip()

        address3 = self.sw_input_address3_field_entry_box.get()
        address3 = address3.replace(', ', ' ')
        address3 = address3.replace(',', ' ')
        address3 = address3.lstrip().rstrip()

        address = address1.title() + ' ' + address2.title() + ' ' + address3.title()
        address = address.lstrip().rstrip()

        if len(address) == 0:

            messagebox.showerror(title='Address Error', message='Enter a valid address')

        else:
            final_address = address.title()

            import mysql.connector as sql

            connection = sql.connect(host='localhost',
                                     user='root',
                                     password='dpsbn',
                                     database='client_db')

            if connection.is_connected():
                cur = connection.cursor()
                cur.execute(f"UPDATE client SET ADDRESS = '{final_address}' WHERE USERNAME = '{self.username}'")
                cur.close()

                connection.commit()
                connection.close()

                self.window.destroy()
                from operation_functions_pyfiles import address_update_successful
                address_update_successful()

    def run(self):
        self.window.mainloop()
