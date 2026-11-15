import threading
import time
global Count

Threads = []
T = 8
valor = 0
M = 200000
Count = 0
Semaforo = threading.Semaphore(1)


def Soma():
    global Count
    for j in range(M):
        Semaforo.acquire()
        try:
            valor = Count
            time.sleep(0)
            Count = valor + 1
        finally:
            Semaforo.release()

for i in range(T):
    t = threading.Thread(target=Soma)
    t.start()
    Threads.append(t)
for t in Threads:
    t.join()

print("Esperado", T*M)
print("Resultado", Count)