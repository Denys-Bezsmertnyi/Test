# Опишіть клас для фігури шахів.
#
# Фігура повинна містити такі атрибути:
#
# Колір (білий або чорний) Місце на дошці (тут є варіанти, або два окремих поля, для опису координат або одне, але,
# наприклад, кортеж з двох чисел) І такі методи як: Змінити колір (нічого не приймає, тільки змінює колір на
# протилежний) Змінити місце на дошці (приймає або дві змінні або один кортеж з двох елементів), не забудьте
# перевірити, що ми не намагаємося поставити фігуру за межі дошки (обидва значення від 0 до 7) Абстрактний метод
# перевірки потенційного ходу (деталі нижче) На даному етапі фігури можуть стояти на одній і ті ж клітині,
# поки нам це не важливо Опишіть класи, для пішака, коня, офіцера, тури, ферзя та короля. Все що в них потрібно
# додати - це один метод для перевірки, чи можливо за один хід поміняти місце фігури на дошці (всі ходять по-різному,
# пішаки мають ще й відмінність від кольору). Метод приймає знову ж таки або дві цифри, або один кортеж. І знову ж
# таки перевіряємо чи не виходить значення за межі дошки (оскільки нам потрібен цей функціонал двічі, бажано робити
# його як окремий захищений метод у батьківському класі). І функцію, яка приймає список фігур та потенційну нову
# клітинку, а повертає список із фігур. Але тільки тих, які можуть за один хід дістатися цієї клітини.
#
# * Скрізь описати типізації (у функціях, атрибутах та методах)
from typing import List, Tuple
from abc import ABC, abstractmethod
class Chess(ABC):
    def __init__(self, color: str, position: Tuple[int, int]):
        self.color = color
        self.position = position
    def change_color(self) -> None:
        if self.color == "білий":
            self.color = "чорний"
        else:
            self.color = "білий"
    def _is_valid_position(self, x: int, y: int) -> bool:
        return 0<=x<=7 and 0<=y<=7

    def can_move_to_position(self, new_position: Tuple[int, int]) -> bool:
        if len(new_position) == 2:
            x,y = new_position
            return self._is_valid_position(x,y)
        return False

    def change_position(self, new_position: Tuple[int, int]) -> None:
        if self.can_move_to_position(new_position):
            self.position = new_position
        else:
            print("Дошка не настільки велика, оло!")

    @abstractmethod
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        pass

class Pawn(Chess):
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        x, y = new_position
        if not self._is_valid_position(x,y):
            return False
        if self.color == "білий":
            return x == self.position[0] and y == self.position[1] + 1
        if self.color == "чорний":
            return x == self.position[0] and y == self.position[1] - 1

class Horse(Chess):
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x == 2 and difference_y == 1) or (difference_x == 1 and difference_y == 2)
class Bishop(Chess):
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return difference_x == difference_y and x != self.position[0]
class Rook(Chess):
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x == 0) or (difference_y == 0)
class Queen(Chess):
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x == 0) or (difference_y == 0) or difference_x == difference_y
class King(Chess):
    def can_reach_to_position(self, new_position: Tuple[int, int]) -> bool:
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x <= 1 and difference_y <= 1)


def can_all_figures_reach_to_new_position(figures: List[Chess], new_position: Tuple[int, int]) -> List[Chess]:
    reach_true = []
    for figure in figures:
        if figure.can_reach_to_position(new_position):
            reach_true.append(figure)
    return reach_true

pawn = Pawn("білий", (1, 1))
bishop = Bishop("білий", (2, 2))
horse = Horse("Чорний", (3,2))
rook = Rook("білий", (4, 1))
queen = Queen("Чорний", (1, 3))
king = King("Чорний", (3, 3))

figures = [pawn,bishop,horse,rook,queen,king]
new_position = (1,4)

reach = can_all_figures_reach_to_new_position(figures,new_position)
for figure in reach:
    print(f"{figure.color} {figure.__class__.__name__}")

# chase1 = Chess("чорний",(2,3))
# chase1.change_color()
# print(chase1.color)
# chase1.change_position((1,3))
# print(chase1.position)

#PHONE Lesson
class Phone:
    number = ''
    _incoming_call = 0

    def set_phone_number(self, number):
        self.number = number

    def _get_incoming_call(self):
        return self._incoming_call

    def adding_income_calls(self):
        self._incoming_call += 1


phone1 = Phone()
phone2 = Phone()
phone3 = Phone()
phone1.set_phone_number('380663902048')
phone2.set_phone_number('380993902048')
phone3.set_phone_number('380503902048')
phone1._get_incoming_call()
phone1.adding_income_calls()
phone2.adding_income_calls()
phone3.adding_income_calls()
phone3.adding_income_calls()

col = [phone1, phone2, phone3]
sum = 0
for i in col:
    sum += i._get_incoming_call()
print(sum)


