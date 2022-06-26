from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import datetime
import io

class Window():
    def __init__(self, width, height, title="W1", resizable=(False, False),icon=None, parent=None):
        if parent:
            self.root = Toplevel(parent)
            self.root.grab_set()
            self.root.focus_set()
            #self.root.wait_window()
        else:
            self.root = Tk()
        self.root.title(title)
        self.widgets = []
        self.widgetspack = []
        self.widgetsgrid=[]
        if width and height:
            self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
    def run(self):
        self.draw_all_widgets()
        self.root.mainloop()
    def add_widget(self, name, x, y):
        self.widgets.append((name, x, y))
    def add_widgetpack(self, name, side=None, fill=None, expand=None, padx=None, pady=None):
        self.widgetspack.append((name, side, fill, expand, padx, pady))
    def add_widgetgrid(self, name, row, column, padx=None, pady=None, columnspan=None, sticky=None):
        self.widgetsgrid.append((name, row, column, padx, pady, columnspan, sticky))

    def draw_all_widgets(self):
        self.draw_widgets()
        self.draw_widgetspack()
        self.draw_widgetsgrid()
        self.widgets = []
        self.widgetsgrid = []
        self.widgetspack = []

    def draw_widgets(self):
        for i in self.widgets:
            i[0].place(x=i[1], y=i[2])
    def draw_widgetspack(self):
        for i in self.widgetspack:
            i[0].pack(side=i[1], fill=i[2], expand=i[3], padx=i[4], pady=i[5])
    def draw_widgetsgrid(self):
        for i in self.widgetsgrid:
            i[0].grid(row=i[1], column=i[2], padx=i[3], pady=i[4], columnspan=i[5], sticky=i[6])







if __name__=="__main__":
    window = Window(600, 400)
    label1 = Label(window.root, text="label")
    window.add_widget(label1, 300, 200)
    window.run()