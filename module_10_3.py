import threading
import random
import time
from threading import Thread, Lock


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            a = random.randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a} ₽. Баланс:{self.balance} ₽')
            time.sleep(0.001)



    def take(self):
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x} ₽')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие:{x} ₽. Баланс: {self.balance} ₽')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)




bk = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread2 = threading.Thread(target=Bank.take, args=(bk,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bk.balance} ₽')

