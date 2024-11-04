def signup_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have signed up successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Signup Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Signup Successful!',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=20, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def otp(username, name):
    import tkinter as tk
    from tkinter import messagebox
    import random
    import threading
    from main_directory.account_window import account_window

    opt_root = tk.Tk()
    opt_root.title("Login in progress")
    opt_root.focus_force()
    opt_root.config(bg='#f2ea94')
    opt_root.resizable(False, False)
    opt_root.overrideredirect(False)
    opt_root.lift()

    heading = tk.Label(opt_root, text='One Time Password',
                       bg='#f2ea94',
                       font=('aerial', '21'))
    heading.pack()
    heading.place(x=110, y=20)

    # ______________fixing window on screen__________credit: stack_overflow

    w = 470  # width for the Tk root
    h = 300  # height for the Tk root

    # get screen width and height
    ws = opt_root.winfo_screenwidth()  # width of the screen
    hs = opt_root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    opt_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    characters = '1234567890'

    n1 = random.choice(characters)
    n2 = random.choice(characters)
    n3 = random.choice(characters)
    n4 = random.choice(characters)
    n5 = random.choice(characters)
    n6 = random.choice(characters)
    n7 = random.choice(characters)

    __otp__ = n1 + n2 + n3 + n4 + n5 + n6 + n7

    display = tk.Label(opt_root, text=f'Enter {__otp__} below',
                       bg='#f2ea94',
                       font=('Georgia', '15'))
    display.pack()
    display.place(x=140, y=100)

    def notify(title='DataSync Intl', message='You have logged in successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=5)

    def call_login():
        from main_directory.LoginWindow import login
        login()

    def verify():
        user_input = entry_box.get()
        if user_input.isdigit():
            if len(user_input) == 7:
                if user_input == __otp__:
                    opt_root.destroy()
                    __object__ = threading.Thread(target=notify)
                    __object__.start()
                    account_window(username, name)
                    pass

                else:
                    messagebox.showerror(title='Input Error', message='No matching values')
                    opt_root.destroy()
                    call_login()

            else:
                messagebox.showerror(title='Input Error', message='Enter correct number of digits')
                opt_root.destroy()
                call_login()
            pass
        else:
            messagebox.showerror(title='Input Error', message='Enter numbers only!')
            opt_root.destroy()
            call_login()

    entry_box = tk.Entry(opt_root,
                         width=10,
                         bg='#ffffff',
                         font=('aerial', '25'))
    entry_box.pack()
    entry_box.place(x=145, y=150)

    entry_box.focus_force()

    def call_verify(*args):
        verify()

    opt_root.bind('<Return>', call_verify)

    check = tk.Button(opt_root,
                      text='     Verify     ',
                      bg='#deb82f',
                      activeforeground='black',
                      activebackground='#bf9d22',
                      fg='black',
                      relief=tk.FLAT,
                      command=verify,
                      font=('Georgia', '10'))
    check.pack()
    check.place(x=200, y=250)
    check.bind('<Enter>', func=lambda e: check.config(bg='#a89552'))
    check.bind('<Leave>', func=lambda e: check.config(bg='#deb82f'))

    def on_closing():
        opt_root.destroy()
        call_login()

    opt_root.protocol("WM_DELETE_WINDOW", on_closing)

    opt_root.mainloop()


def del_otp(username, name, user_email):
    import tkinter as tk
    from tkinter import messagebox
    import random
    from main_directory.delete_confirm_window import del_confirm

    opt_root = tk.Tk()
    opt_root.title("Deletion in progress")
    opt_root.focus_force()
    opt_root.config(bg='#f2ea94')
    opt_root.resizable(False, False)
    opt_root.overrideredirect(False)
    opt_root.lift()

    heading = tk.Label(opt_root, text='One Time Password',
                       bg='#f2ea94',
                       font=('aerial', '21'))
    heading.pack()
    heading.place(x=110, y=20)

    # ______________fixing window on screen__________credit: stack_overflow

    w = 470  # width for the Tk root
    h = 300  # height for the Tk root

    # get screen width and height
    ws = opt_root.winfo_screenwidth()  # width of the screen
    hs = opt_root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    opt_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    characters = '1234567890'

    n1 = random.choice(characters)
    n2 = random.choice(characters)
    n3 = random.choice(characters)
    n4 = random.choice(characters)
    n5 = random.choice(characters)
    n6 = random.choice(characters)
    n7 = random.choice(characters)

    __otp__ = n1 + n2 + n3 + n4 + n5 + n6 + n7

    display = tk.Label(opt_root, text=f'Enter {__otp__} below',
                       bg='#f2ea94',
                       font=('Georgia', '15'))
    display.pack()
    display.place(x=140, y=100)

    def call_delete():
        from main_directory.DeleteWindow import delete
        delete()

    def verify():
        user_input = entry_box.get()
        if user_input.isdigit():
            if len(user_input) == 7:
                if user_input == __otp__:
                    opt_root.destroy()
                    del_confirm(username, name, user_email)
                    pass

                else:
                    messagebox.showerror(title='Input Error', message='No matching values')
                    opt_root.destroy()
                    call_delete()

            else:
                messagebox.showerror(title='Input Error', message='Enter correct number of digits')
                opt_root.destroy()
                call_delete()
            pass
        else:
            messagebox.showerror(title='Input Error', message='Enter numbers only!')
            opt_root.destroy()
            call_delete()

    entry_box = tk.Entry(opt_root,
                         width=10,
                         bg='#ffffff',
                         font=('aerial', '25'))
    entry_box.pack()
    entry_box.place(x=145, y=150)

    entry_box.focus_force()

    def call_verify(*args):
        verify()

    opt_root.bind('<Return>', call_verify)

    check = tk.Button(opt_root,
                      text='     Verify     ',
                      bg='#deb82f',
                      activeforeground='black',
                      activebackground='#bf9d22',
                      fg='black',
                      relief=tk.FLAT,
                      command=verify,
                      font=('Georgia', '10'))
    check.pack()
    check.place(x=200, y=250)
    check.bind('<Enter>', func=lambda e: check.config(bg='#a89552'))
    check.bind('<Leave>', func=lambda e: check.config(bg='#deb82f'))

    def on_closing():
        opt_root.destroy()
        call_delete()

    opt_root.protocol("WM_DELETE_WINDOW", on_closing)

    opt_root.mainloop()


def delete_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have deleted your account successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Deletion Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Deletion Successful',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=0, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def card_otp(name, card):
    import tkinter as tk
    from tkinter import messagebox
    import random
    from main_directory.banking_class import Banking

    opt_root = tk.Tk()
    opt_root.title("OTP")
    opt_root.focus_force()
    opt_root.config(bg='#f2ea94')
    opt_root.resizable(False, False)
    opt_root.overrideredirect(False)
    opt_root.lift()

    heading = tk.Label(opt_root, text='One Time Password',
                       bg='#f2ea94',
                       font=('aerial', '21'))
    heading.pack()
    heading.place(x=110, y=20)

    # ______________fixing window on screen__________credit: stack_overflow

    w = 470  # width for the Tk root
    h = 300  # height for the Tk root

    # get screen width and height
    ws = opt_root.winfo_screenwidth()  # width of the screen
    hs = opt_root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    opt_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    characters = '1234567890'

    n1 = random.choice(characters)
    n2 = random.choice(characters)
    n3 = random.choice(characters)
    n4 = random.choice(characters)
    n5 = random.choice(characters)
    n6 = random.choice(characters)
    n7 = random.choice(characters)

    __otp__ = n1 + n2 + n3 + n4 + n5 + n6 + n7

    display = tk.Label(opt_root, text=f'Enter {__otp__} below',
                       bg='#f2ea94',
                       font=('Georgia', '15'))
    display.pack()
    display.place(x=140, y=100)

    def notify(title='DataSync Intl', message='You have logged in successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=5)

    def call_home():
        from main_directory.HomeWindow import home
        home()

    def call_banking(__name__, __card__):
        notify()
        bank_connect = Banking(__name__, __card__)
        bank_connect.mainloop()

    def verify():
        user_input = entry_box.get()
        if user_input.isdigit():
            if len(user_input) == 7:
                if user_input == __otp__:
                    opt_root.destroy()
                    call_banking(name, card)
                    pass

                else:
                    messagebox.showerror(title='Input Error', message='No matching values')
                    opt_root.destroy()
                    call_home()

            else:
                messagebox.showerror(title='Input Error', message='Enter correct number of digits')
                opt_root.destroy()
                call_home()
            pass
        else:
            messagebox.showerror(title='Input Error', message='Enter numbers only!')
            opt_root.destroy()
            call_home()

    entry_box = tk.Entry(opt_root,
                         width=10,
                         bg='#ffffff',
                         font=('aerial', '25'))
    entry_box.pack()
    entry_box.place(x=145, y=150)

    entry_box.focus_force()

    def call_verify(*args):
        verify()

    opt_root.bind('<Return>', call_verify)

    check = tk.Button(opt_root,
                      text='     Verify     ',
                      bg='#deb82f',
                      activeforeground='black',
                      activebackground='#bf9d22',
                      fg='black',
                      relief=tk.FLAT,
                      command=verify,
                      font=('Georgia', '10'))
    check.pack()
    check.place(x=200, y=250)
    check.bind('<Enter>', func=lambda e: check.config(bg='#a89552'))
    check.bind('<Leave>', func=lambda e: check.config(bg='#deb82f'))

    def on_closing():
        opt_root.destroy()
        call_home()

    opt_root.protocol("WM_DELETE_WINDOW", on_closing)

    opt_root.mainloop()


def deposit_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have deposited the amount successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Deposit Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Deposit Successful',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=10, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def transfer_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have transferred the amount successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Transaction Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Transaction Successful',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=10, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 560  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def withdraw_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have withdrawn the amount the amount successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Withdraw Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Withdraw Successful',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=10, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 560  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def pwd_update_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have updated your password successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Update Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Update Successful!',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=20, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def pin_update_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have updated your pin successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Update Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Update Successful!',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=20, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def phone_update_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have updated your phone number successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Update Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Update Successful!',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=20, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()


def address_update_successful():
    from main_directory.HomeWindow import home

    def notify(title='DataSync Intl', message='You have updated your address successfully!'):
        from plyer import notification
        notification.notify(title, message, timeout=10)

    def show_message():
        import tkinter as tk
        import threading
        from main_directory.open_windows import open_windows_list
        open_windows_list.clear()

        __object__ = threading.Thread(target=notify)
        __object__.start()

        root = tk.Tk()
        root.title("Update Successful")
        root.focus_force()
        root.config(bg='#03fca9')
        root.resizable(False, False)
        root.overrideredirect(False)

        heading = tk.Label(root, text='Update Successful!',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=20, y=20)

        # ______________fixing window on screen__________credit: stack_overflow

        w = 470  # width for the Tk root
        h = 100  # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # login_window.geometry("800x600")

        # _________________fixing window on screen_END___________________________
        root.after(3000, lambda: root.destroy())

        root.mainloop()

    show_message()
    home()
