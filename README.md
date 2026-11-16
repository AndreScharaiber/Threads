# Threads
André Luís Scharaiber Alves
Python
Link para o YouTube: https://youtu.be/HIDJYEyITbg

Atividade 1 - Jantar dos Filósofos

Neste trabalho, programei o clássico problema do jantar dos filósofos proposto por Dijkstra
Nele, usei um Semaphore com valor 4, que permite que apenas esse número de filósofos tentem pegar os garfos simultaneamente. Desta forma, evitamos a espera circular de Coffman.
Assim, enquanto alguns filósofos estão comendo, outros podem estar pensando, ou, esperando para pegar os garfos
Essa solução garante que o deadlock não aconteça, mas não garante fairness, já que, o mesmo filósofo pode continuar pegando o garfo diversas vezes

Prints: Com deadlock 
<img width="1155" height="264" alt="Screenshot 2026-11-15 at 22 42 26" src="https://github.com/user-attachments/assets/f054ad7c-b7cc-49bb-a69f-1114de7cc362" />

Prints: Sem deadlock
<img width="1163" height="369" alt="Screenshot 2026-11-15 at 22 43 25" src="https://github.com/user-attachments/assets/2bc29a41-c4fb-4963-bca8-78676686a916" />

Para executar, basta rodar ambos Jantar.py e JantarSemaphore.py

Atividade 2 - Contador 

Nesta atividade, foram feitos dois contadores. Um sem semaphore, e um usando o semaphore.
No contador onde não foi usado o semaphore, as threads podem adicionar ao contador ao mesmo tempo, o que pode causar que uma das somas não registre, já que uma delas pode ter somado em um número anterior. Para simular isso em python, separei o contador em etapas, já que o GIL garante que apenas uma thread irá acessar o contador por vez. 
Mas, quebrando o contador e adicionando um time.sleep de 0, consegui fazer com que ambas pudessem acabar acessando ao mesmo tempo, como pode ser visualizado nas prints a seguir

Com Semaphore
<img width="777" height="264" alt="Screenshot 2026-11-15 at 22 55 40" src="https://github.com/user-attachments/assets/120fd436-bef9-4938-b7bd-55c677e831b8" />

Sem Semaphore
<img width="742" height="268" alt="Screenshot 2026-11-15 at 22 53 38" src="https://github.com/user-attachments/assets/dce3899f-b695-4c8c-bafa-988440465688" />

O Trade-off disso é que, na versão correta, há um tempo de espera do acquire e release, ou seja, causa um pequeno delay, como pode ser observado nas capturas de tela. Mas, garante que todos os números estão somados um por um. (Não sei fazer tabelas no Git, mas as prints ali mostram certinho o tempo de execução de cada um dos 3 testes).
Em resumo, a função do Semaphore aqui, é garantir que a próxima thread sempre lerá o valor atualizado, já que, sem ele, uma pode acabar lendo o valor anterior, e as duas podem acabar somando o mesmo valor, o que acaba em perdas, como mostrado nas prints causando o Happens-before, ou, barreiras implícitas, do release de uma thread ao acquire da próxima.


Para rodar, basta executar os códigos Contador.py e ContadorSemaphore.py

Atividade 3 - Deadlock

Nessa atividade, foram feitos dois programas utilizando duas threads e dois locks (A e B). Na primeira versão, cada thread pega um lock diferente e tenta pegar o outro, causando uma espera circular. Para facilitar isso, utilizei um time.sleep(0.05) entre as aquisições, dando tempo para ambas pegarem o primeiro lock.

As 4 condições de Coffman

Exclusão mútua: Cada lock só pode ser utilizado por uma thread por vez
Manter e esperar; A thread espera infinitamente pelo recurso, prendendo o outro recurso
Não preempção: Nenhuma thread consegue tirar o lock da outra
Espera circular: As threads irão esperar pelo item que está preso na outra thread

Prints Com deadlock
<img width="1070" height="182" alt="Screenshot 2026-11-15 at 23 10 21" src="https://github.com/user-attachments/assets/ab97d786-c12c-4bd8-b33f-67a1d261bed2" />

Para corrigir, mudei a ordem de aquisição dos locks fazendo com que ambas as threads pegassem primeiro A e depois B. Assim, quenro a espera circular evitando que o deadlock aconteça

Prints Sem deadlock
<img width="1066" height="289" alt="Screenshot 2026-11-15 at 23 10 44" src="https://github.com/user-attachments/assets/7041813a-66aa-4806-9084-06fec0fb312e" />

Para rodar, basta executar os códigos Deadlock.py e DeadlockHierarquico.py





