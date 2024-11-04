import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import time
import datetime
import threading
import sys

from main_directory.open_windows import open_windows_list
from main_directory.refresh_windows_functions_file import refresh_change_pin_window
from main_directory.card_number import hash_pin
from main_directory.password_functions_file import loading


class ChangePin:
    def __init__(self, username, name):
        self.username = username
        self.name = name
        super(ChangePin, self).__init__()

        self.change_pin_wn = tk.Tk()
        self.change_pin_wn.title("Change Pin")
        self.change_pin_wn.focus_force()
        self.change_pin_wn.config(bg='#66ffaf')
        self.change_pin_wn.resizable(False, False)
        try:
            self.change_pin_wn.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic1.png"))

            self.img_lb = tk.Label(self.change_pin_wn, image=self.image1, borderwidth=0)
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
        ws = self.change_pin_wn.winfo_screenwidth()  # width of the screen
        hs = self.change_pin_wn.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        y = y - 30

        # set the dimensions of the screen
        # and where it is placed
        self.change_pin_wn.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________

        heading = tk.Label(self.change_pin_wn, text='Change Pin',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=300, y=75)

        # _________________________design - start________________________________

        label1 = tk.Label(self.change_pin_wn, text='',
                          bg='#127544',
                          width=6,
                          height=50,
                          font=('Georgia', '13'))
        label1.pack()
        label1.place(x=0, y=70)

        label2 = tk.Label(self.change_pin_wn, text='',
                          bg='#127544',
                          width=150,
                          height=2,
                          font=('Georgia', '20'))
        label2.pack()
        label2.place(x=0, y=0)

        # _________________________design - end___________________________________

        # _________________time module display -start___________credit: stack_overflow

        clock = tk.Label(self.change_pin_wn,
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
        date_label = tk.Label(self.change_pin_wn,
                              text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                              bg='#127544',
                              fg='white',
                              font=('Georgia', '10'))
        date_label.pack()
        date_label.place(x=590, y=0)

        # ________________________date display - end_____________________________

        # _____________________initial_window_setup_completed____________________

        def go_back():
            self.change_pin_wn.destroy()
            from main_directory.account_window import account_window
            account_window(self.username, self.name)

        self.go_back_button = tk.Button(self.change_pin_wn,
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
            self.change_pin_wn.destroy()
            refresh_change_pin_window(self.username, self.name)

        self.refresh_label = tk.Label(self.change_pin_wn, text='',
                                      bg='#66ffaf',
                                      font=('Georgia', '12'))
        self.refresh_label.pack()
        self.refresh_label.place(x=70, y=95)

        self.refresh_button = tk.Button(self.change_pin_wn, text='     \n     ♻      \n     ',
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
            self.change_pin_wn.destroy()
            open_windows_list.clear()
            from main_directory.HomeWindow import home
            home()

        self.home_label = tk.Label(self.change_pin_wn, text='',
                                   bg='#66ffaf',
                                   font=('Georgia', '12'))
        self.home_label.pack()
        self.home_label.place(x=70, y=155)

        self.home_button = tk.Button(self.change_pin_wn, text='     \n  Home  \n     ',
                                     bg='#127544',
                                     activeforeground='white',
                                     activebackground='#3b785a',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=return_home,
                                     font=('Georgia', '10'))
        self.home_button.pack()
        self.home_button.place(x=2, y=140)
        self.home_button.bind('<Enter>', func=lambda e: (self.home_button.config(bg='#66ffaf', fg='black'), self.home_label.config(text='   Home    ', bg='#127544', fg='white')))
        self.home_button.bind('<Leave>', func=lambda e: (self.home_button.config(bg='#127544', fg='white'), self.home_label.config(text='', bg='#66ffaf')))

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.change_pin_wn.destroy()
                sys.exit()

        self.change_pin_wn.protocol("WM_DELETE_WINDOW", on_closing)

        self.exit_button = tk.Button(self.change_pin_wn, text='     \n    Exit    \n     ',
                                     bg='#127544',
                                     activeforeground='white',
                                     activebackground='maroon',
                                     fg='white',
                                     relief=tk.FLAT,
                                     command=self.usr_exit_request,
                                     font=('Georgia', '10'))
        self.exit_button.pack()
        self.exit_button.place(x=2, y=537)
        self.exit_button.bind('<Enter>', func=lambda e: self.exit_button.config(bg='#ff0314'))
        self.exit_button.bind('<Leave>', func=lambda e: self.exit_button.config(bg='#127544'))

        # ______________________________ labels - Start _________________________________________

        self.old_pin_label = tk.Label(self.change_pin_wn,
                                      bg='#66ffaf',
                                      text="Enter current pin  :",
                                      font=('aerial', '12'))
        self.old_pin_label.pack()
        self.old_pin_label.place(x=150, y=200)

        self.old_pin_input = ttk.Entry(self.change_pin_wn,
                                       show='*',
                                       width=40,
                                       font=('aerial', '12'))
        self.old_pin_input.pack()
        self.old_pin_input.place(x=350, y=200)
        self.old_pin_input.focus_force()

        def hide_pin():
            old_pin____.config(command=show_pin, text=' ○ ')
            self.old_pin_input.configure(show='*')
            pass

        def show_pin():
            old_pin____.config(command=hide_pin, text=' — ')
            self.old_pin_input.configure(show='')
            pass

        old_pin____ = tk.Button(self.change_pin_wn,
                                text=' ○ ',
                                command=show_pin,
                                relief=tk.FLAT,
                                bg='#66ffaf')
        old_pin____.pack()
        old_pin____.place(x=740, y=200)

        self.old_pin_check = tk.Label(self.change_pin_wn,
                                      text='',
                                      bg='#66ffaf')
        self.old_pin_check.pack()
        self.old_pin_check.place(x=650, y=230)

        self.new_pin_label = tk.Label(self.change_pin_wn,
                                      bg='#66ffaf',
                                      text="Enter new pin       :",
                                      font=('aerial', '12'))
        self.new_pin_label.pack()
        self.new_pin_label.place(x=150, y=300)

        self.new_pin_input = ttk.Entry(self.change_pin_wn,
                                       show='*',
                                       width=40,
                                       font=('aerial', '12'))
        self.new_pin_input.pack()
        self.new_pin_input.place(x=350, y=300)

        def hide_pin2():
            new_pin____.config(command=show_pin2, text=' ○ ')
            self.new_pin_input.configure(show='*')
            pass

        def show_pin2():
            new_pin____.config(command=hide_pin2, text=' — ')
            self.new_pin_input.configure(show='')
            pass

        new_pin____ = tk.Button(self.change_pin_wn,
                                text=' ○ ',
                                command=show_pin2,
                                relief=tk.FLAT,
                                bg='#66ffaf')
        new_pin____.pack()
        new_pin____.place(x=740, y=300)

        self.new_pin_label2 = tk.Label(self.change_pin_wn,
                                       bg='#66ffaf',
                                       text="Renter new pin     :",
                                       font=('aerial', '12'))
        self.new_pin_label2.pack()
        self.new_pin_label2.place(x=150, y=350)

        self.new_pin_input2 = ttk.Entry(self.change_pin_wn,
                                        show='*',
                                        width=40,
                                        font=('aerial', '12'))
        self.new_pin_input2.pack()
        self.new_pin_input2.place(x=350, y=350)

        def hide_pin3():
            new_pin___2.config(command=show_pin3, text=' ○ ')
            self.new_pin_input2.configure(show='*')
            pass

        def show_pin3():
            new_pin___2.config(command=hide_pin3, text=' — ')
            self.new_pin_input2.configure(show='')
            pass

        new_pin___2 = tk.Button(self.change_pin_wn,
                                text=' ○ ',
                                command=show_pin3,
                                relief=tk.FLAT,
                                bg='#66ffaf')
        new_pin___2.pack()
        new_pin___2.place(x=740, y=350)

        def go_to_next_blank(*args):
            if len(self.old_pin_input.get()) != 0:
                self.new_pin_input.focus_force()
            if len(self.old_pin_input.get()) != 0 and len(self.new_pin_input.get()) != 0:
                self.new_pin_input2.focus_force()
            if len(self.old_pin_input.get()) != 0 and len(self.new_pin_input.get()) != 0 and len(self.new_pin_input2.get()) != 0:
                self.submit()

        self.change_pin_wn.bind('<Return>', go_to_next_blank)

        self.submit_button = tk.Button(self.change_pin_wn, text='     Submit     ',
                                       bg='#364f44',
                                       activeforeground='black',
                                       activebackground='#364f44',
                                       fg='white',
                                       relief=tk.FLAT,
                                       command=self.submit,
                                       font=('Georgia', '10'))
        self.submit_button.pack()
        self.submit_button.place(x=370, y=460)
        self.submit_button.bind('<Enter>', func=lambda e: self.submit_button.config(bg='#547a6a'))
        self.submit_button.bind('<Leave>', func=lambda e: self.submit_button.config(bg='#364f44'))

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

            self.change_pin_wn.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.change_pin_wn.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.change_pin_wn.bind('<Button-3>', start_option_menu)

        def back_fn(*args):
            go_back()

        def refresh_fn(*args):
            refresh()

        def return_home_fn(*args):
            return_home()

        def exit_fn(*args):
            on_closing()

        self.change_pin_wn.bind('<Control-b>', back_fn)
        self.change_pin_wn.bind('<Control-r>', refresh_fn)
        self.change_pin_wn.bind('<Alt-h>', return_home_fn)
        self.change_pin_wn.bind('<Control-e>', exit_fn)

    def run(self):
        self.change_pin_wn.mainloop()

    def usr_exit_request(self):
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            self.change_pin_wn.destroy()
            sys.exit()

    def submit(self):

        old_pin = self.old_pin_input.get()
        old_pin = old_pin.lstrip().rstrip()

        if len(old_pin) != 4:
            if not old_pin.isdigit():
                messagebox.showerror(title='Pin Error', message='Enter a valid Pin')

            elif 4 > len(old_pin) > 0:
                messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number\nThe given pin number has less than 4 characters')

            elif len(old_pin) > 4:
                messagebox.showerror(title='Pin Number Error', message='Enter a valid pin number\nThe given pin number has more than 4 characters')

            elif len(old_pin) == 0:
                messagebox.showerror(title='Pin Error', message='Enter a valid Pin')

        else:
            if not old_pin.isdigit():
                messagebox.showerror(title='Pin Error', message='Enter a valid Pin')

            else:

                import mysql.connector as mysql

                __object__ = threading.Thread(target=loading, daemon=True)
                __object__.start()

                final_pin = hash_pin(old_pin)

                connection = mysql.connect(host='localhost',
                                           user='root',
                                           password='dpsbn',
                                           database='client_db')

                if connection.is_connected() is True:
                    cur = connection.cursor()
                    cur.execute(f"SELECT * FROM client WHERE PIN_NUMBER = '{final_pin}' AND USERNAME = '{self.username}'")

                    result = cur.fetchall()
                    cur.close()

                    if len(result) != 0:
                        self.old_pin_check.config(text='your pin is correct', fg='black')

                        new_pin = self.new_pin_input.get()
                        new_pin = new_pin.lstrip().rstrip()

                        if len(new_pin) == 4:

                            if new_pin.isdigit():

                                confirm_pin = self.new_pin_input2.get()
                                confirm_pin = confirm_pin.lstrip().rstrip()

                                if new_pin == confirm_pin:
                                    __object__ = threading.Thread(target=loading, daemon=True)
                                    __object__.start()

                                    new_final_pin = hash_pin(confirm_pin)
                                    cur2 = connection.cursor()
                                    cur2.execute(f"UPDATE client SET PIN_NUMBER = '{new_final_pin}' WHERE USERNAME = '{self.username}'")
                                    cur2.close()

                                    connection.commit()
                                    connection.close()

                                    self.change_pin_wn.destroy()
                                    from operation_functions_pyfiles import pin_update_successful
                                    pin_update_successful()
                                    pass
                                else:
                                    messagebox.showerror(title='New Pin error', message='Pin numbers don\'t match')
                            else:
                                messagebox.showerror(title='New Pin error', message='Pin should be numbers only')

                            pass

                        else:
                            if not new_pin.isdigit():
                                messagebox.showerror(title='New Pin Error', message='Enter a valid Pin')

                            elif 4 > len(new_pin) > 0:
                                messagebox.showerror(title='New Pin Number Error', message='Enter a valid pin number\nThe given pin number has less than 4 characters')

                            elif len(new_pin) > 4:
                                messagebox.showerror(title='New Pin Number Error', message='Enter a valid pin number\nThe given pin number has more than 4 characters')

                            elif len(new_pin) == 0:
                                messagebox.showerror(title='New Pin Error', message='Enter a valid Pin')

                    else:
                        self.old_pin_check.config(text='incorrect pin', fg='red')
                        messagebox.showerror(title='Pin error', message='The pin is incorrect')

                else:
                    messagebox.showerror(title='Server Error', message='The server crashed')
