# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'


class Prince(Human):
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size

    def is_shoe_fits(self, list_of_cinderellas):
        for cinderella in list_of_cinderellas:
            if self.foot_size == cinderella['foot']:
                return f'{self.name} і {cinderella["name"]} гойра весіллє '



class Cinderella(Human):
    def __init__(self, name, age, foot):
        super().__init__(name, age)
        self.foot = foot


ira = Cinderella('Ira', 16, 35).__dict__
katya = Cinderella('Katya', 23, 41).__dict__
olya = Cinderella('Olya', 22, 38).__dict__
khrystyna = Cinderella('Khrystyna', 20, 36).__dict__
vika = Cinderella('Vika', 17, 36).__dict__
sophia = Cinderella('Sophia', 21, 37).__dict__

list_of_cinderellas = [ira, katya, olya, khrystyna, vika, sophia]

rostyslav = Prince('Rostyslav', 20, 36)

love_story = Prince.is_shoe_fits(rostyslav, list_of_cinderellas)
print(love_story)

# =================================================================
# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
