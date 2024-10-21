class Vehicle:
    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color
        self.__COLOR_VARIANTS = {'blue', 'red', 'green', 'black', 'white'}

    #def __str__(self):
    #    kv = str(self.__COLOR_VARIANTS)
    #    return kv

    def print_info(self):
        print(f'Модель:' + self.model)
        print(f'Мощность двигателя:' + str(self.engine_power))
        print(f'Цвет:' + self.color)
        print(f'Владелец:' + self.owner)

    def get_model(self):
        return print(f'Модель: ' + self.model)

    def get_horsepower(self):
        return print(f'Мощность двигателя: ' + str(self.engine_power))

    def get_color(self):
        return print(f'Цвет: ' + self.color)

    def set_color(self, new_color):
        for  color in self.__COLOR_VARIANTS:
                if new_color.lower() == color.lower():
                    self.color = new_color
                    break
        else:
            print(f'Нельзя сменить цвет на ' + new_color)

    def set_owner(self, owner):
        self.owner = owner


class Sedan(Vehicle):
    def __init__(self,__owner: str, __model: str, __color: str, __engine_power: int, __passengers_limit: int = 5):
        super().__init__(__owner,__model, __color, __engine_power)
        self.__PASSENGERS_LIMIT = 5

    #def __str__(self):
    #    return str(self.__COLOR_VARIANTS)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
