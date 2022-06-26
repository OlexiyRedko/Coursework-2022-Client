from WindowClassFile import *
from connection_functions import *
import calendar
import datetime
from complex_window_parts import window_with_scrolls
import logs_db


class Button_profile(Button):
    def __init__(self, id, password=0, *args, **kw):
        super().__init__(*args, **kw)
        self.id = id
        self.password=password
        self.info = get_info(id, photo=0)
        self.config(text=self.info[0] + " " + self.info[1])
        self.picturefilename= None
    def show_profile(self):
        self.info = get_info(self.id)
        self.window = Window(600, 400, title='profile window', parent=self.master, resizable=(True, False))
        self.window.root.minsize(500, 400)
        self.left = Frame(self.window.root)
        self.window.add_widgetpack(self.left, side=LEFT)
        self.right = Frame(self.window.root)
        self.window.add_widgetpack(self.right, side=LEFT)
        try:
            self.my_pic = Image.open(io.BytesIO(self.info[3]))
        except:
            self.my_pic = None
        if self.my_pic != None:
            self.my_pic = self.my_pic.resize((200, 200), Image.ANTIALIAS)
            self.my_pic = ImageTk.PhotoImage(self.my_pic)
            self.image = Label(self.left, image = self.my_pic)
            self.window.add_widgetpack(self.image, side=TOP, pady=30, padx=30)

        self.name =Label(self.right, text=self.info[0])
        self.window.add_widgetpack(self.name, side=TOP, pady=30, padx=30)
        self.name2 = Label(self.right, text=self.info[1])
        self.window.add_widgetpack(self.name2, side=TOP, pady=30, padx=30)
        self.name3 = Label(self.right, text=self.info[2])
        self.window.add_widgetpack(self.name3, side=TOP, pady=30, padx=30)
        self.window.run()
    def show_profile1(self):
        self.info = get_info(self.id)
        def zberegty_zminy():
            # info[id, login, password, role, name, surname, lastname, photo]
            if self.entry1.get()!="":
                name = self.entry1.get()
            else:
                name = self.info[0]
            if self.entry1.get()!="":
                name2 = self.entry2.get()
            else:
                name2 = self.info[1]
            if self.entry1.get()!="":
                name3 = self.entry3.get()
            else:
                name3 = self.info[2]
            send_info_changes(self.id, self.password, name, name2, name3)
            if self.picturefilename!=None:
                a = send_picture_changes(self.id, self.password, self.picturefilename)
                print(a)
            self.info = get_info(self.id)
            self.config(text=self.info[0]+" "+self.info[1])
            self.window.root.destroy()
        def zavantaj_zobraj():
            self.picturefilename = fd.askopenfilename(title="Виберіть файл")
            self.my_pic = Image.open(self.picturefilename)
            if self.my_pic != None:
                self.my_pic = self.my_pic.resize((200, 200), Image.ANTIALIAS)
                self.my_pic = ImageTk.PhotoImage(self.my_pic)
                self.image.config(image=self.my_pic)
        self.window = Window(600, 450, title='profile window', parent=self.master, resizable=(True, False))
        self.window.root.minsize(500, 450)
        self.left = Frame(self.window.root)
        self.window.add_widgetpack(self.left, side=LEFT)
        self.right = Frame(self.window.root)
        self.window.add_widgetpack(self.right, side=LEFT)
        try:
            self.my_pic = Image.open(io.BytesIO(self.info[3]))
            self.my_pic = self.my_pic.resize((200, 200), Image.ANTIALIAS)
            self.my_pic = ImageTk.PhotoImage(self.my_pic)
            self.image = Label(self.left, image=self.my_pic)
            self.window.add_widgetpack(self.image, side=TOP, pady=30, padx=30)
        except:
            self.image = Label(self.left, )
            self.window.add_widgetpack(self.image, side=TOP, pady=30, padx=30)

        self.button_pic = Button(self.left, text="завантажити зображення", command=zavantaj_zobraj)
        self.window.add_widgetpack(self.button_pic)

        self.name = Label(self.right, text=self.info[0])
        self.window.add_widgetpack(self.name, side=TOP, pady=30, padx=30)
        self.entry1 = Entry(self.right, width=20)
        self.window.add_widgetpack(self.entry1, side=TOP)
        self.name2 = Label(self.right, text=self.info[1])
        self.window.add_widgetpack(self.name2, side=TOP, pady=30, padx=30)
        self.entry2 = Entry(self.right, width=20)
        self.window.add_widgetpack(self.entry2, side=TOP)
        self.name3 = Label(self.right, text=self.info[2])
        self.window.add_widgetpack(self.name3, side=TOP, pady=30, padx=30)
        self.entry3 = Entry(self.right, width=20)
        self.window.add_widgetpack(self.entry3, side=TOP)
        self.button_apply = Button(self.right, text="зберегти зміни", command=zberegty_zminy)
        self.window.add_widgetpack(self.button_apply, pady=30, padx=30)
        self.window.run()

class Button_other_materials(Button):
    def __init__(self, group, filename, base, parent=None, command2=None, *args, **kw):
        super().__init__(*args, **kw)
        self.filename = filename
        self.base = base
        self.group= group
        self.command2 = command2
        self.m=parent
    def delete(self):
        delete_data(self.group, self.base, self.filename)
        self.command2()
    def download(self):
        if download_data(self.group, self.base, self.filename, self.m) == "Error":
            self.config(text="file doesn't exist")

class Indexed_button(Button):
    def __init__(self, filename, group, month, day, year, id, parent = None, command2=None, *args, **kw):
        super().__init__(*args,**kw)
        self.index=0
        self.year = year
        self.group=group
        self.month = calendar.month_name[month]
        self.day = day
        self.id = id
        self.filename = filename
        self.command2 = command2
        self.m = parent

    def button_download(self):
        self.base = [self.month+str(self.year), self.day]
        download_data(self.group, self.base, self.filename)

    def download_answer(self):
        self.base = [self.month+str(self.year), self.day]
        download_data(self.group, self.base, self.filename, answer=1)

    def button_delete(self):
        self.base = [self.year, self.month, self.day]
        delete_data(self.group, self.base, self.filename)
        self.command2()

    def delete_answer(self):
        self.base = [self.year, self.month, self.day]
        delete_data(self.group, self.base, self.filename, answer=1)
        self.command2()

    def button_upload(self):
        file = fd.askopenfilename(title="Виберіть файл")
        self.base = [self.month+str(self.year), self.day]
        print(file)
        upload_homework(self.group, self.base, file, self.id)
        self.command2()

    def button_add_task(self):
        base = [self.year, self.month, self.day]
        file = fd.askopenfilename(title="Виберіть файл")
        upload_task(self.group, base, file)
        self.command2()

    def set_mark(self):
        self.markwindow = Window(600, 400, title='task window', parent=self.master)
        self.mark_text = Label(self.markwindow.root, wraplength = 600)
        self.markwindow.add_widgetpack(self.mark_text, side=TOP)
        self.mark_text.config(text=get_mark(self.group, self.year, self.month, self.day, self.filename))
        self.markwindow.draw_all_widgets()

class Calendar_button(Button):
    def __init__(self, tgroup, index, id,  *args, **kw):
        super().__init__(*args,**kw)
        self.index=index
        self.group = tgroup
        self.id = id
        self.year = None
        self.month = None
        self.day = None
    def set_group(self, group):
        self.group = group

    def set_date(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show_task(self):
        try:self.tpag.destroy()
        except Exception:print(Exception)
        try:self.tpag = window_with_scrolls(self.window, self.window.root);self.taskpage = self.tpag.return_container()
        except:print('here');self.window = Window(600, 400, title='task window', parent=self.master);self.tpag = window_with_scrolls(self.window,self.window.root);self.taskpage = self.tpag.return_container()
        self.content = tasks_for_day(self.group, calendar.month_name[self.month]+str(self.year), self.day)
        print(self.content)
        self.upperframe = Frame(self.taskpage)
        self.window.add_widgetgrid(self.upperframe, row=0, column=0)
        self.button_homework = Calendar_button(self.group, self.index, self.id, master=self.upperframe,text='see homework', relief=RIDGE)
        self.window.add_widgetpack(self.button_homework, side=LEFT)
        self.button_homework.set_date(self.year, self.month, self.day)
        self.button_homework.config(command=self.show_answers)
        for i in range(len(self.content)):
            self.frame = Frame(self.taskpage)
            self.window.add_widgetgrid(self.frame, row=i+1, column=0)
            self.label_index=Label(self.frame, text=self.content[i][0])
            self.window.add_widgetpack(self.label_index, side=LEFT)
            self.label_time = Label(self.frame, text=datetime.datetime.fromtimestamp(self.content[i][1]))
            self.window.add_widgetpack(self.label_time, side=LEFT)
            self.frame2 = Frame(self.frame)
            self.window.add_widgetpack(self.frame2, side=RIGHT)
            self.button_download= Indexed_button(self.content[i][0], self.group, self.month, self.day, self.year, self.id, parent=self.window, master=self.frame2, text='download', relief=RIDGE)
            self.window.add_widgetpack(self.button_download, side=LEFT)
            self.button_download.config(command = self.button_download.button_download)
            self.button_upload_answer = Indexed_button(self.content[i][0], self.group, self.month, self.day, self.year, self.id, master=self.frame2, text='upload answer',command2=self.show_answers, relief=RIDGE)
            self.window.add_widgetpack(self.button_upload_answer, side=LEFT)
            self.button_upload_answer.config(command=self.button_upload_answer.button_upload)
        self.window.draw_all_widgets()

    def show_answers(self):
        try:self.tpag2.destroy()
        except Exception:print(Exception)
        try:
            self.tpag2 = window_with_scrolls(self.window2,self.window2.root)
            self.taskpage2 = self.tpag2.return_container()
        except:
            print('here')
            self.window2 = Window(600, 400, title='homework',parent=self.master)
            self.tpag2 = window_with_scrolls(self.window2,self.window2.root)
            self.taskpage2 = self.tpag2.return_container()
        self.content = answers_for_task(self.group, calendar.month_name[self.month] + str(self.year), self.day, self.id)
        print(self.content)
        self.upperframe = Frame(self.taskpage2)
        self.window2.add_widgetgrid(self.upperframe, row=0, column=0)
        self.button_upload_answer = Indexed_button(None, self.group, self.month, self.day, self.year, self.id, master=self.upperframe, text='upload answer',command2=self.show_answers)
        self.window2.add_widgetpack(self.button_upload_answer, side=LEFT)
        self.button_upload_answer.config(command=self.button_upload_answer.button_upload)
        for i in range(len(self.content)):
            self.frame = Frame(self.taskpage2)
            self.window2.add_widgetgrid(self.frame, row=i + 1, column=0, padx=10, pady=10)
            self.frame3 = Frame(self.frame)
            self.window2.add_widgetpack(self.frame3, side=LEFT)
            self.label_index = Label(self.frame3, text=self.content[i][0])
            self.window2.add_widgetpack(self.label_index, side=TOP)
            self.label_time = Label(self.frame3, text=datetime.datetime.fromtimestamp(self.content[i][1]))
            self.window2.add_widgetpack(self.label_time, side=TOP)
            self.frame2 = Frame(self.frame)
            self.window2.add_widgetpack(self.frame2, side=RIGHT)
            self.button_download = Indexed_button(self.content[i][0], self.group, self.month, self.day, self.year, self.id,master=self.frame2, text='download', width=20, relief=RIDGE)
            self.window2.add_widgetpack(self.button_download, side=TOP)
            self.button_download.config(command = self.button_download.download_answer)
            self.frame_markholder = Frame(self.frame2)
            self.window2.add_widgetpack(self.frame_markholder, side=TOP)
            self.button_delete = Indexed_button(self.content[i][0], self.group, self.month, self.day, self.year, self.id,master=self.frame_markholder, text='delete', command2=self.show_answers, width=10, relief=RIDGE)
            self.window2.add_widgetpack(self.button_delete, side=LEFT)
            self.button_delete.config(command = self.button_delete.delete_answer)
            self.button_mark = Indexed_button(self.content[i][0], self.group, self.month, self.day, self.year, self.id, master=self.frame_markholder, text='mark', width=10, relief=RIDGE)
            self.window2.add_widgetpack(self.button_mark, side=LEFT)
            self.button_mark.config(command=self.button_delete.set_mark)
        self.window2.draw_all_widgets()

    def set_button_index(self, ind):
        self.index = ind

class main_page():
    def __init__(self, info):
        self.main_page = Window(None, None, resizable=(0,0), title="Student page")
        self.id = info[0]
        self.role = info[3]
        self.info = info
        # info[id, login, password, role, name, surname, lastname, photo]
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.classpicked = IntVar(value=0)
        def back():
            self.month -= 1
            if self.month==0:
                self.month=12
                self.year-=1
            self.fill()
        def forward():
            self.month += 1
            if self.month==13:
                self.month=1
                self.year+=1
            self.fill()
        def list_button():
            try:
                self.content_window.destroy()
                self.frame2.destroy()
                self.frame3.destroy()
            except:
                pass
            self.calendar_var = 0
            self.get_other_materials()
        def calendar_button():
            try:
                self.content_window.destroy()
                self.frame2.destroy()
                self.frame3.destroy()
            except:
                pass
            self.calendar_var = 1
            self.frame2 = Frame(self.canvas)
            self.main_page.add_widgetpack(self.frame2, fill=X, side=TOP)
            self.frame3 = Frame(self.canvas, bg='black')
            self.main_page.add_widgetpack(self.frame3, fill='both', side=TOP, expand=1)
            self.button_left = Button(self.frame2, text='<', width=20, command=back, relief='flat')
            self.main_page.add_widgetpack(self.button_left, side=LEFT)
            self.month_label = Label(self.frame2, text='month')
            self.main_page.add_widgetpack(self.month_label, side=LEFT, expand=1, fill='both')
            self.button_right = Button(self.frame2, text='>', width=20, command=forward, relief='flat')
            self.main_page.add_widgetpack(self.button_right, side=LEFT)
            for n in range(7):
                self.lbl = Label(self.frame3, text=calendar.day_abbr[n], width=4, height=3, fg='darkblue',
                                 font='Arial 10 bold')
                self.main_page.add_widgetgrid(self.lbl, column=0, row=n)
            self.days = []
            self.dtasks = []
            self.ddone = []
            self.dmark = []
            for col in range(6):
                for row in range(7):
                    self.box = Frame(self.frame3, width=6)
                    self.main_page.add_widgetgrid(self.box, row=row, column=col + 1, padx=2, pady=2)
                    self.label_date = Label(self.box, text='0', width=2, height=3)
                    self.days.append(self.label_date)
                    self.main_page.add_widgetpack(self.label_date, side=LEFT)
                    self.inbox = Frame(self.box)
                    self.main_page.add_widgetpack(self.inbox, side=LEFT)

                    self.button_task = Calendar_button(master=self.inbox, tgroup=self.classes[self.classpicked.get()],
                                                       index=col * 7 + row + 1, id=self.id, text='task', relief=RIDGE)
                    self.button_task.config(command=self.button_task.show_task)
                    self.dtasks.append(self.button_task)
                    self.main_page.add_widgetpack(self.button_task, side=TOP)

                    self.button_done = Calendar_button(master=self.inbox, tgroup=self.classes[self.classpicked.get()],
                                                       index=col * 7 + row + 1, id=self.id, text='done', relief=RIDGE)
                    self.button_done.config(command=self.button_task.show_answers)
                    self.ddone.append(self.button_done)
                    self.main_page.add_widgetpack(self.button_done, side=TOP)

                    self.mark = Label(self.box, text='M')
                    self.dmark.append(self.mark)
                    self.main_page.add_widgetpack(self.mark, side=LEFT)
            self.main_page.draw_all_widgets()
            self.get_other_materials()
            self.fill()

        self.canvas = Canvas(self.main_page.root, bg='cadetblue4')
        self.main_page.add_widgetpack(self.canvas,side=LEFT, fill='both', expand=1)
        self.frame_profile = Frame(self.main_page.root, width=200, bg='#8A3324')
        self.main_page.add_widgetpack(self.frame_profile, side=RIGHT, fill='both')
        self.distance_holder = Frame(self.frame_profile, width=200, height=10, bg='#8A3324')
        self.main_page.add_widgetpack(self.distance_holder, side=TOP, fill='both')

        self.button_profile = Button_profile(id = self.id, password=self.info[2], master=self.frame_profile, text=f'name + surname', relief='flat', width=20)
        self.main_page.add_widgetpack(self.button_profile, side=TOP)
        self.button_profile.config(command=self.button_profile.show_profile1)

        self.distance_holder = Frame(self.frame_profile, width=200, height=10, bg='#8A3324')
        self.main_page.add_widgetpack(self.distance_holder, side=TOP, fill='both')
        self.frame1 = Frame(self.canvas, height=100, bg='cadetblue4')
        self.main_page.add_widgetpack(self.frame1, fill=X, side=TOP, padx=5, pady=5)
        self.button_calendar = Button(self.frame1, text='calendar', command=calendar_button , relief='flat', width=20)
        self.main_page.add_widgetpack(self.button_calendar, side=LEFT)
        self.paddingframe=Frame(self.frame1, width=10, bg='cadetblue4')
        self.main_page.add_widgetpack(self.paddingframe, side=LEFT)
        self.button_list = Button(self.frame1, text='list', command=list_button, relief='flat', width=20)
        self.main_page.add_widgetpack(self.button_list, side=LEFT)
        self.get_classes(self.role)
        list_button()

    def set_username(self, name, surname):
        self.button_profile.config(text=str(surname+" "+name))
    def get_classes(self, role):
        self.classes = get_classes(role, self.id)
        self.classes_window = window_with_scrolls(self.main_page, self.frame_profile, height=100, width=10)
        self.classes_holder = self.classes_window.return_container()
        for i in range(len(self.classes)):
            self.radiobutton = Radiobutton(self.classes_holder, text=self.classes[i], variable=self.classpicked,
                                           value=i, command=self.get_other_materials)
            self.main_page.add_widgetgrid(self.radiobutton, column=0, row=i, pady=6)
        self.main_page.draw_all_widgets()
    def get_other_materials(self):
        try:
            self.content_window.destroy()
            self.button.destroy()
        except:
            pass
        self.content_window = window_with_scrolls(self.main_page, self.canvas, height=200)
        self.content_holder = self.content_window.return_container()
        if self.calendar_var:
            self.content_window.taskholder.config(height=200, width=200)
            a = load_other_materials(self.classes[self.classpicked.get()])
            for i in range(len(a)):
                self.nameholder = Frame(self.content_holder)
                self.main_page.add_widgetgrid(self.nameholder, column=0, row=i + 1, padx=10, pady=10)
                self.label = Label(self.nameholder, text=a[i])
                self.main_page.add_widgetpack(self.label, side=LEFT)
                self.download_button = Button_other_materials(master=self.nameholder, text='download', filename=a[i], parent=self.main_page,
                                                              base='other_materials',
                                                              group=self.classes[self.classpicked.get()])
                self.main_page.add_widgetpack(self.download_button, side=RIGHT)
                self.download_button.config(command=self.download_button.download)
            self.main_page.draw_all_widgets()
        else:
            self.content_window.taskholder.config(height=600, width=800)
            rows = logs_db.db(self.classes[self.classpicked.get()]).return_selflength()
            logs = get_logs(self.classes[self.classpicked.get()], rows)
            for i in logs:
                logs_db.db(self.classes[self.classpicked.get()]).add_log(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            logs = logs_db.db(self.classes[self.classpicked.get()]).return_logs()
            for i in range(len(logs)):
                i = -(i+1)
                if logs[i][3]=='added a task':
                    self.nameholder = Frame(self.content_holder)
                    self.main_page.add_widgetgrid(self.nameholder, column=0, row=-i, padx=10, pady=10)
                    text = 'teacher '+str(logs[i][3])+' '+str(logs[i][2])+' at'+str(datetime.datetime.fromtimestamp(int(logs[i][4])))
                    self.label = Label(self.nameholder, text=text)
                    self.main_page.add_widgetpack(self.label, side=LEFT)
                    self.download_button = Button_other_materials(master=self.nameholder, text='download', filename=logs[i][2], base=pickle.loads(logs[i][7]), group=self.classes[self.classpicked.get()])
                    self.main_page.add_widgetpack(self.download_button, side=RIGHT)
                    self.download_button.config(command=self.download_button.download)
            self.main_page.draw_all_widgets()


    def fill(self):
        self.month_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
        month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            self.prev_month = 12
            back_month_days = calendar.monthrange(self.year - 1, 12)[1]
        else:
            self.prev_month = self.month - 1
            back_month_days = calendar.monthrange(self.year, self.month - 1)[1]
        week_day = calendar.monthrange(self.year, self.month)[0]

        if self.month == 12:
            self.next_month = 1
        else:
            self.next_month = self.month + 1

        for n in range(month_days):
            self.days[n + week_day]['text'] = n + 1
            self.days[n + week_day]['bg'] = '#f3f3f3'
            self.dtasks[n + week_day].set_date(self.year, self.month, n + 1)
            self.dtasks[n + week_day].set_group(self.classes[self.classpicked.get()])
        for n in range(week_day):
            self.days[n]['text'] = back_month_days - (week_day - n) + 1
            self.days[n]['bg'] = 'gray'
            self.dtasks[n].set_date(self.year, self.prev_month, back_month_days - (week_day - n) + 1)
            self.dtasks[n].set_group(self.classes[self.classpicked.get()])
        a = 1
        for n in range(42 - (42 - (month_days + week_day)), 42):
            self.days[n]['text'] = a
            self.days[n]['bg'] = 'gray'
            self.dtasks[n].set_date(self.year, self.next_month, a)
            self.dtasks[n].set_group(self.classes[self.classpicked.get()])
            a += 1
    def run(self):
        self.main_page.run()


if __name__=="__main__":
    window = main_page()
    window.run()