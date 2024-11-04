import threading
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import datetime
import sys


class AdminAccount:

    def __init__(self, name):
        self.name = name
        super(AdminAccount, self).__init__()

        self.root = tk.Tk()
        self.root.title(f"{name.title()}'s Account - Administrator")
        self.root.focus_force()
        self.root.config(bg='#66ffaf')
        self.root.resizable(False, False)
        try:
            self.root.iconbitmap(r"..\main_directory\ico1.ico")

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic1.png"))

            self.img_lb = tk.Label(self.root, image=self.image1, borderwidth=0)
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

        heading = tk.Label(self.root, text='Admin Account',
                           bg='#66ffaf',
                           font=('Georgia', '40'))
        heading.pack()
        heading.place(x=250, y=75)

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
            from main_directory.connection import is_connected as connection_

            check_connection = connection_(REMOTE_SERVER)

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
            from main_directory.admin.admin_login import AdminLogin
            wn = AdminLogin()
            wn.run()

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

        refresh_label = tk.Label(self.root, text='',
                                 bg='#66ffaf',
                                 font=('Georgia', '12'))
        refresh_label.pack()
        refresh_label.place(x=70, y=95)

        refresh_button = tk.Button(self.root, text='     \n     ♻      \n     ',
                                   bg='#127544',
                                   activeforeground='white',
                                   activebackground='#3b785a',
                                   relief=tk.FLAT,
                                   fg='white',
                                   command=self.refresh,
                                   font=('Georgia', '10'))
        refresh_button.pack()
        refresh_button.place(x=2, y=75)
        refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#66ffaf', fg='black'), refresh_label.config(text='   Refresh    ', bg='#127544', fg='white')))
        refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#127544', fg='white'), refresh_label.config(text='', bg='#66ffaf')))

        def return_home():
            self.root.destroy()
            from main_directory.open_windows import open_windows_list
            open_windows_list.clear()
            from main_directory.HomeWindow import home
            home()

        home_label = tk.Label(self.root, text='',
                              bg='#66ffaf',
                              font=('Georgia', '12'))
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
        home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#127544', fg='white'), home_label.config(text='', bg='#66ffaf')))

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

        self.block_card_label = tk.Label(self.root,
                                         bg='#66ffaf',
                                         text="Enter card number ",
                                         font=('Helvetica', '14'))
        self.block_card_label.pack()
        self.block_card_label.place(x=500, y=150)

        self.block_card_input = ttk.Entry(self.root,
                                          width=30,
                                          font=('Helvetica', '12'))
        self.block_card_input.pack()
        self.block_card_input.place(x=504, y=190)

        self.unblock_card_label = tk.Label(self.root,
                                           bg='#66ffaf',
                                           text="Enter card number ",
                                           font=('Helvetica', '14'))
        self.unblock_card_label.pack()
        self.unblock_card_label.place(x=500, y=300)

        self.unblock_card_input = ttk.Entry(self.root,
                                            width=30,
                                            font=('Helvetica', '12'))
        self.unblock_card_input.pack()
        self.unblock_card_input.place(x=504, y=340)

        self.delete_card_label = tk.Label(self.root,
                                          bg='#66ffaf',
                                          text="Enter card number ",
                                          font=('Helvetica', '14'))
        self.delete_card_label.pack()
        self.delete_card_label.place(x=500, y=450)

        self.delete_card_input = ttk.Entry(self.root,
                                           width=30,
                                           font=('Helvetica', '12'))
        self.delete_card_input.pack()
        self.delete_card_input.place(x=504, y=490)

        self.show_info_label = tk.Label(self.root,
                                        bg='#66ffaf',
                                        text="Enter card number ",
                                        font=('Helvetica', '14'))
        self.show_info_label.pack()
        self.show_info_label.place(x=150, y=450)

        self.show_info_input = ttk.Entry(self.root,
                                         width=28,
                                         font=('Helvetica', '12'))
        self.show_info_input.pack()
        self.show_info_input.place(x=150, y=490)

        self.show_info_input.focus_force()

        # _______________________ buttons ________________________

        block = tk.Button(self.root, text=' Hard Block (Administrator Rights) ',
                          bg='#364f44',
                          activeforeground='white',
                          activebackground='#364f44',
                          fg='white',
                          relief=tk.FLAT,
                          command=self.block,
                          font=('Georgia', '10'))
        block.pack()
        block.place(x=504, y=220)
        block.bind('<Enter>', func=lambda e: block.config(bg='#547a6a'))
        block.bind('<Leave>', func=lambda e: block.config(bg='#364f44'))

        s_block = tk.Button(self.root, text='  Secure-Temp Block (User Rights)   ',
                          bg='#364f44',
                          activeforeground='white',
                          activebackground='#364f44',
                          fg='white',
                          relief=tk.FLAT,
                          command=self.temp_block,
                          font=('Georgia', '10'))
        s_block.pack()
        s_block.place(x=504, y=250)
        s_block.bind('<Enter>', func=lambda e: s_block.config(bg='#547a6a'))
        s_block.bind('<Leave>', func=lambda e: s_block.config(bg='#364f44'))

        unblock = tk.Button(self.root, text='    Unblock (Administrator Rights)    ',
                            bg='#364f44',
                            activeforeground='white',
                            activebackground='#364f44',
                            fg='white',
                            relief=tk.FLAT,
                            command=self.unblock,
                            font=('Georgia', '10'))
        unblock.pack()
        unblock.place(x=504, y=370)
        unblock.bind('<Enter>', func=lambda e: unblock.config(bg='#547a6a'))
        unblock.bind('<Leave>', func=lambda e: unblock.config(bg='#364f44'))

        delete_ = tk.Button(self.root, text='      Delete (Administrator Rights)       ',
                            bg='#364f44',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            relief=tk.FLAT,
                            command=self.delete,
                            font=('Georgia', '10'))
        delete_.pack()
        delete_.place(x=504, y=520)
        delete_.bind('<Enter>', func=lambda e: delete_.config(bg='#ff0314'))
        delete_.bind('<Leave>', func=lambda e: delete_.config(bg='#364f44'))

        show_info = tk.Button(self.root, text='       Show Info      ',
                              bg='#364f44',
                              activeforeground='white',
                              activebackground='#364f44',
                              fg='white',
                              relief=tk.FLAT,
                              command=self.show_info_,
                              font=('Georgia', '10'))
        show_info.pack()
        show_info.place(x=150, y=520)
        show_info.bind('<Enter>', func=lambda e: show_info.config(bg='#547a6a'))
        show_info.bind('<Leave>', func=lambda e: show_info.config(bg='#364f44'))

        clear_tb_eb = tk.Button(self.root, text='           Clear         ',
                                bg='#364f44',
                                activeforeground='white',
                                activebackground='#364f44',
                                fg='white',
                                relief=tk.FLAT,
                                command=self.clear_info_,
                                font=('Georgia', '10'))
        clear_tb_eb.pack()
        clear_tb_eb.place(x=300, y=520)
        clear_tb_eb.bind('<Enter>', func=lambda e: clear_tb_eb.config(bg='#547a6a'))
        clear_tb_eb.bind('<Leave>', func=lambda e: clear_tb_eb.config(bg='#364f44'))

        self.text_box = tk.Text(self.root,
                                width=25,
                                height=15,
                                bg='#ebebeb',
                                wrap=tk.WORD,
                                font=('Courier New', '12'))
        self.text_box.pack()
        self.text_box.place(x=150, y=200)
        self.text_box.configure(state=tk.DISABLED)

        self.SCROLL_BAR = tk.Scrollbar(self.text_box, cursor='hand2')
        self.SCROLL_BAR.pack()
        self.SCROLL_BAR.place(relheight=1, relx=0.974)

        self.text_box.config(yscrollcommand=self.SCROLL_BAR.set)
        self.SCROLL_BAR.config(command=self.text_box.yview)

        import mysql.connector as sql
        connection = sql.connect(host='localhost',
                                 user='root',
                                 password='dpsbn',
                                 database='client_db')

        if connection.is_connected() is True:
            c = connection.cursor()
            c.execute("""SELECT COUNT(*) FROM client""")
            r = c.fetchall()

            l1 = tk.Label(self.root,
                          bg='#66ffaf',
                          text=f"Number of users: {r[0][0]} ",
                          font=('Georgia', '14'))
            l1.pack()
            l1.place(x=150, y=150)

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
                self.refresh()

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
            self.refresh()

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

    def refresh(self):
        self.root.destroy()
        from main_directory.refresh_windows_functions_file import refresh_admin_account
        refresh_admin_account(self.name)

    def temp_block(self):
        card_number = self.block_card_input.get()
        card_number = card_number.lstrip().rstrip()

        if len(card_number) != 16:

            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            elif 16 > len(card_number) > 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

            elif len(card_number) > 16:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

            elif len(card_number) == 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

        else:
            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            else:
                import mysql.connector as sql
                connection = sql.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')

                if connection.is_connected() is True:
                    cur = connection.cursor()
                    cur.execute(f"SELECT NAME FROM client WHERE CARD_NUMBER='{card_number}'")
                    result = cur.fetchall()
                    cur.close()

                    if len(result) != 0:
                        name = result[0][0]

                        cur_ = connection.cursor()
                        cur_.execute(f"SELECT CARD_NUMBER_IN_USE_PERMISSION FROM client WHERE CARD_NUMBER='{card_number}'")
                        check = cur_.fetchall()
                        if check[0][0] == 'None':
                            messagebox.showerror(title='Hard Block error', message='Card is hard-blocked by the administrator')
                        elif check[0][0] == 'False':
                            messagebox.showerror(title='Secure-Temp Block error', message='Card is already blocked')
                        else:

                            response = messagebox.askokcancel(title='Security Alert', message=f"Secure (Temporary) Block {name}'s account?")
                            if response is True:

                                cur2 = connection.cursor()
                                cur2.execute(f"UPDATE client SET CARD_NUMBER_IN_USE_PERMISSION = 'False' WHERE CARD_NUMBER='{card_number}'")
                                cur2.close()

                                connection.commit()
                                connection.close()

                                messagebox.showinfo(title='Alert!', message='Card Secure blocked')

                                self.refresh()
                    else:
                        messagebox.showerror(title='Card Number error', message='Data not found')

    def block(self):
        card_number = self.block_card_input.get()
        card_number = card_number.lstrip().rstrip()

        if len(card_number) != 16:

            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            elif 16 > len(card_number) > 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

            elif len(card_number) > 16:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

            elif len(card_number) == 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

        else:
            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            else:

                import mysql.connector as sql
                connection = sql.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')

                if connection.is_connected() is True:
                    cur = connection.cursor()
                    cur.execute(f"SELECT NAME FROM client WHERE CARD_NUMBER='{card_number}'")
                    result = cur.fetchall()
                    cur.close()

                    if len(result) != 0:
                        name = result[0][0]

                        cur_ = connection.cursor()
                        cur_.execute(f"SELECT CARD_NUMBER_IN_USE_PERMISSION FROM client WHERE CARD_NUMBER='{card_number}'")
                        check = cur_.fetchall()
                        if check[0][0] == 'None':
                            messagebox.showerror(title='Card Number error', message='Card is already blocked')
                        else:

                            response = messagebox.askokcancel(title='Security Alert', message=f"Block {name}'s account?")
                            if response is True:

                                cur2 = connection.cursor()
                                cur2.execute(f"UPDATE client SET CARD_NUMBER_IN_USE_PERMISSION = 'None' WHERE CARD_NUMBER='{card_number}'")
                                cur2.close()

                                connection.commit()
                                connection.close()

                                messagebox.showinfo(title='Alert!', message='Card blocked')

                                self.refresh()

                    else:
                        messagebox.showerror(title='Card Number error', message='Data not found')

    def unblock(self):

        card_number = self.unblock_card_input.get()
        card_number = card_number.lstrip().rstrip()

        if len(card_number) != 16:

            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            elif 16 > len(card_number) > 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

            elif len(card_number) > 16:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

            elif len(card_number) == 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

        else:
            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            else:

                import mysql.connector as sql
                connection = sql.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')

                if connection.is_connected() is True:
                    cur = connection.cursor()
                    cur.execute(f"SELECT NAME FROM client WHERE CARD_NUMBER='{card_number}'")
                    result = cur.fetchall()
                    cur.close()

                    if len(result) != 0:
                        name = result[0][0]

                        cur_ = connection.cursor()
                        cur_.execute(f"SELECT CARD_NUMBER_IN_USE_PERMISSION FROM client WHERE CARD_NUMBER='{card_number}'")
                        check = cur_.fetchall()
                        if check[0][0] == 'True':
                            messagebox.showerror(title='Card Number error', message='Card is already unblocked')
                        elif check[0][0] == 'False':
                            messagebox.showerror(title='Card Number error', message='Card is not blocked by the administrator')
                        else:
                            response = messagebox.askokcancel(title='Security Alert', message=f"Unblock {name}'s account?")
                            if response is True:
                                cur2 = connection.cursor()
                                cur2.execute(f"UPDATE client SET CARD_NUMBER_IN_USE_PERMISSION = 'True' WHERE CARD_NUMBER='{card_number}'")
                                cur2.close()

                                connection.commit()
                                connection.close()

                                messagebox.showinfo(title='Alert!', message='Card unblocked')

                                self.refresh()

                    else:
                        messagebox.showerror(title='Card Number error', message='Data not found')

    def delete(self):
        card_number = self.delete_card_input.get()
        card_number = card_number.lstrip().rstrip()

        if len(card_number) != 16:

            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            elif 16 > len(card_number) > 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

            elif len(card_number) > 16:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

            elif len(card_number) == 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

        else:
            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            else:

                import mysql.connector as sql
                connection = sql.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')

                if connection.is_connected() is True:
                    cur = connection.cursor()
                    cur.execute(f"SELECT NAME FROM client WHERE CARD_NUMBER='{card_number}'")
                    result = cur.fetchall()
                    cur.close()

                    if len(result) != 0:
                        name = result[0][0]
                        response = messagebox.askokcancel(title='Security Alert', message=f"Delete {name}'s account?")
                        if response is True:
                            cur2 = connection.cursor()
                            cur2.execute(f"DELETE FROM client WHERE CARD_NUMBER = '{card_number}'")
                            cur2.close()

                            connection.commit()
                            connection.close()

                            messagebox.showinfo(title='Alert!', message='Card deleted')

                            self.refresh()

                        pass
                    else:
                        messagebox.showerror(title='Card Number error', message='Data not found')

    def show_info_(self):
        card_number = self.show_info_input.get()
        card_number = card_number.lstrip().rstrip()

        if len(card_number) != 16:

            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            elif 16 > len(card_number) > 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has less than 16 characters')

            elif len(card_number) > 16:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number\nThe given card number has more than 16 characters')

            elif len(card_number) == 0:
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

        else:

            if not card_number.isdigit():
                messagebox.showerror(title='Card Number Error', message='Enter a valid card number')

            else:

                import mysql.connector as sql
                connection = sql.connect(host='localhost',
                                         user='root',
                                         password='dpsbn',
                                         database='client_db')

                if connection.is_connected() is True:
                    cur = connection.cursor()
                    cur.execute(f"SELECT NAME, EMAIL, USERNAME, PHONE, BALANCE, TRANSFERS, DEPOSITS, WITHDRAWALS FROM client WHERE CARD_NUMBER = '{card_number}'")
                    result = cur.fetchall()
                    cur.close()

                    if len(result) != 0:
                        name = result[0][0]
                        email = result[0][1]
                        username = result[0][2]
                        phone = result[0][3]
                        balance = result[0][4]
                        transfers = result[0][5]
                        deposits = result[0][6]
                        withdrawals = result[0][7]

                        info = f"\nNAME:  {name} \n\nEMAIL:  {email} \n\nUSERNAME:  {username} \n\nPHONE:  {phone} \n\nBALANCE:  {balance} \n\nTRANSFERS:  {transfers} \n\nDEPOSITS:  {deposits} \n\nWITHDRAWALS: {withdrawals}"

                        self.text_box.configure(state=tk.NORMAL)
                        self.text_box.delete(1.0, tk.END)
                        self.text_box.insert(tk.END, info)
                        self.text_box.configure(state=tk.DISABLED)
                    else:
                        messagebox.showerror(title='Card Number error', message='Data not found')

    def clear_info_(self):
        self.text_box.configure(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        self.text_box.configure(state=tk.DISABLED)
        self.show_info_input.delete(0, tk.END)
