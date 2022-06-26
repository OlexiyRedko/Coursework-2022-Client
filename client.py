import socket
from threading import*
from time import sleep
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.88.127", 12345))
x=0
y=0
data = None

def send_request():
    global x
    while True:
        client.send("login admin admin".encode("utf-8"))
        x = x + 1
        sleep(0.0001)

def get_answer():
    global y
    global data
    while True:
        data = client.recv(1024).decode("utf-8")
        if data != None:
            y=y+1

def print_everything():
    global x
    global y
    global data
    while True:
        print("x="+str(x)+" y="+str(y)+" data="+str(data))

t1 = Thread(target=send_request)
t2 = Thread(target=get_answer)
t3 = Thread(target=print_everything)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()

t3.join()
client.close()




