from main_directory.HomeWindow import home
import tkinter as tk
import tkinter.ttk as ttk
import time


def system_boot():

    """
    -> objective: starting the application
    -> call the startup function to load the window at the beginning of the runtime of
    -> destroy the load window and then from main_directory.home, import home function that brings
       the user to the home screen
    """

    def startup():
        # time.sleep(2)

        """
        Once the system_boot() function is called, the startup() function is executed
        the startup window is then destroyed to later call the home window from main_directory.home file

        Create a tkinter window as the first window that appears on app startup
        The entire GUI program is created using tkinter anf tkinter.ttk
        """

        print('[ INFO ] Tkinter [ Tkinter     ] : Startup loaded successfully')
        start_window = tk.Tk()  # create the tkinter window
        start_window.overrideredirect(True)  # remove the status bar

        # ______________fixing window on screen__________credit: stack_overflow

        w = 800  # width for the Tk root
        h = 600  # height for the Tk root

        # get screen width and height
        ws = start_window.winfo_screenwidth()  # width of the screen
        hs = start_window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        start_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # start_window.geometry('800x600')

        # _________________fixing window on screen_END___________________________

        try:
            from PIL import ImageTk, Image
            image1 = ImageTk.PhotoImage(Image.open(r"..\main_directory\images\pic12.png"))

            img_lb = tk.Label(image=image1, borderwidth=0)
            img_lb.pack()
            img_lb.place(x=0, y=0)

        except tk.TclError:
            pass
        except FileNotFoundError:
            pass

        # start_window.title('DataSync International')
        # start_window.config(bg='#68cca1')
        # start_window.resizable(0, 0)
        # # start_window.overrideredirect(True)
        #
        # # We create labels displaying certain elements
        #
        # company_name = tk.Label(start_window, text="Data"+"Sync ® International".title(),
        #                         bg='#68cca1',
        #                         font=('Georgia', '40'))  # #4d90fa
        # company_name.pack()
        # company_name.place(x=100, y=200)
        #
        # system_power = tk.Label(start_window, text="Powered by Tkinter Python 3.8 & MySQL",
        #                         bg='#68cca1',
        #                         font=('aerial', '15'))
        # system_power.pack()
        # system_power.place(x=215, y=300)

        # using tkinter.ttk, we create a particular style for our window to use the progressbar which
        # comes with tkinter.ttk module

        style = ttk.Style()
        style.theme_use('alt')
        style.configure("blue.Horizontal.TProgressbar",
                        foreground='#68cca1', background='#265059')

        # Now we create the progressbar

        progress_bar = ttk.Progressbar(start_window, style="blue.Horizontal.TProgressbar", orient=tk.HORIZONTAL,
                                       length=800, mode='determinate')
        progress_bar.pack()
        progress_bar.place(x=0, y=590)

        def bar():

            """
            At the startup window, we run the progressbar at the same time to display the progress made
            and the time required to launch the homepage. The progressbar is updated after a certain
            duration to a particular value to display the progress made
            """

            progress_bar['value'] = 25  # the progressbar value gets updated to 25%
            start_window.update_idletasks()
            time.sleep(1)  # every second, there is a delay using the time.sleep() method in the time module

            progress_bar['value'] = 50  # the progressbar value gets updated to 50%
            start_window.update_idletasks()
            time.sleep(1)  # every second, there is a delay using the time.sleep() method in the time module

            progress_bar['value'] = 75  # the progressbar value gets updated to 75%
            start_window.update_idletasks()
            time.sleep(1)  # every second, there is a delay using the time.sleep() method in the time module
            progress_bar['value'] = 100  # the progressbar value gets updated to 100%
            start_window.update_idletasks()
            time.sleep(1)  # every second, there is a delay using the time.sleep() method in the time module

        start_window.after(1000, lambda: bar())  # just after 1 second, we call the progressbar which is inside the bar() function

        start_window.after(4000, lambda: start_window.destroy())  # in 4 seconds, we destroy the startup window and launch the home window

        # after the startup window is destroyed, we call the home window in the home file from
        # main_directory.home

        start_window.mainloop()
    startup()

    # after the startup function has been run successfully, we destroy the window and launch the
    # home window from the home file located at main_directory

    home()


'''
SystemBootFile is the first file that is run to launch the app
-> while runtime, we load the startup page first by calling the system_boot() function which contains
   the startup function
'''

if __name__ == "__main__":
    print('[ INFO ] Tkinter [ Tkinter     ] : System loaded successfully')
    system_boot()
