# Домашнее задание по теме "Множественное наследование"

class Horse:

    def __init__(self):
        self.x_distance : int= 0
        self.sound : str = 'Frrr'
        super().__init__() # Отправка поиска по mro() в Eagle, что не нашло в Horse... В случае с sound -
                           # принимает последнее значение, которое находит последним в Eagle

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:

    def __init__(self):
        self.y_distance : int = 0
        self.sound : str = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    
    def __init__(self):
        super().__init__() # Отправка поиска по mro() в Horse

    def move(self, dx, dy):
             return f"({super().run(dx)}, {super().fly(dy)})" # run находит по mro() в Horse, fly в Eagle

    def get_pos(self):
        return f"({self.x_distance}, {self.y_distance})"

    def voice(self):
        print(self.sound) # Первый sound находит в Horse, но в Horse отправка поиска в Eagle,
                          # откуда и берётся выводимый sound



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()