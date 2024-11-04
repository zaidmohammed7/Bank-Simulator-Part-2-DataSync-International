import threading
import tkinter as tk
from tkinter import messagebox
from main_directory.open_windows import open_windows_list
import time
import datetime

BG_COLOR = "#213e4f"
BG_BUTTON_COLOR = "#238c89"

chat_box_run_check = []


class BankingChatApplicationWn:

    def __init__(self, name, card):
        self.name = name
        self.card = card

        super(BankingChatApplicationWn, self).__init__()

        print('[ INFO ] Tkinter [ Tkinter     ] : chat box loaded successfully')

        self.root = tk.Tk()

        self.root.title('Chat Bot')
        self.root.config(bg=BG_COLOR)
        self.root.resizable(False, False)
        try:
            self.root.iconbitmap(r'..\main_directory\ico1.ico')

            from PIL import ImageTk, Image
            self.image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic4.png"))

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

        # _________________time module display - START___________credit: stack_overflow

        clock = tk.Label(self.root,
                         bg=BG_COLOR,
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
        date_label = tk.Label(self.root,
                              text='|    ' + date.strftime("%Y-%m-%d") + '   |',
                              bg=BG_COLOR,
                              fg='white',
                              font=('Georgia', '10'))
        date_label.pack()
        date_label.place(x=590, y=0)

        # ________________________date display - END_____________________________

        self.TEXT_BOX = tk.Text(self.root,
                                width=40,
                                height=17,
                                bg='#17202A',
                                fg='white',
                                wrap=tk.WORD,
                                font=('Georgia', '15'))
        self.TEXT_BOX.pack()
        self.TEXT_BOX.place(x=150, y=80)
        self.TEXT_BOX.configure(state=tk.DISABLED)  # DISABLED

        self.TEXT_BOX.configure(state=tk.NORMAL)
        self.TEXT_BOX.insert(tk.END, '\nBob: How may I help you?\n\n')
        self.TEXT_BOX.configure(state=tk.DISABLED)

        self.ENTRY_BOX = tk.Entry(self.root,
                                  width=40,
                                  bg='#ABB2B9',
                                  font=('Georgia', '15'))
        self.ENTRY_BOX.pack()
        self.ENTRY_BOX.place(x=150, y=500)
        self.ENTRY_BOX.focus_force()

        self.SCROLL_BAR = tk.Scrollbar(self.TEXT_BOX, cursor='hand2')
        self.SCROLL_BAR.pack()
        self.SCROLL_BAR.place(relheight=1, relx=0.974)

        self.TEXT_BOX.config(yscrollcommand=self.SCROLL_BAR.set)
        self.SCROLL_BAR.config(command=self.TEXT_BOX.yview)

        self.TITLE = tk.Label(self.root,
                              text="Welcome to ChatBot",
                              bg=BG_COLOR,
                              font=('Georgia', '20'),
                              fg='white')
        self.TITLE.pack()
        self.TITLE.place(x=270, y=30)

        self.SEND_QUERY_BUTTON = tk.Button(self.root, text='\nSend Query\n',
                                           bg=BG_BUTTON_COLOR,
                                           activeforeground='white',
                                           activebackground='#787373',
                                           relief=tk.FLAT,
                                           fg='white',
                                           command=self.get_text,
                                           font=('Georgia', '10'))
        self.SEND_QUERY_BUTTON.pack()
        self.SEND_QUERY_BUTTON.place(x=650, y=470)
        self.SEND_QUERY_BUTTON.bind('<Enter>', func=lambda e: (self.SEND_QUERY_BUTTON.config(bg='#57bdba', fg='black')))
        self.SEND_QUERY_BUTTON.bind('<Leave>', func=lambda e: (self.SEND_QUERY_BUTTON.config(bg=BG_BUTTON_COLOR, fg='white')))

        def get__text__(*args):
            self.get_text()

        self.root.bind('<Return>', get__text__)

        self.CLEAR_MSG_BUTTON = tk.Button(self.root, text='\n      Clear       \n ',
                                          bg=BG_BUTTON_COLOR,
                                          activeforeground='white',
                                          activebackground='#787373',
                                          relief=tk.FLAT,
                                          fg='white',
                                          command=self.clear_text,
                                          font=('Georgia', '10'))
        self.CLEAR_MSG_BUTTON.pack()
        self.CLEAR_MSG_BUTTON.place(x=650, y=400)
        self.CLEAR_MSG_BUTTON.bind('<Enter>', func=lambda e: (self.CLEAR_MSG_BUTTON.config(text='\n      Clear       \n ', bg='#57bdba', fg='black')))
        self.CLEAR_MSG_BUTTON.bind('<Leave>', func=lambda e: (self.CLEAR_MSG_BUTTON.config(text='\n      Clear       \n ', bg=BG_BUTTON_COLOR, fg='white')))

        self.CLEAR_CHAT_BUTTON = tk.Button(self.root, text='\n Clear Chat  \n ',
                                           bg=BG_BUTTON_COLOR,
                                           activeforeground='white',
                                           activebackground='#787373',
                                           relief=tk.FLAT,
                                           fg='white',
                                           command=self.clear_chat,
                                           font=('Georgia', '9'))
        self.CLEAR_CHAT_BUTTON.pack()
        self.CLEAR_CHAT_BUTTON.place(x=650, y=300)
        self.CLEAR_CHAT_BUTTON.bind('<Enter>', func=lambda e: (self.CLEAR_CHAT_BUTTON.config(text='\n Clear Chat  \n ', bg='#57bdba', fg='black')))
        self.CLEAR_CHAT_BUTTON.bind('<Leave>', func=lambda e: (self.CLEAR_CHAT_BUTTON.config(text='\n Clear Chat  \n ', bg=BG_BUTTON_COLOR, fg='white')))

        def delete_text(*args):
            self.clear_text()

        self.root.bind('<Delete>', delete_text)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        def refresh():
            self.root.destroy()
            from main_directory.refresh_windows_functions_file import refresh_banking_chat_box__utils__
            refresh_banking_chat_box__utils__(self.name, self.card)

        self.REFRESH_LABEL = tk.Label(self.root, text='',
                                      bg='#213e4f',
                                      font=('Georgia', '12'))
        self.REFRESH_LABEL.pack()
        self.REFRESH_LABEL.place(x=70, y=95)

        self.REFRESH_BUTTON = tk.Button(self.root, text='     \n     ♻      \n     ',
                                        bg=BG_BUTTON_COLOR,
                                        activeforeground='white',
                                        activebackground='#787373',
                                        relief=tk.FLAT,
                                        fg='white',
                                        command=refresh,
                                        font=('Georgia', '10'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=2, y=75)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: (self.REFRESH_BUTTON.config(bg='#dbdbdb', fg='black'), self.REFRESH_LABEL.config(text='   Refresh    ', bg='#dbdbdb', fg='black')))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: (self.REFRESH_BUTTON.config(bg=BG_BUTTON_COLOR, fg='white'), self.REFRESH_LABEL.config(text='', bg='#213e4f')))

        def return_home():
            self.root.destroy()
            open_windows_list.clear()
            from main_directory.HomeWindow import home
            home()

        self.HOME_LABEL = tk.Label(self.root, text='',
                                   bg='#213e4f',
                                   font=('Georgia', '12'))
        self.HOME_LABEL.pack()
        self.HOME_LABEL.place(x=70, y=155)

        self.HOME_BUTTON = tk.Button(self.root, text='     \n  Home   \n     ',
                                     bg=BG_BUTTON_COLOR,
                                     activeforeground='white',
                                     activebackground='#787373',
                                     relief=tk.FLAT,
                                     fg='white',
                                     command=return_home,
                                     font=('Georgia', '10'))
        self.HOME_BUTTON.pack()
        self.HOME_BUTTON.place(x=2, y=140)
        self.HOME_BUTTON.bind('<Enter>', func=lambda e: (self.HOME_BUTTON.config(bg='#dbdbdb', fg='black'), self.HOME_LABEL.config(text='   Home    ', bg='#dbdbdb', fg='black')))
        self.HOME_BUTTON.bind('<Leave>', func=lambda e: (self.HOME_BUTTON.config(bg=BG_BUTTON_COLOR, fg='white'), self.HOME_LABEL.config(text='', bg='#213e4f')))

        self.EXIT_BUTTON = tk.Button(self.root, text='     \n    Exit    \n     ',
                                     bg='#213e4f',
                                     activeforeground='white',
                                     activebackground='maroon',
                                     fg='white',
                                     command=self.usr_exit_request,
                                     relief=tk.FLAT,
                                     font=('Georgia', '10'))
        self.EXIT_BUTTON.pack()
        self.EXIT_BUTTON.place(x=2, y=537)
        self.EXIT_BUTTON.bind('<Enter>', func=lambda e: self.EXIT_BUTTON.config(bg='#ff0314'))
        self.EXIT_BUTTON.bind('<Leave>', func=lambda e: self.EXIT_BUTTON.config(bg='#213e4f'))

        self.GO_BACK_BUTTON = tk.Button(self.root,
                                        text="    Back   ",
                                        bg=BG_BUTTON_COLOR,
                                        relief=tk.FLAT,
                                        activeforeground='white',
                                        activebackground='#546f7a',
                                        fg='white',
                                        command=self.go_back,
                                        font=('Georgia', '10'))
        self.GO_BACK_BUTTON.pack()
        self.GO_BACK_BUTTON.place(x=2, y=20)
        self.GO_BACK_BUTTON.bind('<Enter>', func=lambda e: self.GO_BACK_BUTTON.config(bg='#dbdbdb', fg='black'))
        self.GO_BACK_BUTTON.bind('<Leave>', func=lambda e: self.GO_BACK_BUTTON.config(bg=BG_BUTTON_COLOR, fg='white'))

        self.POP_OUT_WN_LABEL = tk.Label(self.root, text='',
                                         bg=BG_COLOR,
                                         fg='white',
                                         font=('Georgia', '12'))
        self.POP_OUT_WN_LABEL.pack()
        self.POP_OUT_WN_LABEL.place(x=730, y=130)

        self.POP_OUT_WN_BUTTON = tk.Button(self.root,
                                           text="➰",
                                           bg='#cfb476',
                                           relief=tk.FLAT,
                                           activeforeground='white',
                                           activebackground='#787373',
                                           fg='black',
                                           command=self.pop_out,
                                           font=('Georgia', '10'))
        self.POP_OUT_WN_BUTTON.pack()
        self.POP_OUT_WN_BUTTON.place(x=750, y=100)
        self.POP_OUT_WN_BUTTON.bind('<Enter>', func=lambda e: (self.POP_OUT_WN_BUTTON.config(bg='#dbdbdb', fg='black'), self.POP_OUT_WN_LABEL.config(text='Pop Out')))
        self.POP_OUT_WN_BUTTON.bind('<Leave>', func=lambda e: (self.POP_OUT_WN_BUTTON.config(bg='#cfb476', fg='black'), self.POP_OUT_WN_LABEL.config(text='', bg=BG_COLOR)))

        def right_button_press(*args):
            start_option_menu()

        def start_option_menu(*args):
            root2 = tk.Tk()
            abs_coord_x = root2.winfo_pointerx() - root2.winfo_rootx()
            abs_coord_y = root2.winfo_pointery() - root2.winfo_rooty()

            root2.geometry(f"+{abs_coord_x}+{abs_coord_y}")
            root2.geometry("100x148")

            root2.overrideredirect(True)
            root2.config(bg='#1c1c1c')

            def refresh__():
                root2.destroy()
                refresh()

            def return_home__():
                root2.destroy()
                return_home()

            def go_back__():
                self.root.destroy()
                root2.destroy()

                from main_directory.banking_class import Banking
                connect_banking_class = Banking(self.name, self.card)
                connect_banking_class.mainloop()

            opt_back_button = tk.Button(root2, text='         Back           ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=go_back__, activebackground='#3d3d3d')
            opt_back_button.pack()
            opt_back_button.place(x=0, y=0)
            opt_back_button.bind('<Enter>', func=lambda e: opt_back_button.config(bg='#3d3d3d'))
            opt_back_button.bind('<Leave>', func=lambda e: opt_back_button.config(bg='#1c1c1c'))

            opt_refresh_button = tk.Button(root2, text='       Refresh       ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=refresh__, activebackground='#3d3d3d')
            opt_refresh_button.pack()
            opt_refresh_button.place(x=0, y=30)
            opt_refresh_button.bind('<Enter>', func=lambda e: opt_refresh_button.config(bg='#3d3d3d'))
            opt_refresh_button.bind('<Leave>', func=lambda e: opt_refresh_button.config(bg='#1c1c1c'))

            opt_home_button = tk.Button(root2, text=' Return Home     ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=return_home__, activebackground='#3d3d3d')
            opt_home_button.pack()
            opt_home_button.place(x=0, y=60)
            opt_home_button.bind('<Enter>', func=lambda e: opt_home_button.config(bg='#3d3d3d'))
            opt_home_button.bind('<Leave>', func=lambda e: opt_home_button.config(bg='#1c1c1c'))

            def pop_out__():
                from main_directory.ChatBox__reg__utils__ import pop_out_chat_box_list

                if len(pop_out_chat_box_list) == 0:
                    if len(chat_box_run_check) == 0:
                        pop_out_chat_box_list.append(1)
                        chat_box_run_check.append(1)
                        self.root.destroy()

                        from main_directory.BankingPopOutChatBox__reg__sub__utils__ import BankingPopOutChatBox

                        def run_banking_pop_out_chat_box():
                            app = BankingPopOutChatBox(self.name, self.card)
                            app.run()

                        self.root.after(10, lambda: run_banking_pop_out_chat_box())
                        root2.destroy()

                        from main_directory.banking_class import Banking
                        connect_banking_class = Banking(self.name, self.card)
                        connect_banking_class.mainloop()

            opt_pop_out_button = tk.Button(root2, text='       Pop Out           ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=pop_out__, activebackground='#3d3d3d')
            opt_pop_out_button.pack()
            opt_pop_out_button.place(x=0, y=90)
            opt_pop_out_button.bind('<Enter>', func=lambda e: opt_pop_out_button.config(bg='#3d3d3d'))
            opt_pop_out_button.bind('<Leave>', func=lambda e: opt_pop_out_button.config(bg='#1c1c1c'))

            def exit__():
                response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
                if response is True:
                    import sys
                    sys.exit()

            opt_exit_button = tk.Button(root2, text='           Exit          ', relief=tk.FLAT, font=('Georgia', '10'), bg='#1c1c1c', fg='white', command=exit__, activebackground='#3d3d3d')
            opt_exit_button.pack()
            opt_exit_button.place(x=0, y=120)
            opt_exit_button.bind('<Enter>', func=lambda e: opt_exit_button.config(bg='#ff0314'))
            opt_exit_button.bind('<Leave>', func=lambda e: opt_exit_button.config(bg='#1c1c1c'))

            def left_button_press(*args):
                try:
                    root2.destroy()
                except tk.TclError:
                    pass

            self.root.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root2.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.root.bind('<Button-3>', right_button_press__)

            root2.after(4000, lambda: root2.destroy())

        self.root.bind('<Button-3>', start_option_menu)

        def refresh__fn(*args):
            refresh()

        def return_home__fn(*args):
            return_home()

        def exit__fn(*args):
            self.on_closing()

        def pop_out__fn(*args):
            self.pop_out()

        def back__fn(*args):
            self.go_back()

        self.root.bind('<Control-r>', refresh__fn)
        self.root.bind('<Alt-h>', return_home__fn)
        self.root.bind('<Control-e>', exit__fn)
        self.root.bind('<Control-p>', pop_out__fn)
        self.root.bind('<Control-b>', back__fn)

    def get_text(self):

        from multi_char_chat_tokens import tokens
        import random

        text = self.ENTRY_BOX.get()
        text = text.lower().lstrip().rstrip()
        if len(text) <= 1:
            query_text = "** Please enter a valid query\n"
            self.TEXT_BOX.configure(state=tk.NORMAL)
            self.TEXT_BOX.insert(tk.END, query_text)
            self.TEXT_BOX.configure(state=tk.DISABLED)
            self.TEXT_BOX.see(tk.END)

        else:
            self.TEXT_BOX.tag_config('__query__', background='#274f5c')
            self.ENTRY_BOX.delete(0, tk.END)
            msg1 = f"\n{'You'}: {text.capitalize()}\n\n"
            self.TEXT_BOX.configure(state=tk.NORMAL)
            self.TEXT_BOX.insert(tk.END, msg1, '__query__')
            self.TEXT_BOX.configure(state=tk.DISABLED)

            original_text = text

            original_text = original_text.lower()
            trim = [char for char in original_text if char.isalpha() or char.isdigit() or char.isspace()]
            trim = ''.join(trim)

            split_words = trim.split()

            if len(split_words) == 1:

                check = []
                check.clear()

                from main_directory.single_char_chat_tokens import single_tokens

                for i in split_words:
                    for k, v in single_tokens.items():
                        if i in k:
                            check.append(1)
                            response = random.choice(v)
                            self.insert_query(response)

                if len(check) == 0:
                    self.insert_query("I don't understand that. I'm learning you see")

            else:

                messagebox_ = []
                messagebox_.clear()

                check = []
                check.clear()

                res_len = []
                res_len.clear()

                for i in split_words:
                    if i not in messagebox_:
                        for key, values in tokens.items():
                            if i in key:
                                for j in key:
                                    messagebox_.append(j)

                                check.append(1)
                                res_len.append(1)
                                if len(res_len) >= 1:
                                    response = random.choice(values)
                                    self.insert_query(response)

                trim2 = [char for char in original_text if char.isalpha() or char.isdigit()]
                trim2 = ''.join(trim2)

                for key_, values_ in tokens.items():
                    for i in key_:
                        if i not in messagebox_:
                            if i in trim2:
                                for j in key_:
                                    messagebox_.append(j)
                                check.append(1)
                                res_len.append(1)
                                if len(res_len) >= 1:
                                    response = random.choice(values_)
                                    self.insert_query(response)

                if len(check) == 0:
                    self.insert_query("I don't understand that. I'm learning you see")

    def insert_query(self, reply):
        self.TEXT_BOX.tag_config('__reply__', background='#17202A')
        self.ENTRY_BOX.delete(0, tk.END)
        msg1 = f"\nBob: {reply}\n\n"
        self.TEXT_BOX.configure(state=tk.NORMAL)
        self.TEXT_BOX.insert(tk.END, msg1, '__reply__')
        self.TEXT_BOX.configure(state=tk.DISABLED)

        self.TEXT_BOX.see(tk.END)

    def go_back(self):
        self.root.destroy()

        from main_directory.banking_class import Banking
        connect_banking_class = Banking(self.name, self.card)
        connect_banking_class.mainloop()

    def clear_text(self):
        self.ENTRY_BOX.delete(0, tk.END)

    def clear_chat(self):
        self.TEXT_BOX.configure(state=tk.NORMAL)
        self.TEXT_BOX.delete(1.0, tk.END)
        self.TEXT_BOX.insert(tk.END, '\nBob: How may I help you?\n\n')
        self.TEXT_BOX.configure(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()
        # self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?") is True:
            self.root.destroy()
            import sys
            sys.exit()

    def usr_exit_request(self):
        response = messagebox.askokcancel(title="Exit Prompt", message="Are you sure you want to exit?")
        if response is True:
            self.root.destroy()
            import sys
            sys.exit()

    def pop_out(self):
        from main_directory.ChatBox__reg__utils__ import pop_out_chat_box_list

        if len(pop_out_chat_box_list) == 0:
            if len(chat_box_run_check) == 0:

                pop_out_chat_box_list.append(1)
                chat_box_run_check.append(1)
                self.root.destroy()

                from main_directory.BankingPopOutChatBox__reg__sub__utils__ import BankingPopOutChatBox

                def run_banking_pop_out_chat_box():
                    app = BankingPopOutChatBox(self.name, self.card)
                    app.run()

                self.root.after(10, lambda: run_banking_pop_out_chat_box())

                from main_directory.banking_class import Banking
                connect_banking_class = Banking(self.name, self.card)
                connect_banking_class.mainloop()


        pass


# app = ChatApplicationWn()
# app.run()
