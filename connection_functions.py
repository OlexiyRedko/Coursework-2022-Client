import shelve
import socket
import pickle
import time
import complex_window_parts
from threading import*

headsize = 10
command_size = 6
title = 5
adress = ""

class connection:
    def __init__(self):
        self.client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((adress, 12345))
    def get_client(self):
        return self.client



def login(login, password, ip):
    global adress
    adress = ip
    client = connection().get_client()
    a = str(login) + " " + str(password)
    client.send(str(f'{len(a):<{headsize}}' + "login " + a).encode("utf-8"))
    header = int(client.recv(headsize).decode('utf-8'))
    data = client.recv(header)
    data = pickle.loads(data)
    counter2 = 0
    data2 = b''
    print(data[7])
    while counter2 < data[7]:
        data2 += client.recv(800)
        counter2 += 800
    #data[7] = data2
    print("done all here")
    return data
    try:
        pass
    except Exception:
        print(Exception)


def upload_other_materials(filename, group):
    try:
        client=connection().get_client()
        print(filename)
        with open(filename, 'rb') as file:
            f = file.read()
        filename = filename.split("/")
        filename = filename[len(filename) - 1]
        length = filename.encode('utf-8')
        length2 = group.encode('utf-8')
        print(str(f'{len(f):<{headsize}}' + "upl om" + f'{len(length):<{title}}' + filename+ f'{len(length2):<{title}}' + group))
        client.send(
            str(f'{len(f):<{headsize}}' + "upl om" + f'{len(length):<{title}}' + filename+ f'{len(length2):<{title}}' + group).encode('utf-8') + f)
        client.close()
    except Exception:
        print(Exception)

def upload_task(group ,base, filename):
    try:
        client = connection().get_client()
        year, month, day = base
        with open(filename, 'rb') as file:
            f = file.read()
        filename = filename.split("/")
        filename = filename[len(filename) - 1]
        length = filename.encode('utf-8')
        length2 = group.encode('utf-8')
        basenew = str(year)+"!"+str(month)+"!"+str(day)
        length3=basenew.encode('utf-8')
        client.send(str(f'{len(f):<{headsize}}' + "upltas"+f'{len(length2):<{title}}'+group+f'{len(length3):<{title}}'+basenew+f'{len(length):<{title}}'+filename).encode('utf-8')+f)
        client.close()
    except Exception:
        print(Exception)

def upload_homework(group ,base, filename, id):
    client = connection().get_client()
    month, day = base
    with open(filename, 'rb') as file:
        f = file.read()
    filename = filename.split("/")
    filename = filename[len(filename) - 1]
    length = filename.encode('utf-8')
    length2 = group.encode('utf-8')
    basenew = str(month) + "!" + str(day) + "!" + str(id)
    length3 = basenew.encode('utf-8')
    client.send(
        str(f'{len(f):<{headsize}}' + "uplhom" + f'{len(length2):<{title}}' + group + f'{len(length3):<{title}}' + basenew + f'{len(length):<{title}}' + filename).encode(
            'utf-8') + f)
    client.close()
    try:
        pass
    except Exception:
        print(Exception)

def get_classes(role, id):
    try:
        client = connection().get_client()
        a = str(role)+" "+str(id)
        client.send(str(f'{len(a):<{headsize}}retcla'+a).encode('utf-8'))
        header = client.recv(headsize).decode('utf-8')
        data = client.recv(int(header))
        data = pickle.loads(data)
        client.close()
        return data
    except Exception:
        print(Exception)

def load_other_materials(group):
    try:
        client = connection().get_client()
        group = group.encode('utf-8')
        client.send(str(f'{len(group):<{headsize}}retom ').encode('utf-8')+group)
        header = client.recv(headsize).decode('utf-8')
        data = client.recv(int(header))
        data = pickle.loads(data)
        client.close()
        return data
    except Exception:
        print(Exception)

def download_data(group ,base, filename, answer=None, ):
    try:
        client = connection().get_client()
        if base == 'other_materials':
            a = str(group + '!' + base + "!" + filename).encode('utf-8')
            client.send(str(f'{len(a):<{headsize}}dload ').encode('utf-8') + a)
        else:
            month, day = base
            print(base)
            if answer:
                a = str(group + "!" + month + '!' + str(day) + "!" + filename).encode('utf-8')
                client.send(str(f'{len(a):<{headsize}}dload1').encode('utf-8') + a)
            else:
                a = str(group + "!" + month + '!' + str(day) + "!" + filename).encode('utf-8')
                client.send(str(f'{len(a):<{headsize}}dload ').encode('utf-8') + a)
        header = int(client.recv(headsize).decode("utf-8")[:headsize])
        titlelen = int(client.recv(5).decode('utf-8'))
        print(titlelen)
        if titlelen == 0:
            print("File doesn't exist already")
            return "Error"
        title = client.recv(titlelen).decode('utf-8')
        a1 = time.time()
        data = 0
        with open(title, 'wb') as f:
            while data < header:
                f.write(client.recv(800))
                data += 800
            print("len " + str(data))
            f.close()
        b1 = time.time()
        print("end")
        print(b1 - a1)
        client.close()
    except Exception:
        print(Exception)

def delete_data(group ,base, filename, answer=None):
    try:
        client = connection().get_client()
        if base == 'other_materials':
            a = str(group + '!' + base + "!" + filename).encode('utf-8')
            client.send(str(f'{len(a):<{headsize}}del1  ').encode('utf-8') + a)
        else:
            year, month, day = base
            if answer:
                a = str(group + "!" + month + str(year) + '!' + str(day) + "!" + filename).encode('utf-8')
                client.send(str(f'{len(a):<{headsize}}del2  ').encode('utf-8') + a)
            else:
                a = str(group + "!" + month + str(year) + '!' + str(day) + "!" + filename).encode('utf-8')
                client.send(str(f'{len(a):<{headsize}}del1  ').encode('utf-8') + a)
        client.close()
    except Exception:
        print(Exception)




def tasks_for_day(group, month, day):
    try:
        client = connection().get_client()
        date=group+'!'+month+'!'+str(day)
        print(date)
        date = date.encode('utf-8')
        client.send(str(f'{len(date):<{headsize}}rettas').encode('utf-8')+date)
        header = client.recv(headsize).decode('utf-8')
        data = client.recv(int(header))
        data = pickle.loads(data)
        client.close()
        return data
    except Exception:
        print(Exception)

def answers_for_task(group, month, day, id=None):
    try:
        client = connection().get_client()
        date = group + '!' + month + '!' + str(day)
        if id!=None:
            date = date +"!"+str(id)
        print(date)
        date = date.encode('utf-8')
        client.send(str(f'{len(date):<{headsize}}rethom').encode('utf-8') + date)
        header = client.recv(headsize).decode('utf-8')
        data = client.recv(int(header))
        data = pickle.loads(data)
        client.close()
        return data
    except Exception:
        print(Exception)

def set_mark(group, year, month, day, mark, filename):
    client = connection().get_client()
    f = mark.encode('utf-8')
    length = filename.encode('utf-8')
    length2 = group.encode('utf-8')
    basenew = str(year) + "!" + str(month) + "!" + str(day)
    length3 = basenew.encode('utf-8')
    client.send(str(f'{len(f):<{headsize}}').encode('utf-8'))
    client.send(str("smark " + f'{len(length2):<{title}}' + group ).encode('utf-8'))
    client.send(str(f'{len(length3):<{title}}' + basenew).encode('utf-8') )
    client.send(str(f'{len(length):<{title}}' + filename).encode('utf-8') + f)
    client.close()
    print("sent"+mark)

def get_mark(group, year, month, day, filename):
    client = connection().get_client()
    length = filename.encode('utf-8')
    length2 = group.encode('utf-8')
    basenew = str(year) + "!" + str(month) + "!" + str(day)
    length3 = basenew.encode('utf-8')
    client.send(str(f'{len(length):<{headsize}}').encode('utf-8'))
    client.send(str("gmark " + f'{len(length2):<{title}}' + group ).encode('utf-8'))
    client.send(str(f'{len(length3):<{title}}' + basenew).encode('utf-8') )
    client.send(str(filename).encode('utf-8') )
    header = int(client.recv(headsize).decode("utf-8")[:headsize])
    mark = client.recv(header).decode('utf-8')
    client.close()
    print("sent"+mark)
    return mark

def get_logs(group, rows):
    client = connection().get_client()
    f = group.encode('utf-8')
    client.send(str(f'{len(f):<{headsize}}'+'glogs '+f'{rows:<{title}}').encode('utf-8')+f)
    header = int(client.recv(headsize).decode("utf-8")[:headsize])
    logs = pickle.loads(client.recv(header))
    client.close()
    return logs

def return_Name(id):
    client = connection().get_client()
    f = str(id).encode('utf-8')
    client.send(str(f'{len(f):<{headsize}}' + 'retnam').encode('utf-8')+f)
    header = int(client.recv(headsize).decode("utf-8")[:headsize])
    name = client.recv(header)
    name = pickle.loads(name)
    return name

def get_info(id ,photo=1):
    client = connection().get_client()
    a = str(id)
    if photo:
        client.send(str(f'{len(a):<{headsize}}' + "getinf" + a).encode("utf-8"))
        header = client.recv(headsize).decode('utf-8')
        print("header " + str(header))
        counter = 0
        data = b''
        while counter < int(header):
            data += client.recv(1024)
            counter += 1024
        data = pickle.loads(data)
        client.close()
        return data
    else:
        client.send(str(f'{len(a):<{headsize}}' + "getin2" + a).encode("utf-8"))
        header = client.recv(headsize).decode('utf-8')
        print("header " + str(header))
        counter = 0
        data = b''
        while counter < int(header):
            data += client.recv(1024)
            counter += 1024
        data = pickle.loads(data)
        client.close()
        return data

def send_info_changes(id, password, name, name2, name3):
    client = connection().get_client()
    a = str(str(id)+" "+str(password)+" "+str(name)+" "+str(name2)+" "+str(name3))
    print(a)
    f = a.encode('UTF-8')
    client.send(str(f'{len(f):<{headsize}}' + 'infch ').encode('utf-8') + f)
def send_picture_changes(id, password, picturename):
    with open(picturename, 'rb') as file:
        picture = file.read()
    client = connection().get_client()
    f = pickle.dumps([str(id), str(password), picture])
    client.send(str(f'{len(f):<{headsize}}' + 'pictch').encode('utf-8') + f)
    header = client.recv(headsize).decode('utf-8')
    data = client.recv(int(header))
    return data



#if __name__=="__main__":
 #pass