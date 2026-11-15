import threading
import time
global Count

Threads = []
T = 8
valor = 0
M = 200000
Count = 0

def Soma():
    global Count
    for j in range(M):
        valor = Count
        time.sleep(0)
        Count = valor + 1

for i in range(T):
    t = threading.Thread(target=Soma)
    t.start()
    Threads.append(t)
for t in Threads:
    t.join()

print("Esperado", T*M)
print("Resultado", Count)