import threading
import time

A = threading.Lock()
B = threading.Lock()

def Thread1():
    A.acquire()
    print("T1 pegou A")
    time.sleep(0.05)
    print("T1 esperando B")
    print(threading.enumerate())
    B.acquire()
    print("T1 pegou B")
    print("T1 Finalizada")
    B.release()
    print("T1 Liberou B")
    A.release()
    print("T1 Liberou A")

def Thread2():
    B.acquire()
    print("T2 pegou B")
    time.sleep(0.05)
    print("T2 esperando A")
    print(threading.enumerate())
    A.acquire()
    print("T2 pegou A")
    print("T2 Finalizada")
    A.release()
    print("T2 Liberou A")
    B.release()
    print("T2 Liberou B")

t1 = threading.Thread(target=Thread1)
t2 = threading.Thread(target=Thread2)

t1.start()
t2.start()

t1.join()
t2.join()