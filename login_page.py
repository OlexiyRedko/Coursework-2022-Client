from WindowClassFile import *
import connection_functions
import shelve

class login_page():
    def __init__(self):
        self.a=0
        self.login_page = Window(400, 400)
        self.label1 = Label(self.login_page.root, text="Введіть свої дані")
        self.login_page.add_widget(self.label1, 140, 120)
        self.label2 = Label(self.login_page.root, text="логін")
        self.login_page.add_widget(self.label2, 80, 160)
        self.label3 = Label(self.login_page.root, text="пароль")
        self.login_page.add_widget(self.label3, 65, 200)
        self.entry1 = Entry(self.login_page.root, width=20)
        self.login_page.add_widget(self.entry1, 130, 160)
        self.entry2 = Entry(self.login_page.root, show='*', width=20)
        self.login_page.add_widget(self.entry2,  130, 200)
        self.entry3 = Entry(self.login_page.root, width=20)
        self.login_page.add_widget(self.entry3, 130, 300)
        self.label4 = Label(self.login_page.root, text="")
        self.login_page.add_widget(self.label4, 65, 280)
        def __show_pswd():
            self.entry2.config(show='')
            self.button1.config(command=__hide_pswd)
        def __hide_pswd():
            self.entry2.config(show='*')
            self.button1.config(command=__show_pswd)
        def check_data():
            a = connection_functions.login(self.entry1.get(), self.entry2.get(), self.entry3.get())
            if a==0:
                self.label4.config(text="Невірні дані або профіля неіснує")
            elif a==None:
                self.label4.config(text="Немає зв'язку з сервером")
            else:
                with shelve.open("login", 'c') as file:
                    file['login']=self.entry1.get()
                    file['password']=self.entry2.get()
                    file['adress']=self.entry3.get()
                self.a = a
                self.login_page.root.destroy()

        self.button1 = Button(self.login_page.root, text='👁', command=__show_pswd)
        self.login_page.add_widget(self.button1, 300, 200)
        self.button2 = Button(self.login_page.root, text='Вхід', command=check_data)
        self.login_page.add_widget(self.button2, 250, 230)
        with shelve.open("login", 'c') as file:
            if 'login' in file.keys():
                self.entry1.insert(0, file['login'])
            if 'password' in file.keys():
                self.entry2.insert(0, file['password'])
            if 'adress' in file.keys():
                self.entry3.insert(0, file['adress'])
    def get_info(self):
        return self.a

    def run(self):
        self.login_page.run()
