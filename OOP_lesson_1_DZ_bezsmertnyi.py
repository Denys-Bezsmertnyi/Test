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
from abc import abstractmethod
class Chess():
    def __init__(self,color,position): #цвет - строка, позиция - тюпл
        self.color = color
        self.position = position
    def change_color(self): #ничего не возвращаем, меняем значение цвета
        if self.color == "білий":
            self.color = "чорний"
        else:
            self.color = "білий"

    def _is_valid_position(self,x,y): #x - int, y - int
        return 0<=x<=7 and 0<=y<=7 #возвращаем bool

    def can_move_to_position(self,new_position): #new_position - тюпл из 2 значений
        if len(new_position) == 2:
            x,y = new_position
            return self._is_valid_position(x,y) #вернёт bool
        return False

    def change_position(self,new_position): #new_position - тюпл из 2 значений
        if self.can_move_to_position(new_position): #если True, меняем значение позиции на новое
            self.position = new_position
        else:
            print("Дошка не настільки велика, оло!")
    @abstractmethod
    def can_reach_to_position(self,new_position): #new_position - тюпл из 2 значений, вернёт bool
        pass

#во всех остальных классах принцип одинаковый, берем значение новой позиции
#и проверяем ограничения от 0 до 7, и потом смотрим для каждой фигуры, можно ли переместить на новую позицию.
#в конце возвращаем bool значение
class Pawn(Chess):
    def can_reach_to_position(self, new_position):
        x, y = new_position
        if not self._is_valid_position(x,y):
            return False
        if self.color == "білий":
            return x == self.position[0] and y == self.position[1] + 1
        if self.color == "чорний":
            return x == self.position[0] and y == self.position[1] - 1

class Horse(Chess):
    def can_reach_to_position(self,new_position):
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x == 2 and difference_y == 1) or (difference_x == 1 and difference_y == 2)
class Bishop(Chess):
    def can_reach_to_position(self,new_position):
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return difference_x == difference_y and x != self.position[0]
class Rook(Chess):
    def can_reach_to_position(self,new_position):
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x == 0) or (difference_y == 0)
class Queen(Chess):
    def can_reach_to_position(self,new_position):
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x == 0) or (difference_y == 0) or difference_x == difference_y
class King(Chess):
    def can_reach_to_position(self,new_position):
        x,y = new_position
        if not self._is_valid_position(x,y):
            return False
        difference_x = abs(x - self.position[0])
        difference_y = abs(y - self.position[1])
        return (difference_x <= 1 and difference_y <= 1)


def can_all_figures_reach_to_new_position(figures,new_position): #передаю в функцию список моих объектов фигур и тюпл с 2 позициями
    reach_true = []
    for figure in figures:
        if figure.can_reach_to_position(new_position):
            reach_true.append(figure)
    return reach_true #возвращаю список фигур, которые могут переместиться на новую позицию

pawn = Pawn("білий", (1, 1)) #цвет и позиция фигуры
bishop = Bishop("білий", (2, 2))
horse = Horse("Чорний", (3,2))
rook = Rook("білий", (4, 1))
queen = Queen("Чорний", (1, 3))
king = King("Чорний", (3, 3))

figures = [pawn,bishop,horse,rook,queen,king] #закидываем фигуры в список, чтобы проще было обрабатывать
new_position = (1,4) #новая позиция

reach = can_all_figures_reach_to_new_position(figures,new_position)
for figure in reach:
    print(f"{figure.color} {figure.__class__.__name__}") #вывод фигур, которые можно переместить на новую позицию

# chase1 = Chess("чорний",(2,3))
# chase1.change_color()
# print(chase1.color)
# chase1.change_position((1,3))
# print(chase1.position)


