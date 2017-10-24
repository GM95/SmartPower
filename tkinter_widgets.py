import tkinter as tk
import random
import fetch_data

class FullScreenAppMainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):  #tworzy główne okienko
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SmartPower")
        tk.Tk.geometry(self, "{0}x{1}-0-0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        tk.Tk.iconbitmap(self, '@/home/grzegorz/PycharmProjects/SmartPower/ps_logo.xbm')
        self.label = tk.Label(text='0', font=("Courier", 44))
        self.label.pack(side="top")
        tk.Tk.after(self, 1000, self.update)

    def update(self):
        #self.label.config(text="napiecie "+str(random.randint(1, 40)))
        self.label.config(text="napiecie "+str(fetch_data.GetDataFromDataBase.get_voltage_static(random.randint(1, 50))))
        tk.Tk.after(self, 1000, self.update)

        """
        self.master = master
        master.title("Smart Power") 
        self.master.geometry("{0}x{1}-0-0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.screenWidth = self.master.winfo_screenwidth()
        self.screenHeight = self.master.winfo_screenheight()
        self.create_to_bar(self.master, self.master.winfo_screenheight()) #wywołanie medody tworzacej pasek menu
        self.create_left_container(self.master)                           #wywołanie metody tworzacej kontener na dane tekstowe
        self.create_right_container(self.master)

    def return_parent_id(self, master):
        return master

    def create_to_bar(self, parent, screen_height):
        top_bar_height = screen_height/20
        container_top_bar = tk.Frame(parent, width=self.screenWidth, height=top_bar_height, background="grey")
        container_top_bar.pack(side="top")
        return container_top_bar

    def create_left_container(self, parent):
        container_left = tk.Frame(parent, width=(parent.winfo_screenwidth()/10), height=parent.winfo_screenheight()-parent.winfo_screenheight()/20, background="white")
        container_left.pack(side="left")
        return container_left

    def create_right_container(self, parent):
        container_right = tk.Frame(parent, width=(parent.winfo_screenwidth()*(9/10)), height=parent.winfo_screenheight()-parent.winfo_screenheight()/20)
        container_right.pack(side="right")
        return container_right
        #self.containerLeft = tk.Frame(self.master, width=(self.screenWidth/4), height=master.winfo_screenheight()-self.topBarHeight, background="red")
        #self.containerLeft.pack(side="left")
        #self.containerRight = tk.Frame(self.master, width=(self.screenWidth*(3/4)), height=master.winfo_screenheight()-self.topBarHeight, background="green")
        #self.containerRight.pack()
        """


"""
class topBar(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.containerTopBar = tk.Frame(master, width=master.screenWidth, height=master.topBarHeight, background="blue")
        self.containerTopBar.pack(side="top")


        self.buttonLeft1 = tk.Button(self.containerLeft, text="button1")
        self.buttonLeft1.grid(row=0, column=1)

        self.buttonLeft2 = tk.Button(self.containerLeft, text="button1")
        self.buttonLeft2.grid(row=1, column=2)

        self.buttonLeft3 = tk.Button(self.containerRight, text="button1")
        self.buttonLeft3.grid(row=1, column=2)

        self.buttonLeft4 = tk.Button(self.containerRight, text="button1")
        self.buttonLeft4.grid(row=0, column=1)


    
        self.master = master
        self.master.geometry("{0}x{1}-0-0".format(
        self.master.winfo_screenwidth(), master.winfo_screenheight()))
        self.master.wm_title("SMARTPower")

        self.master=master
        button = tk.Button()
        button.pack()
        #w = Label(self.master,)
        #self.top = Toplevel()
        #w.pack()
    
        pad=3
        master.geometry("{0}x{1}-0-0".format(
        master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
    
    def noweOkienko(self):
        w = Label(self.master)
        self.top = Toplevel()
        w.pack()
    """

