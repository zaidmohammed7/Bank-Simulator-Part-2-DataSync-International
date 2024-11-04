import threading
import tkinter as tk
from tkinter import messagebox
import time
import datetime
import sys

from main_directory.open_windows import open_windows_list
from main_directory.refresh_windows_functions_file import documentation_refresh_registry

PopOutCalender_DOCUMENTATION = []
PopOutChatBox_DOCUMENTATION = []
REMOTE_SERVER = "one.one.one.one"


def documentation():
    print('[ INFO ] Tkinter [ Tkinter     ] : document window loaded successfully')

    documentation_window = tk.Tk()
    documentation_window.focus_force()
    documentation_window.config(bg='#dbdbdb')
    documentation_window.title("Documentation")
    documentation_window.resizable(False, False)
    try:
        documentation_window.iconbitmap(r'..\main_directory\ico1.ico')

        from PIL import ImageTk, Image
        image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic6.png"))

        img_lb = tk.Label(image=image1, borderwidth=0)
        img_lb.pack()
        img_lb.place(x=0, y=0)
    except tk.TclError:
        pass
    except FileNotFoundError:
        pass

    def run_pop_out_calender_doc():

        if len(PopOutCalender_DOCUMENTATION) == 1:
            PopOutCalender_DOCUMENTATION.append(1)

            from PopOutCalendar__reg__utils__ import PopOutCalendar
            app = PopOutCalendar()
            app.run()

    documentation_window.after(10, lambda: run_pop_out_calender_doc())

    def run_pop_out_chat_box_doc():

        if len(PopOutChatBox_DOCUMENTATION) == 1:
            PopOutChatBox_DOCUMENTATION.append(1)

            from PopOutChatBox__reg__utils__ import PopOutChatBox
            app = PopOutChatBox()
            app.run()

    documentation_window.after(10, lambda: run_pop_out_chat_box_doc())

    # ___________________fixing window on screen_START_______credit: stack_overflow

    w = 800  # width for the Tk root
    h = 600  # height for the Tk root

    # get screen width and height
    ws = documentation_window.winfo_screenwidth()  # width of the screen
    hs = documentation_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    y = y - 30

    # set the dimensions of the screen
    # and where it is placed
    documentation_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # home_window.geometry('800x600')

    # _________________fixing window on screen_END___________________________

    # _________________________design - start________________________________

    label1 = tk.Label(documentation_window, text='',
                      bg='#616161',
                      width=6,
                      height=50,
                      font=('Georgia', '13'))
    label1.pack()
    label1.place(x=0, y=70)

    label2 = tk.Label(documentation_window, text='',
                      bg='#616161',
                      width=150,
                      height=2,
                      font=('Georgia', '20'))
    label2.pack()
    label2.place(x=0, y=0)

    # _________________________design - end___________________________________

    # _________________time module display - START___________credit: stack_overflow

    clock = tk.Label(documentation_window,
                     bg='#616161',
                     fg='white',
                     font=('Georgia', '10'))
    clock.pack()
    clock.place(x=720, y=0)

    def tick():  # credit: StackOverflow
        updated_time = time.strftime('%H:%M:%S')
        clock.config(text=updated_time + '   ')
        clock.after(200, tick)

    threading.Thread(target=tick, daemon=True).start()

    # ________________________time display - END_____________________________

    # ________________________date display - START__________credit: stack_overflow

    date = datetime.datetime.now()
    date_label = tk.Label(documentation_window,
                          text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                          bg='#616161',
                          fg='white',
                          font=('Georgia', '10'))
    date_label.pack()
    date_label.place(x=590, y=0)

    # ________________________date display - END_____________________________

    # mode
    mode = tk.Label(text='', bg='#616161', font=('Helvetica', '10'))
    mode.pack()
    mode.place(x=510, y=0)

    def mode_function():
        from connection import is_connected as connection

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
        length = len(open_windows_list)
        element = open_windows_list[length - 1]

        if element == 'home':
            open_windows_list.pop()
            from HomeWindow import home
            documentation_window.destroy()
            home()

        elif element == 'login':
            open_windows_list.pop()
            from LoginWindow import login
            documentation_window.destroy()
            login()

        elif element == 'delete':
            open_windows_list.pop()
            from DeleteWindow import delete
            documentation_window.destroy()
            delete()

        elif element == 'signup':
            open_windows_list.pop()
            from SignupWindow import signup
            documentation_window.destroy()
            signup()

    go_back_button = tk.Button(documentation_window,
                               text="  Back  ",
                               bg='#616161',
                               relief=tk.FLAT,
                               activeforeground='white',
                               activebackground='#545454',
                               fg='white',
                               command=go_back,
                               font=('Georgia', '10'))
    go_back_button.pack()
    go_back_button.place(x=5, y=20)
    go_back_button.bind('<Enter>', func=lambda e: go_back_button.config(bg='#878787'))
    go_back_button.bind('<Leave>', func=lambda e: go_back_button.config(bg='#616161'))

    # _______________________________body___________________________________________

    def usr_exit_request():
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            documentation_window.destroy()
            sys.exit()

    def redirect_to_login_window():
        open_windows_list.append("docs")
        documentation_window.destroy()
        from LoginWindow import login
        login()

    def redirect_to_signup_window():
        open_windows_list.append("docs")
        documentation_window.destroy()
        from SignupWindow import signup
        signup()

    def redirect_to_delete_window():
        open_windows_list.append("docs")
        documentation_window.destroy()
        from DeleteWindow import delete
        delete()

    login_button = tk.Button(documentation_window, text='           Log In           ',
                             bg='#616161',
                             activeforeground='white',
                             activebackground='#545454',
                             fg='white',
                             relief=tk.FLAT,
                             command=redirect_to_login_window,
                             font=('Georgia', '10'))
    login_button.pack()
    login_button.place(x=64, y=20)
    login_button.bind('<Enter>', func=lambda e: login_button.config(bg='#878787'))
    login_button.bind('<Leave>', func=lambda e: login_button.config(bg='#616161'))

    signup_button = tk.Button(documentation_window, text='          Signup          ',
                              bg='#616161',
                              activeforeground='white',
                              activebackground='#545454',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_signup_window,
                              font=('Georgia', '10'))
    signup_button.pack()
    signup_button.place(x=184, y=20)
    signup_button.bind('<Enter>', func=lambda e: signup_button.config(bg='#878787'))
    signup_button.bind('<Leave>', func=lambda e: signup_button.config(bg='#616161'))

    delete_button = tk.Button(documentation_window, text='     Delete Account     ',
                              bg='#616161',
                              activeforeground='white',
                              activebackground='#545454',
                              fg='white',
                              relief=tk.FLAT,
                              command=redirect_to_delete_window,
                              font=('Georgia', '10'))
    delete_button.pack()
    delete_button.place(x=304, y=20)
    delete_button.bind('<Enter>', func=lambda e: delete_button.config(bg='#878787'))
    delete_button.bind('<Leave>', func=lambda e: delete_button.config(bg='#616161'))

    exit_button = tk.Button(documentation_window, text='     \n    Exit    \n     ',
                            bg='#616161',
                            activeforeground='white',
                            activebackground='maroon',
                            fg='white',
                            relief=tk.FLAT,
                            command=usr_exit_request,
                            font=('Georgia', '10'))
    exit_button.pack()
    exit_button.place(x=2, y=537)
    exit_button.bind('<Enter>', func=lambda e: exit_button.config(bg='#ff0314'))
    exit_button.bind('<Leave>', func=lambda e: exit_button.config(bg='#616161'))

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            documentation_window.destroy()
            sys.exit()

    documentation_window.protocol("WM_DELETE_WINDOW", on_closing)

    def refresh():
        documentation_window.destroy()
        documentation_refresh_registry()

    refresh_label = tk.Label(documentation_window, text='',
                             bg='black',
                             font=('Georgia', '12'),
                             borderwidth=0)
    refresh_label.pack()
    refresh_label.place(x=70, y=95)

    refresh_button = tk.Button(documentation_window, text='     \n     ♻      \n     ',
                               bg='#616161',
                               activeforeground='white',
                               activebackground='#787373',
                               relief=tk.FLAT,
                               fg='white',
                               command=refresh,
                               font=('Georgia', '10'))
    refresh_button.pack()
    refresh_button.place(x=2, y=75)
    refresh_button.bind('<Enter>', func=lambda e: (refresh_button.config(bg='#dbdbdb', fg='black'), refresh_label.config(text='   Refresh    ', bg='#616161', fg='white')))
    refresh_button.bind('<Leave>', func=lambda e: (refresh_button.config(bg='#616161', fg='white'), refresh_label.config(text='', bg='black')))

    def return_home():
        documentation_window.destroy()
        open_windows_list.clear()
        from HomeWindow import home
        home()

    home_label = tk.Label(documentation_window, text='',
                          bg='#d5862a',
                          font=('Georgia', '12'))
    home_label.pack()
    home_label.place(x=70, y=155)

    home_button = tk.Button(documentation_window, text='     \n  Home  \n     ',
                            bg='#616161',
                            activeforeground='white',
                            activebackground='#787373',
                            relief=tk.FLAT,
                            fg='white',
                            command=return_home,
                            font=('Georgia', '10'))
    home_button.pack()
    home_button.place(x=2, y=140)
    home_button.bind('<Enter>', func=lambda e: (home_button.config(bg='#dbdbdb', fg='black'), home_label.config(text='   Home    ', bg='#616161', fg='white')))
    home_button.bind('<Leave>', func=lambda e: (home_button.config(bg='#616161', fg='white'), home_label.config(text='', bg='#d5862a')))

    self_chat_box_label = tk.Label(documentation_window, text='',
                                   bg='#d5862a',
                                   font=('Georgia', '12'))
    self_chat_box_label.pack()
    self_chat_box_label.place(x=70, y=420)

    def call_scb():
        open_windows_list.append('docs')
        documentation_window.destroy()
        from ChatBox__reg__utils__ import ChatApplicationWn
        chat_box = ChatApplicationWn()
        chat_box.run()

    self_chat_box_button = tk.Button(documentation_window, text='     \n    Chat   \n     ',
                                     bg='#616161',
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_scb,
                                     font=('Georgia', '10'))
    self_chat_box_button.pack()
    self_chat_box_button.place(x=2, y=400)
    self_chat_box_button.bind('<Enter>', func=lambda e: (self_chat_box_button.config(bg='#dbdbdb', fg='black'), self_chat_box_label.config(text='   Chat Bot   ', bg='#616161', fg='white')))
    self_chat_box_button.bind('<Leave>', func=lambda e: (self_chat_box_button.config(bg='#616161', fg='white'), self_chat_box_label.config(text='', bg='#d5862a')))

    self_calendar_label = tk.Label(documentation_window, text='',
                                   bg='#d5862a',
                                   font=('Georgia', '12'))
    self_calendar_label.pack()
    self_calendar_label.place(x=70, y=350)

    def call_calendar():
        open_windows_list.append('docs')
        documentation_window.destroy()
        from Calendar__reg__utils__ import Calendar
        chat_box = Calendar()
        chat_box.run()

    self_calendar_button = tk.Button(documentation_window, text='     \n       C       \n     ',
                                     bg='#616161',
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=call_calendar,
                                     font=('Georgia', '10'))
    self_calendar_button.pack()
    self_calendar_button.place(x=2, y=330)
    self_calendar_button.bind('<Enter>', func=lambda e: (self_calendar_button.config(bg='#dbdbdb', fg='black'), self_calendar_label.config(text='   Calendar   ', bg='#616161', fg='white')))
    self_calendar_button.bind('<Leave>', func=lambda e: (self_calendar_button.config(bg='#616161', fg='white'), self_calendar_label.config(text='', bg='#d5862a')))

    text_box = tk.Text(documentation_window,
                       width=40,
                       height=17,
                       bg='#ebebeb',
                       wrap=tk.WORD,
                       font=('Georgia', '15'))
    text_box.pack()
    text_box.place(x=190, y=175)
    text_box.configure(state=tk.DISABLED)  # DISABLED

    display_text = """This project has been done by -\nAbhijeet Rajhans \nArmaan Shaikh \nZaid Khan Md. 
    \n\nThis project aims to inculcate a feeling of using any banking site/application in processes of opening a bank account, logging in and using monetary operations as depositing, transferring and withdrawing money. 
    \nThis program was built in approximately 48 hours spread over the span of 5 weeks which involved learning new concepts, experimenting with the code and scheduling joint sessions to code. 
    \nThis has been a great learning experience to learn additional and practical knowledge while writing the code for this program.
    \n\n====================================
    Keyboard Shortcuts:

    Ctrl+L : login window
    Ctrl+D : delete window
    Ctrl+S : signup window
    Ctrl+T : documentation window
    Alt +H : home window
    Alt +C : Calender
    Ctrl+H : Chat Box
    Ctrl+B : back
    Ctrl+R : refresh window
    Ctrl+P : pop-out calender or chat box
    Ctrl+E : exit
    """

    text_box.configure(state=tk.NORMAL)
    text_box.insert(tk.END, display_text)
    text_box.configure(state=tk.DISABLED)

    scroll_bar = tk.Scrollbar(text_box, cursor='hand2')
    scroll_bar.pack()
    scroll_bar.place(relheight=1, relx=0.974)

    text_box.config(yscrollcommand=scroll_bar.set)
    scroll_bar.config(command=text_box.yview)

    class OptionsPaneHome:
        def __init__(self):

            super(OptionsPaneHome, self).__init__()

            self.options_doc_wn = tk.Tk()
            self.options_doc_wn.overrideredirect(True)
            self.options_doc_wn.config(bg='#1c1c1c')

            abs_coord_x = self.options_doc_wn.winfo_pointerx() - self.options_doc_wn.winfo_rootx()
            abs_coord_y = self.options_doc_wn.winfo_pointery() - self.options_doc_wn.winfo_rooty()
            self.options_doc_wn.geometry(f"+{abs_coord_x}+{abs_coord_y}")

            self.options_doc_wn.geometry("100x178")

            opt_back_button = tk.Button(self.options_doc_wn,
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

            opt_refresh_button = tk.Button(self.options_doc_wn,
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

            opt_home_button = tk.Button(self.options_doc_wn,
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

            opt_chat_box_button = tk.Button(self.options_doc_wn,
                                            text='Open Chat Box  ',
                                            relief=tk.FLAT,
                                            font=('Georgia', '10'),
                                            bg='#1c1c1c',
                                            fg='white',
                                            command=self.cal_scb__,
                                            activebackground='#3d3d3d')
            opt_chat_box_button.pack()
            opt_chat_box_button.place(x=0, y=90)
            opt_chat_box_button.bind('<Enter>', func=lambda e: opt_chat_box_button.config(bg='#3d3d3d'))
            opt_chat_box_button.bind('<Leave>', func=lambda e: opt_chat_box_button.config(bg='#1c1c1c'))

            opt_calendar_button = tk.Button(self.options_doc_wn,
                                            text='Open Calendar  ',
                                            relief=tk.FLAT,
                                            font=('Georgia', '10'),
                                            bg='#1c1c1c',
                                            fg='white',
                                            command=self.call_calendar__,
                                            activebackground='#3d3d3d')
            opt_calendar_button.pack()
            opt_calendar_button.place(x=0, y=120)
            opt_calendar_button.bind('<Enter>', func=lambda e: opt_calendar_button.config(bg='#3d3d3d'))
            opt_calendar_button.bind('<Leave>', func=lambda e: opt_calendar_button.config(bg='#1c1c1c'))

            opt_exit_button = tk.Button(self.options_doc_wn,
                                        text='           Exit          ',
                                        relief=tk.FLAT,
                                        font=('Georgia', '10'),
                                        bg='#1c1c1c',
                                        fg='white',
                                        command=self.exit__,
                                        activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=150)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            documentation_window.bind('<Button-1>', self.left_button_options__home)
            documentation_window.bind('<Button-3>', self.right_button_options__home)

            self.options_doc_wn.after(5000, lambda: self.options_doc_wn.destroy())

        def run(self):
            self.options_doc_wn.mainloop()

        def cal_scb__(self):
            self.options_doc_wn.destroy()
            call_scb()

        def refresh__(self):
            self.options_doc_wn.destroy()
            refresh()

        def return_home__(self):
            self.options_doc_wn.destroy()
            return_home()

        def call_calendar__(self):
            self.options_doc_wn.destroy()
            call_calendar()

        def exit__(self):
            self.options_doc_wn.destroy()
            usr_exit_request()

        def left_button_options__home(self, *args):
            try:
                self.options_doc_wn.destroy()
            except tk.TclError:
                pass

        def right_button_options__home(self, *args):
            try:
                self.options_doc_wn.destroy()
                relaunch_options_pane()
            except tk.TclError:
                relaunch_options_pane()

        def __go_back__(self):
            length = len(open_windows_list)
            element = open_windows_list[length - 1]

            if element == 'home':
                open_windows_list.pop()
                from HomeWindow import home
                self.options_doc_wn.destroy()
                documentation_window.destroy()
                home()

            elif element == 'login':
                open_windows_list.pop()
                from LoginWindow import login
                self.options_doc_wn.destroy()
                documentation_window.destroy()
                login()

            elif element == 'delete':
                open_windows_list.pop()
                from DeleteWindow import delete
                self.options_doc_wn.destroy()
                documentation_window.destroy()
                delete()

            elif element == 'signup':
                open_windows_list.pop()
                from SignupWindow import signup
                self.options_doc_wn.destroy()
                documentation_window.destroy()
                signup()

    def relaunch_options_pane():
        options_pane = OptionsPaneHome()
        options_pane.run()

    def right_button_options__home(*args):
        options_pane = OptionsPaneHome()
        options_pane.run()

    documentation_window.bind('<Button-3>', right_button_options__home)

    def redirect_to_login_window_(*args):
        redirect_to_login_window()

    def redirect_to_delete_window_(*args):
        redirect_to_delete_window()

    def redirect_to_signup_window_(*args):
        redirect_to_signup_window()

    def call_calendar_(*args):
        call_calendar()

    def call_scb_(*args):
        call_scb()

    def refresh_(*args):
        refresh()

    def back_(*args):
        go_back()

    def exit_(*args):
        on_closing()

    documentation_window.bind('<Control-l>', redirect_to_login_window_)
    documentation_window.bind('<Control-d>', redirect_to_delete_window_)
    documentation_window.bind('<Control-s>', redirect_to_signup_window_)
    documentation_window.bind('<Control-c>', call_calendar_)
    documentation_window.bind('<Control-r>', refresh_)
    documentation_window.bind('<Control-t>', back_)
    documentation_window.bind('<Control-h>', call_scb_)
    documentation_window.bind('<Control-e>', exit_)

    def return_home_(*args):
        return_home()

    documentation_window.bind('<Alt-h>', return_home_)

    documentation_window.mainloop()
