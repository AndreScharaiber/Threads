import threading
import time

N = 5

garfo0 = threading.Lock()
garfo1 = threading.Lock()
garfo2 = threading.Lock()
garfo3 = threading.Lock()
garfo4 = threading.Lock()
garfos = [garfo0, garfo1, garfo2, garfo3, garfo4]

def come(p):
    print(p, "Comendo")
    time.sleep(2)

def pensa(p):
    print(p, "Pensando")
    time.sleep(2)

def fome(p):
    print(p, "Com fome")
    time.sleep(2)

def garfo_esquerda(p):
    return p

def garfo_direita(p):
    return (p + 4) % 5

def pegagarfos (p):
    direita = garfo_direita(p)
    esquerda = garfo_esquerda(p)

    garfos[esquerda].acquire()
    time.sleep(1)
    garfos[direita].acquire()

def largargarfo (p):
    direita = garfo_direita(p)
    esquerda = garfo_esquerda(p)

    garfos[esquerda].release()
    time.sleep(1)
    garfos[direita].release()


def filosofo(p):

    while True:
        pensa(p)
        fome(p)
        pegagarfos(p)
        come(p)
        largargarfo(p)


t1 = threading.Thread(target=filosofo, args=(0,))
t2 = threading.Thread(target=filosofo, args=(1,))
t3 = threading.Thread(target=filosofo, args=(2,))
t4 = threading.Thread(target=filosofo, args=(3,))
t5 = threading.Thread(target=filosofo, args=(4,))


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
