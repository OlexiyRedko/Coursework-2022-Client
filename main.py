import login_page
import main_student_page
import main_teacher_page


print("started")
page1=login_page.login_page()
page1.run()

info = page1.get_info()

#info[id, login, password, role, name, surname, lastname, photo]
if info[3]=="student":
    page2 = main_student_page.main_page(info)
    page2.set_username(info[4], info[5])
    page2.run()

if info[3]=="teacher":
    page2=main_teacher_page.main_page(info)
    page2.set_username(info[4], info[5])
    page2.run()




print('end')