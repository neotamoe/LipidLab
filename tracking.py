from PIL import Image
from tkinter import Tk, Label, Button, Entry, W, E
from tkinter.filedialog import askopenfilename

# this will open a file dialog and allow user to select file
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print(filename)

# this code will open a designated image file
img = Image.open('HTG18-SBH_0119.jpg')
img.show()


# this creates a simple demo GUI
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lipids Lab")
        master.geometry("500x250")
        master.resizable(0, 0)
        self.label = Label(master, text="Enter instructions or text here")
        self.label.grid(columnspan=2, row=0)

        self.label2 = Label(master, text="Enter file name: ")
        self.label2.grid(columnspan=2, row=1, sticky=W)

        self.entry = Entry(master)
        self.entry.grid(columnspan=3, row=2, sticky=E)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=3, columnspan=1, sticky=W)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=3, columnspan=1, sticky=E)

    def greet(self):
        print("Greetings!")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
