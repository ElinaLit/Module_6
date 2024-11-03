class Vehicle:
    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self.model = _model
        self.engine_power = _engine_power
        self.color = _color

    def __str__(self):
        return self.owner, self.model, self.color

    _COLOR_VARIANTS = ['black', 'blue', 'red', 'green', 'yellow', 'white']

    def get_model(self):
        return f'Модель: {self.model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        #return f'{self.get_model}, {self.get_horsepower}, {self.get_color}, Владелец: {self.owner}, sep="\n"'
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep="\n")
    def set_color(self, new_color: str):
        if new_color.lower() in  self._COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'yellow', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()