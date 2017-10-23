import tkinter as tk


class FullScreenApp():

    def __init__(self, master):  #tworzy główne okienko
        self.master = master
        master.title("Smart Power")
        self.master.geometry("{0}x{1}-0-0".format(self.master.winfo_screenwidth(), master.winfo_screenheight()))
        self.screenWidth = self.master.winfo_screenwidth()
        self.screenHeight = self.master.winfo_screenheight()
        self.create_to_bar(self.master, self.master.winfo_screenheight()) #wywołanie medody tworzacej pasek menu
        self.create_left_container(self.master)                           #wywołanie metody tworzacej kontener na wykresy
        self.create_right_container(self.master)

    def return_parent_id(self, master):
        return master

    def create_to_bar(self, parent, screen_height):
        top_bar_height = screen_height/20
        container_top_bar = tk.Frame(parent, width=self.screenWidth, height=top_bar_height, background="blue")
        container_top_bar.pack(side="top")

    def create_left_container(self, parent, screen_height):
        self.container_left = tk.Frame(self.master, width=(self.screenWidth/4), height=self.master.winfo_screenheight()-self.top_bar_height, background="red")
        self.container_left.pack(side="left")

    def create_right_container(self, parent, screen_height):
        self.container_right.pack()
        self.container_right = tk.Frame(self.master, width=(self.screenWidth*(3/4)), height=self.master.winfo_screenheight()-self.top_bar_height, background="green")

        #self.containerLeft = tk.Frame(self.master, width=(self.screenWidth/4), height=master.winfo_screenheight()-self.topBarHeight, background="red")
        #self.containerLeft.pack(side="left")
        #self.containerRight = tk.Frame(self.master, width=(self.screenWidth*(3/4)), height=master.winfo_screenheight()-self.topBarHeight, background="green")
        #self.containerRight.pack()


root = tk.Tk()
app = FullScreenApp(root)
root.mainloop()

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

