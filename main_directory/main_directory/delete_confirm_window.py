import threading
import tkinter as tk
from tkinter import messagebox
from main_directory.open_windows import open_windows_list
from main_directory.refresh_windows_functions_file import del_win_refresh_registry

REMOTE_SERVER = "one.one.one.one"


def del_confirm(username, name, user_email):
    root = tk.Tk()
    root.title(f"{name.title()}'s Account")
    root.focus_force()
    root.config(bg='#eb6a6a')
    root.resizable(False, False)
    try:
        root.iconbitmap(r'..\main_directory\ico1.ico')
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    label1 = tk.Label(root, text='',
                      bg='#690a1d',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    # ______________fixing window on screen__________credit: stack_overflow

    w = 550  # width for the Tk root
    h = 260  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # login_window.geometry("800x600")

    # _________________fixing window on screen_END___________________________

    # mode
    mode0 = tk.Label(root, text='                     ', bg='#690a1d', font=('Helvetica', '10'))
    mode0.pack()
    mode0.place(x=480, y=0)

    mode = tk.Label(root, text='', bg='#690a1d', font=('Helvetica', '10'))
    mode.pack()
    mode.place(x=480, y=0)

    def mode_function():
        from connection import is_connected as connection

        check_connection = connection(REMOTE_SERVER)

        if check_connection is True:
            mode.config(fg='#34eb43', text='ONLINE')
            mode.after(5000, mode_function)
        else:
            mode.config(fg='#dea9a9', text='OFFLINE')
            mode.after(5000, mode_function)

    threading.Thread(target=mode_function, daemon=True).start()

    text = tk.Label(root, text='Do you want to delete your account?',
                    bg='#eb6a6a',
                    font=('Georgia', '21'))
    text.pack()
    text.place(x=70, y=100)

    def go_back():
        root.destroy()
        from main_directory.DeleteWindow import delete
        delete()

    go_back_button = tk.Button(root,
                               text="  Back  ",
                               bg='#690a1d',
                               relief=tk.FLAT,
                               activeforeground='white',
                               activebackground='#9e4a65',
                               fg='white',
                               command=go_back,
                               font=('Georgia', '10'))
    go_back_button.pack()
    go_back_button.place(x=5, y=20)
    go_back_button.bind('<Enter>', func=lambda e: go_back_button.config(bg='#c73e53', fg='black'))
    go_back_button.bind('<Leave>', func=lambda e: go_back_button.config(bg='#690a1d', fg='white'))

    def yes():
        from main_directory.client_database import delete_account
        root.destroy()

        from connection import is_connected

        check_connection = is_connected(REMOTE_SERVER)

        if check_connection is True:

            import yagmail
            import random
            import mysql.connector as sql
            characters = '1234567890'
            chr2 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

            n1 = random.choice(characters)
            n2 = random.choice(characters)
            n3 = random.choice(characters)
            n4 = random.choice(characters)
            n5 = random.choice(characters)
            n6 = random.choice(characters)
            n7 = random.choice(characters)
            n8 = random.choice(chr2)
            n9 = random.choice(chr2)
            n1_ = random.choice(characters)
            n2_ = random.choice(characters)
            n3_ = random.choice(characters)
            n8_ = random.choice(chr2)
            n9_ = random.choice(chr2)

            ref_id = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n1_ + n2_ + n3_ + n8_ + n9_

            server_connection = sql.connect(host='localhost',
                                            user='root',
                                            password='dpsbn',
                                            database='dsi_gmail')

            server_cursor = server_connection.cursor()
            server_cursor.execute("""SELECT emailid, pwd FROM company_gmail where emailid='{}'""".format('datasyncinternational@gmail.com'))
            result = server_cursor.fetchall()
            server_cursor.close()

            connection = sql.connect(host='localhost',
                                     user='root',
                                     password='dpsbn',
                                     database='client_db')

            new_conn = connection.cursor()
            new_conn.execute(f"SELECT NAME, EMAIL FROM client WHERE USERNAME = '{username}'")
            new_conn_result = new_conn.fetchall()

            final_name = new_conn_result[0][0]
            final_email = new_conn_result[0][1]

            server_email = result[0][0]
            server_pwd = result[0][1]

            msg = """Hello user, DataSync International is committed to the security and integrity of your credentials and hence, by the laws of the land, certain procedures can be time-consuming. 
            It's noticed that you have decided to delete your bank account. However, due to security reasons, you cannot alone carry out this. It is to notify you that deleting an account from the app ONLY DISABLES YOUR ACCOUNT for 6 months. However, if you want to disable your account briefly, here are some requirements for doing the same:
            -> your account balance should be null
            -> you are not supposed to have any pending loans
            Once you have disabled your account, your reference id shall be sent to you shortly and you are requested to visit your bank branch within the 6 months with the required documents such as a recent photo-id (Aadhar), bank checkbook, etc as mentioned in the bank sop website.

            We wish the best for your future. Happy banking with DataSync International!"""

            yag = yagmail.SMTP(server_email, server_pwd)
            yag.send(f"{final_email}", 'Verification', f"Hello {final_name}\n\nHere is your reference id: {ref_id}\n\nDO NOT SHARE THIS\n\n\nIt is unfortunate to see that you are disabling your account.\nHowever, this method DOES NOT deletes your bank account.\nDo visit the bank soon\n🙂 :)\n\n\n\nRegards\nTeam DSI\n\n\n{msg}")

            delete_account(username)

        else:
            messagebox.showerror(title="Connection error", message="You are not connected to the internet")
            delete_account(username)

    def go_to_delete():
        root.destroy()
        from main_directory.DeleteWindow import delete
        delete()

    def no():
        messagebox.showinfo(title="Alert!", message="You have not deleted your account")
        go_to_delete()

    yes_button = tk.Button(root, text='     YES     ',
                           bg='#690a1d',
                           activeforeground='black',
                           activebackground='#c73e53',
                           fg='white',
                           relief=tk.FLAT,
                           command=yes,
                           font=('Georgia', '10'))
    yes_button.pack()
    yes_button.place(x=100, y=200)
    yes_button.bind('<Enter>', func=lambda e: yes_button.config(bg='#961b2e', fg='white'))
    yes_button.bind('<Leave>', func=lambda e: yes_button.config(bg='#690a1d', fg='white'))

    no_button = tk.Button(root, text='     NO     ',
                          bg='#690a1d',
                          activeforeground='black',
                          activebackground='#c73e53',
                          fg='white',
                          relief=tk.FLAT,
                          command=no,
                          font=('Georgia', '10'))
    no_button.pack()
    no_button.place(x=400, y=200)
    no_button.bind('<Enter>', func=lambda e: no_button.config(bg='#961b2e', fg='white'))
    no_button.bind('<Leave>', func=lambda e: no_button.config(bg='#690a1d', fg='white'))

    def refresh():
        root.destroy()
        del_win_refresh_registry(username, name, user_email)

    refresh_label = tk.Label(root, text='',
                             bg='#eb6a6a',
                             font=('Georgia', '12'))
    refresh_label.pack()
    refresh_label.place(x=70, y=95)

    refresh_button = tk.Button(root, text='     \n     ♻      \n     ',
                               bg='#690a1d',
                               activeforeground='white',
                               activebackground='#9e4a65',
                               relief=tk.FLAT,
                               fg='white',
                               command=refresh,
                               font=('Georgia', '10'))
    refresh_button.pack()
    refresh_button.place(x=2, y=75)
    refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#eb6a6a', fg='black'), refresh_label.config(text='   Refresh    ', bg='#690a1d', fg='white')))
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#690a1d', fg='white'), refresh_label.config(text='', bg='#eb6a6a', fg='white')))

    def return_home():
        root.destroy()
        open_windows_list.clear()
        from main_directory.HomeWindow import home
        home()

    home_label = tk.Label(root, text='',
                          bg='#eb6a6a',
                          font=('Georgia', '12'))
    home_label.pack()
    home_label.place(x=70, y=155)

    home_button = tk.Button(root, text='     \n  Home  \n     ',
                            bg='#690a1d',
                            activeforeground='white',
                            activebackground='#9e4a65',
                            relief=tk.FLAT,
                            fg='white',
                            command=return_home,
                            font=('Georgia', '10'))
    home_button.pack()
    home_button.place(x=2, y=140)
    home_button.bind('<Enter>', func=lambda e: (home_button.config(bg='#eb6a6a', fg='black'), home_label.config(text='   Home    ', bg='#690a1d', fg='white')))
    home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#690a1d', fg='white'), home_label.config(text='', bg='#eb6a6a', fg='white')))

    class OptionPane:
        def __init__(self):
            super(OptionPane, self).__init__()
            self.options_pane = tk.Tk()
            self.options_pane.overrideredirect(True)
            self.options_pane.config(bg='#1c1c1c')

            abs_coord_x = self.options_pane.winfo_pointerx() - self.options_pane.winfo_rootx()
            abs_coord_y = self.options_pane.winfo_pointery() - self.options_pane.winfo_rooty()
            self.options_pane.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_pane.geometry("100x88")

            opt_back_button = tk.Button(self.options_pane,
                                        text='         Back           ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.__go_back__,
                                        activebackground='#3d3d3d')
            opt_back_button.pack()
            opt_back_button.place(x=0, y=0)
            opt_back_button.bind('<Enter>', func=lambda e: opt_back_button.config(bg='#3d3d3d'))
            opt_back_button.bind('<Leave>', func=lambda e: opt_back_button.config(bg='#1c1c1c'))

            opt_refresh_button = tk.Button(self.options_pane,
                                           text='       Refresh       ',
                                           relief=tk.FLAT,
                                           font=('Georgia', '10'),
                                           bg='#1c1c1c',
                                           fg='white',
                                           command=self.refresh__,
                                           activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=30)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_home_button = tk.Button(self.options_pane,
                                        text=' Return Home     ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.return_home__,
                                        activebackground='#3d3d3d')
            opt_home_button.pack()
            opt_home_button.place(x=0, y=60)
            opt_home_button.bind('<Enter>', func=lambda e: opt_home_button.config(bg='#3d3d3d'))
            opt_home_button.bind('<Leave>', func=lambda e: opt_home_button.config(bg='#1c1c1c'))

            root.bind('<Button-1>', self.left_button_options__home)
            root.bind('<Button-3>', self.right_button_options__home)

            self.options_pane.after(5000, lambda: self.options_pane.destroy())

        def run(self):
            self.options_pane.mainloop()

        def refresh__(self):
            self.options_pane.destroy()
            refresh()

        def return_home__(self):
            self.options_pane.destroy()
            return_home()

        def __go_back__(self):
            self.options_pane.destroy()
            go_back()

        def left_button_options__home(self, *args):
            try:
                self.options_pane.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_pane.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

    def relaunch_options_pane():
        options_pane = OptionPane()
        options_pane.run()

    def right_button_options__home(*args):
        options_pane = OptionPane()
        options_pane.run()

    root.bind('<Button-3>', right_button_options__home)

    def refresh_fn(*args):
        refresh()

    def return_home_fn(*args):
        return_home()

    def go_back_fn(*args):
        go_back()

    def yes_fn(*args):
        yes()

    def no_fn(*args):
        no()

    root.bind('<Control-r>', refresh_fn)
    root.bind('<Alt-h>', return_home_fn)
    root.bind('<Control-y>', yes_fn)
    root.bind('<Control-n>', no_fn)
    root.bind('<Control-b>', go_back_fn)

    root.protocol("WM_DELETE_WINDOW", go_to_delete)

    root.mainloop()
