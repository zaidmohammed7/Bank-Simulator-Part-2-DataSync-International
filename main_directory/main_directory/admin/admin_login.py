import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import datetime
import sys
import threading


class AdminLogin:
    def __init__(self):
        super(AdminLogin, self).__init__()

        self.root = tk.Tk()
        self.root.title("Admin Login")
        self.root.focus_force()
        self.root.config(bg='#66ffaf')
        self.root.resizable(False, False)
        try:
            self.root.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\al.png"))

            self.img_lb = tk.Label(self.root, image=self.image1, borderwidth=0)
            self.img_lb.pack()
            self.img_lb.place(x=0, y=0)
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        # ______________fixing window on screen__________credit: stack_overflow

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
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        #
        # heading = tk.Label(self.root, text='Admin Login',
        #                    bg='#66ffaf',
        #                    font=('Georgia', '40'))
        # heading.pack()
        # heading.place(x=280, y=75)

        # _________________________design - start________________________________

        label1 = tk.Label(self.root, text='',
                          bg='#127544',
                          width=6,
                          height=50,
                          font=('Georgia', '13'))
        label1.pack()
        label1.place(x=0, y=70)

        label2 = tk.Label(self.root, text='',
                          bg='#127544',
                          width=150,
                          height=2,
                          font=('Georgia', '20'))
        label2.pack()
        label2.place(x=0, y=0)

        # _________________________design - end___________________________________

        # _________________time module display -start___________credit: stack_overflow

        clock = tk.Label(self.root,
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
        date_label = tk.Label(self.root,
                              text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                              bg='#127544',
                              fg='white',
                              font=('Georgia', '10'))
        date_label.pack()
        date_label.place(x=590, y=0)

        # ________________________date display - end_____________________________

        REMOTE_SERVER = "one.one.one.one"
        mode = tk.Label(self.root, text='', bg='#127544', font=('Helvetica', '10'))
        mode.pack()
        mode.place(x=510, y=0)

        def mode_function():
            from main_directory.connection import is_connected as connection

            check_connection = connection(REMOTE_SERVER)

            if check_connection is True:
                mode.config(fg='#34eb43', text='ONLINE')
                mode.after(5000, mode_function)
            else:
                mode.config(fg='#ff0000', text='OFFLINE')
                mode.after(5000, mode_function)

        threading.Thread(target=mode_function, daemon=True).start()

        # _____________________initial_window_setup_completed____________________

        def go_back():
            self.root.destroy()
            from main_directory.LoginWindow import login
            login()

        go_back_button = tk.Button(self.root,
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
            self.root.destroy()
            from main_directory.refresh_windows_functions_file import refresh_admin_login
            refresh_admin_login()

        refresh_label = tk.Label(self.root, text='',
                                 bg='#06140C',
                                 font=('Georgia', '12'),
                                 borderwidth=0)
        refresh_label.pack()
        refresh_label.place(x=70, y=95)

        refresh_button = tk.Button(self.root, text='     \n     ♻      \n     ',
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
        refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#127544', fg='white'), refresh_label.config(text='', bg='#06140C')))

        def return_home():
            self.root.destroy()
            from main_directory.open_windows import open_windows_list
            open_windows_list.clear()
            from main_directory.HomeWindow import home
            home()

        home_label = tk.Label(self.root, text='',
                              bg='#06140C',
                              font=('Georgia', '12'),
                              borderwidth=0)
        home_label.pack()
        home_label.place(x=70, y=155)

        home_button = tk.Button(self.root, text='     \n  Home  \n     ',
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
        home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#127544', fg='white'), home_label.config(text='', bg='#06140C')))

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                sys.exit()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        exit_button = tk.Button(self.root, text='     \n    Exit    \n     ',
                                bg='#127544',
                                activeforeground='white',
                                activebackground='maroon',
                                fg='white',
                                relief=tk.FLAT,
                                command=on_closing,
                                font=('Georgia', '10'))
        exit_button.pack()
        exit_button.place(x=2, y=537)
        exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
        exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#127544'))

        # lw_display_username_field_label = tk.Label(self.root,
        #                                            bg='#66ffaf',
        #                                            text="Enter your username  :",
        #                                            font=('aerial', '12'))
        # lw_display_username_field_label.pack()
        # lw_display_username_field_label.place(x=150, y=200)

        self.lw_input_username_field_entry_box = ttk.Entry(self.root,
                                                           width=25,
                                                           font=('aerial', '12'))
        self.lw_input_username_field_entry_box.pack()
        self.lw_input_username_field_entry_box.place(x=460, y=300)

        self.lw_input_username_field_entry_box.focus_force()

        self.username_check = tk.Label(self.root, text='',
                                       fg='black', bg='#06140C',
                                       borderwidth=0)
        self.username_check.pack()
        self.username_check.place(x=650, y=328)

        # __________________________________________ password 1 field  _________________________________________

        # lw_display_password1_field_label = tk.Label(self.root,
        #                                             bg='#66ffaf',
        #                                             text="Enter your password  :",
        #                                             font=('aerial', '12'))
        # lw_display_password1_field_label.pack()
        # lw_display_password1_field_label.place(x=150, y=300)

        self.lw_input_password1_field_entry_box = ttk.Entry(self.root,
                                                            show='*',
                                                            width=25,
                                                            font=('aerial', '12'))
        self.lw_input_password1_field_entry_box.pack()
        self.lw_input_password1_field_entry_box.place(x=460, y=371)

        def hide_pwd():
            pin___label.config(command=show_pwd, text=' ○ ')
            self.lw_input_password1_field_entry_box.configure(show='*')
            pass

        def show_pwd():
            pin___label.config(command=hide_pwd, text=' — ')
            self.lw_input_password1_field_entry_box.configure(show='')
            pass

        pin___label = tk.Button(self.root,
                                text=' ○ ',
                                command=show_pwd,
                                relief=tk.FLAT,
                                bg='#364f44',
                                fg='white',
                                borderwidth=0)
        pin___label.pack()
        pin___label.place(x=720, y=371)

        self.password_check__ = tk.Label(self.root, text='',
                                         fg='black', bg='#171B16', justify='left',
                                         borderwidth=0)
        self.password_check__.pack()
        self.password_check__.place(x=600, y=395)

        # ______________________________________ security pin field #12345 ______________________

        # security_pin_label = tk.Label(self.root,
        #                               bg='#66ffaf',
        #                               text="Enter your security pin  :",
        #                               font=('aerial', '12'))
        # security_pin_label.pack()
        # security_pin_label.place(x=150, y=400)

        self.security_pin_input = ttk.Entry(self.root,
                                            show='*',
                                            width=25,
                                            font=('aerial', '12'))
        self.security_pin_input.pack()
        self.security_pin_input.place(x=460, y=448)

        def hide_pwd2():
            pin___label2.config(command=show_pwd2, text=' ○ ')
            self.security_pin_input.configure(show='*')
            pass

        def show_pwd2():
            pin___label2.config(command=hide_pwd2, text=' — ')
            self.security_pin_input.configure(show='')
            pass

        pin___label2 = tk.Button(self.root,
                                 text=' ○ ',
                                 command=show_pwd2,
                                 relief=tk.FLAT,
                                 bg='#364f44',
                                 fg='white',
                                 borderwidth=0)
        pin___label2.pack()
        pin___label2.place(x=720, y=448)

        def go_to_next_textbox(*args):
            if len(self.lw_input_username_field_entry_box.get()) != 0:
                self.lw_input_password1_field_entry_box.focus_force()
            if len(self.lw_input_username_field_entry_box.get()) != 0 and len(self.lw_input_password1_field_entry_box.get()) != 0:
                self.security_pin_input.focus_force()
            if len(self.lw_input_username_field_entry_box.get()) != 0 and len(self.lw_input_password1_field_entry_box.get()) != 0 and len(self.security_pin_input.get()) != 0:
                self.submit()

        self.root.bind('<Return>', go_to_next_textbox)

        submit_button = tk.Button(self.root, text='\n     Submit     \n',
                                  bg='#364f44',
                                  activeforeground='white',
                                  activebackground='#364f44',
                                  fg='white',
                                  relief=tk.FLAT,
                                  command=self.submit,
                                  font=('Georgia', '10'))
        submit_button.pack()
        submit_button.place(x=530, y=530)
        submit_button.bind('<Enter>', func=lambda e: submit_button.config(bg='#547a6a'))
        submit_button.bind('<Leave>', func=lambda e: submit_button.config(bg='#364f44'))

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

            self.root.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.root.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.root.bind('<Button-3>', start_option_menu)

        def back_fn(*args):
            go_back()

        def refresh_fn(*args):
            refresh()

        def return_home_fn(*args):
            return_home()

        def exit_fn(*args):
            on_closing()

        self.root.bind('<Control-b>', back_fn)
        self.root.bind('<Control-r>', refresh_fn)
        self.root.bind('<Alt-h>', return_home_fn)
        self.root.bind('<Control-e>', exit_fn)

    def run(self):
        self.root.mainloop()

    def submit(self):
        username = self.lw_input_username_field_entry_box.get()
        username = username.lstrip().rstrip()

        password = self.lw_input_password1_field_entry_box.get()
        password = password.lstrip().rstrip()

        security_pin = self.security_pin_input.get()
        security_pin = security_pin.lstrip().rstrip()

        if len(username) == 0:
            messagebox.showerror(title='Username Error', message='Enter a valid username')

        else:

            if len(password) == 0:
                messagebox.showerror(title='Password Error', message='Enter a valid password')

            else:

                if len(security_pin) == 0:
                    messagebox.showerror(title='Security Error', message='Enter a valid security pin')

                else:

                    import mysql.connector as sql

                    connection = sql.connect(host='localhost',
                                             user='root',
                                             password='dpsbn',
                                             database='admin_db')
                    if connection.is_connected():
                        cur = connection.cursor()
                        cur.execute(f"SELECT PASSWORD_SALT FROM administrators WHERE USERNAME = '{username}'")
                        salt = cur.fetchall()
                        cur.close()
                        if len(salt) != 0:
                            self.username_check.config(text='')
                            salt_ = salt[0][0]
                            from main_directory.password_functions_file import hash_password
                            from main_directory.card_number import hash_pin
                            from main_directory.password_functions_file import loading

                            __object__1 = threading.Thread(target=loading, daemon=True)
                            __object__1.start()

                            final_password = hash_password(salt_, password)

                            __object__2 = threading.Thread(target=loading, daemon=True)
                            __object__2.start()

                            final_security_pin = hash_pin(security_pin)

                            cur2 = connection.cursor()
                            cur2.execute(f"SELECT NAME FROM administrators WHERE USERNAME='{username}' AND PASSWORD = '{final_password}' AND SECURITY_KEY = '{final_security_pin}'")
                            result = cur2.fetchall()
                            cur2.close()
                            if len(result) != 0:
                                self.password_check__.config(text='', fg='black')
                                name = result[0][0]

                                def notify(title='DataSync Intl', message='You have logged in successfully!'):
                                    from plyer import notification
                                    notification.notify(title, message, timeout=5)

                                __object___ = threading.Thread(target=notify)
                                __object___.start()

                                self.root.destroy()
                                from main_directory.admin.admin_account import AdminAccount
                                AdminAccount(name).run()

                            else:
                                self.password_check__.config(text='incorrect credentials\neither password or security code \nis incorrect', fg='red')
                                messagebox.showerror(title='Security error', message='Data not found')
                            pass
                        else:
                            self.username_check.config(text='username not found', fg='red')
                            messagebox.showerror(title='Username error', message='Data not found')
                    else:
                        messagebox.showerror(title='Server error', message='Server connection lost')
