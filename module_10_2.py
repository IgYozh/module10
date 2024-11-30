from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        enemies = 100
        days = 0
        print(f'Сир {self.name} на нас напали!')
        for i in range(enemies):
            if enemies > 0:
                time.sleep(1)
                days += 1
                enemies -= self.power
                print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')
                if enemies <= 0:
                    print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все сражения закончены!")