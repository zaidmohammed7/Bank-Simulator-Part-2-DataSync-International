import tkinter as tk

BG_COLOR = "#213e4f"
BG_BUTTON_COLOR = "#238c89"


class BankingPopOutChatBox:

    def __init__(self, name, card):
        self.name = name
        self.card = card

        super(BankingPopOutChatBox, self).__init__()

        print('\n[ INFO ] Tkinter [ Tkinter     ] : Chat box [ pop_out     ] loaded successfully')

        self.wn3 = tk.Tk()
        self.wn3.title('Chat Box')
        self.wn3.geometry("+50+440")
        self.wn3.geometry('300x300')
        self.wn3.config(bg=BG_COLOR)
        self.wn3.resizable(False, False)
        try:
            self.wn3.iconbitmap(r'..\main_directory\ico1.ico')
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        self.wn3.focus_force()

        self.TEXT_BOX = tk.Text(self.wn3,
                                width=20,
                                height=12,
                                bg='#17202A',
                                fg='white',
                                wrap=tk.WORD,
                                font=('Georgia', '12'))
        self.TEXT_BOX.pack()
        self.TEXT_BOX.place(x=5, y=5)
        self.TEXT_BOX.configure(state=tk.DISABLED)

        self.TEXT_BOX.configure(state=tk.NORMAL)
        self.TEXT_BOX.insert(tk.END, '\nBob: How may I help you?\n\n')
        self.TEXT_BOX.configure(state=tk.DISABLED)

        self.SCROLL_BAR = tk.Scrollbar(self.TEXT_BOX, cursor='hand2')
        self.SCROLL_BAR.pack()
        self.SCROLL_BAR.place(relheight=1, relx=0.97)

        self.TEXT_BOX.config(yscrollcommand=self.SCROLL_BAR.set)
        self.SCROLL_BAR.config(command=self.TEXT_BOX.yview)

        self.ENTRY_BOX = tk.Entry(self.wn3,
                                  width=20,
                                  bg='#ABB2B9',
                                  font=('Georgia', '13'))
        self.ENTRY_BOX.pack()
        self.ENTRY_BOX.place(x=5, y=260)
        self.ENTRY_BOX.focus_force()

        self.SEND_QUERY_BUTTON = tk.Button(self.wn3, text='Send Query',
                                           bg=BG_BUTTON_COLOR,
                                           activeforeground='white',
                                           activebackground='#787373',
                                           relief=tk.FLAT,
                                           fg='black',
                                           command=self.get_text,
                                           font=('Georgia', '8'))
        self.SEND_QUERY_BUTTON.pack()
        self.SEND_QUERY_BUTTON.place(x=215, y=260)
        self.SEND_QUERY_BUTTON.bind('<Enter>', func=lambda e: (self.SEND_QUERY_BUTTON.config(bg='#57bdba', fg='black')))
        self.SEND_QUERY_BUTTON.bind('<Leave>', func=lambda e: (self.SEND_QUERY_BUTTON.config(bg=BG_BUTTON_COLOR, fg='black')))

        self.CLEAR_MSG_BUTTON = tk.Button(self.wn3, text='      Clear      ',
                                          bg=BG_BUTTON_COLOR,
                                          activeforeground='white',
                                          activebackground='#787373',
                                          relief=tk.FLAT,
                                          fg='black',
                                          command=self.clear_text,
                                          font=('Georgia', '8'))
        self.CLEAR_MSG_BUTTON.pack()
        self.CLEAR_MSG_BUTTON.place(x=215, y=230)
        self.CLEAR_MSG_BUTTON.bind('<Enter>', func=lambda e: (self.CLEAR_MSG_BUTTON.config(text='      Clear      ', bg='#57bdba', fg='black')))
        self.CLEAR_MSG_BUTTON.bind('<Leave>', func=lambda e: (self.CLEAR_MSG_BUTTON.config(text='      Clear      ', bg=BG_BUTTON_COLOR, fg='black')))

        def delete_text(*args):
            self.clear_text()

        self.wn3.bind('<Delete>', delete_text)

        self.wn3.protocol("WM_DELETE_WINDOW", self.on_closing)

        def get__text__(*args):
            self.get_text()

        self.wn3.bind('<Return>', get__text__)

        self.CLEAR_CHAT_BUTTON = tk.Button(self.wn3, text=' Clear Chat ',
                                           bg=BG_BUTTON_COLOR,
                                           activeforeground='white',
                                           activebackground='#787373',
                                           relief=tk.FLAT,
                                           fg='black',
                                           command=self.clear_chat,
                                           font=('Georgia', '8'))
        self.CLEAR_CHAT_BUTTON.pack()
        self.CLEAR_CHAT_BUTTON.place(x=215, y=150)
        self.CLEAR_CHAT_BUTTON.bind('<Enter>', func=lambda e: (self.CLEAR_CHAT_BUTTON.config(text=' Clear Chat ', bg='#57bdba', fg='black')))
        self.CLEAR_CHAT_BUTTON.bind('<Leave>', func=lambda e: (self.CLEAR_CHAT_BUTTON.config(text=' Clear Chat ', bg=BG_BUTTON_COLOR, fg='black')))

        def refresh():
            self.wn3.destroy()
            from main_directory.refresh_windows_functions_file import refresh_banking_pop_up_chat_box__utils__
            refresh_banking_pop_up_chat_box__utils__(self.name, self.card)

        self.REFRESH_BUTTON = tk.Button(self.wn3, text='    Refresh    ',
                                        bg=BG_BUTTON_COLOR,
                                        activeforeground='white',
                                        activebackground='#787373',
                                        relief=tk.FLAT,
                                        fg='black',
                                        command=refresh,
                                        font=('Georgia', '8'))
        self.REFRESH_BUTTON.pack()
        self.REFRESH_BUTTON.place(x=215, y=50)
        self.REFRESH_BUTTON.bind('<Enter>', func=lambda e: self.REFRESH_BUTTON.config(bg='#dbdbdb', fg='black'))
        self.REFRESH_BUTTON.bind('<Leave>', func=lambda e: self.REFRESH_BUTTON.config(bg=BG_BUTTON_COLOR, fg='black'))

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
                from main_directory.ChatBox__reg__utils__ import pop_out_chat_box_list
                from main_directory.Banking_ChatBox__reg__sub__utils__ import chat_box_run_check
                from main_directory.HomeWindow import PopOutChatBox_HOME
                from main_directory.LoginWindow import PopOutChatBox_LOGIN
                from main_directory.SignupWindow import PopOutChatBox_SIGNUP
                from main_directory.DeleteWindow import PopOutChatBox_DELETE
                from main_directory.DocumentationWindow import PopOutChatBox_DOCUMENTATION

                pop_out_chat_box_list.clear()
                chat_box_run_check.clear()
                PopOutChatBox_HOME.clear()
                PopOutChatBox_LOGIN.clear()
                PopOutChatBox_SIGNUP.clear()
                PopOutChatBox_DELETE.clear()
                PopOutChatBox_DOCUMENTATION.clear()

                root.destroy()
                self.wn3.destroy()

            def refresh__():
                root.destroy()
                self.wn3.destroy()
                from main_directory.refresh_windows_functions_file import refresh_pop_out_chat__utils__
                refresh_pop_out_chat__utils__()

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

            self.wn3.bind('<Button-1>', left_button_press)

            def right_button_press__(*args):
                try:
                    root.destroy()
                    right_button_press(*args)
                except tk.TclError:
                    right_button_press(*args)

            self.wn3.bind('<Button-3>', right_button_press__)

            root.after(4000, lambda: root.destroy())

        self.wn3.bind('<Button-3>', start_option_pane)

        def exit_(*args):
            self.on_closing()

        def refresh(*args):
            self.wn3.destroy()
            from main_directory.refresh_windows_functions_file import refresh_pop_out_chat__utils__
            refresh_pop_out_chat__utils__()

        self.wn3.bind('<Control-e>', exit_)
        self.wn3.bind('<Control-r>', refresh)

    def run(self):
        self.wn3.mainloop()

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

            msg1 = f"\nYou: {text.capitalize()}\n\n"

            self.TEXT_BOX.configure(state=tk.NORMAL)
            self.TEXT_BOX.insert(tk.END, msg1, '__query__')
            self.TEXT_BOX.configure(state=tk.DISABLED)

            original_text = text

            original_text = original_text.lower()

            text = text.lower()
            trim = [char for char in text if char.isalpha() or char.isdigit() or char.isspace()]
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

                messages = []
                messages.clear()

                check = []
                check.clear()

                res_len = []
                res_len.clear()

                for i in split_words:
                    for key, value in tokens.items():
                        if i not in messages:
                            if i in key:
                                response = random.choice(value)
                                for j in key:
                                    messages.append(j)

                                check.append(1)
                                res_len.append(1)
                                if len(res_len) >= 1:
                                    self.insert_query(response)

                trim2 = [char for char in original_text if char.isalpha() or char.isdigit()]
                trim2 = ''.join(trim2)

                for key_, values_ in tokens.items():
                    for i in key_:
                        if i not in messages:
                            if i in trim2:
                                for j in key_:
                                    messages.append(j)
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

        reply_ = f"\nBob: {reply}\n\n"
        self.TEXT_BOX.configure(state=tk.NORMAL)
        self.TEXT_BOX.insert(tk.END, reply_, '__reply__')
        self.TEXT_BOX.configure(state=tk.DISABLED)

        self.TEXT_BOX.see(tk.END)

    def clear_text(self):
        self.ENTRY_BOX.delete(0, tk.END)

    def clear_chat(self):
        self.TEXT_BOX.configure(state=tk.NORMAL)
        self.TEXT_BOX.delete(1.0, tk.END)
        self.TEXT_BOX.insert(tk.END, '\nBob: How may I help you?\n\n')
        self.TEXT_BOX.configure(state=tk.DISABLED)

    def on_closing(self):

        from main_directory.ChatBox__reg__utils__ import pop_out_chat_box_list
        from main_directory.Banking_ChatBox__reg__sub__utils__ import chat_box_run_check
        from main_directory.HomeWindow import PopOutChatBox_HOME
        from main_directory.LoginWindow import PopOutChatBox_LOGIN
        from main_directory.SignupWindow import PopOutChatBox_SIGNUP
        from main_directory.DeleteWindow import PopOutChatBox_DELETE
        from main_directory.DocumentationWindow import PopOutChatBox_DOCUMENTATION

        pop_out_chat_box_list.clear()
        chat_box_run_check.clear()
        PopOutChatBox_HOME.clear()
        PopOutChatBox_LOGIN.clear()
        PopOutChatBox_SIGNUP.clear()
        PopOutChatBox_DELETE.clear()
        PopOutChatBox_DOCUMENTATION.clear()

        self.wn3.destroy()
