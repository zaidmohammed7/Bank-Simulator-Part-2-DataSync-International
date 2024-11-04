import tkinter as tk

text = """
DataSync International 
Version: 17.0.0.1 (System Build PB17.0.0.1.S01R01AA2021TFA)
© DataSync International. All Rights Reserved.

DataSync International SystemBootFile Windows10 via-run 
System and its user interface shall be and would be 
protected by trademark and other pending or existing
intellectual property rights in India and other regions.

This product is licensed under the DSI Software License Terms to:
    Abhijeet
    Armaan
    Zaid
     """


class DSIWinVer:
    def __init__(self):
        super(DSIWinVer, self).__init__()

        self.wn = tk.Tk()
        self.wn.resizable(False, False)
        self.wn.geometry('455x380')
        self.wn.geometry('+30+30')
        self.wn.title('About Data Sync International')
        try:
            self.wn.iconbitmap(r'..\main_directory\ico1.ico')
        except tk.TclError:
            pass
        except FileNotFoundError:
            pass
        self.wn.config(bg='black')
        self.wn.focus_force()

        header = tk.Label(self.wn, text='DataSync International', font=('Georgia', 28), bg='black', fg='white')
        header.pack()
        header.place(x=38, y=30)

        content = tk.Label(self.wn, text=text, font=('Helvetica', 10), bg='black', fg='white', justify='left')
        content.pack()
        content.place(x=40, y=90)

        btn = tk.Button(self.wn, text='     OK     ', bg='#cfcfcf', relief=tk.FLAT, bd=3, command=self.close)
        btn.pack()
        btn.place(x=380, y=340)
        btn.bind('<Enter>', func=lambda e: btn.config(bg='white'))
        btn.bind('<Leave>', func=lambda e: btn.config(bg='#cfcfcf'))

        extra_ = tk.Label(self.wn, text='DSI', font=('Helvetica', 10, 'italic'), bg='black', fg='white')
        extra_.pack()
        extra_.place(x=40, y=340)

        self.wn.protocol("WM_DELETE_WINDOW", self.close)

    def run(self):
        self.wn.mainloop()

    def close(self):
        from main_directory.HomeWindow import dsi_check
        dsi_check.clear()

        self.wn.destroy()
