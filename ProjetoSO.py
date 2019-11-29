import threading as t
import random
from time import sleep

class Contacorrente:
    def __init__(self, num, saldo):
        self.num = num
        self.saldo = saldo

    def relatorio(self):
        print(f"\nConta {self.num}")
        print(f"Saldo: R$ {self.saldo}")

    def transfere(self, destino, valor, lock):
        lock.acquire()
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            print(f"\nTransação concluída com sucesso!")
            print(f"Saldo da conta {self.num}: R$ {self.saldo}")
            print(f"Saldo da conta {destino.num}: R$ {destino.saldo}")
        else:
            print(f"\nTransação negada! Saldo insuficiente.")

        lock.release()

if __name__ == '__main__':
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    lock = t.Lock()
    C1 = Contacorrente(1, 100)
    C2 = Contacorrente(2, 100)
    C1.relatorio()
    C2.relatorio()

    for i in range(0, 100):
        thread1 = t.Thread(C2.transfere(C1, x, lock))
        thread2 = t.Thread(C1.transfere(C2, y, lock))
        sleep(0.1)
        thread1.start()
        sleep(0.1)
        thread2.start()
        sleep(0.1)
    C1.relatorio()
    C2.relatorio()