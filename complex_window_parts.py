from tkinter import *
from tkinter import ttk

class window_with_scrolls:
    def __init__(self, main_page, parent, height=None, width=None):
        self.main_page= main_page
        self.parent= parent

        self.frame = Frame(self.parent)
        self.main_page.add_widgetpack(self.frame, side=TOP, fill=BOTH, expand=1)
        self.frame_holder = Frame(self.frame)
        self.main_page.add_widgetpack(self.frame_holder, side=TOP, fill=BOTH, expand=1)
        self.taskholder = Canvas(self.frame_holder, height=height, width=width)
        self.main_page.add_widgetpack(self.taskholder, side=LEFT, fill=BOTH, expand=1)
        self.second_frame = Frame(self.taskholder)
        self.taskholder.create_window((0, 0), window=self.second_frame, anchor='nw')

        self.scrollbar = ttk.Scrollbar(self.frame_holder, orient=VERTICAL, command=self.taskholder.yview)
        self.main_page.add_widgetpack(self.scrollbar, side=RIGHT, fill=Y)
        self.scrollbar2 = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.taskholder.xview)
        self.main_page.add_widgetpack(self.scrollbar2, side=TOP, fill=X)
        self.taskholder.config(yscrollcommand=self.scrollbar.set)
        self.taskholder.config(xscrollcommand=self.scrollbar2.set)
        self.taskholder.bind('<Configure>',
                             lambda e: self.taskholder.configure(scrollregion=self.taskholder.bbox("all")))
        self.main_page.draw_all_widgets()
    def return_container(self):
        return self.second_frame
    def destroy(self):
        self.frame.destroy()

class loading_window():
    def __init__(self, parent=None):
        if parent:
            self.root = Toplevel(parent.root)
            self.root.grab_set()
            self.root.focus_set()
        else:
            self.root = Tk()
        self.root.title("loading")
        self.root.geometry(f"{200}x{100}")
        self.root.resizable(0, 0)

        # if icon:
        #     self.root.iconbitmap(icon)

    def persents(self, var):
        self.pb = ttk.Progressbar(self.root, orient=HORIZONTAL, mode="determinate", length=200)
        self.pb.pack()
        self.pb.configure(maximum = var)
        print('progress bar started')

    def persents_update(self, var):
        try:
            self.pb.configure(value=var)
            self.pb.update()
        except:  print(" no pb")

    def run(self):
        self.root.mainloop()
