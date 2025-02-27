class Vehicle:
    """     
    Базовый класс для всех транспортных средств
    """    
    def __init__(self, max_speed):
        """
        Конструктор базового класса Vehicle.
        Инициализирует свойства, общие для всех транспортных средств.
        :param max_speed: Максимальная скорость транспортного средства.
        """
        self._speed = 0  # Текущая скорость (инкапсуляция: скрыта от прямого доступа)
        self._max_speed = max_speed  # Максимальная скорость

    @property
    def speed(self):
        """
        Геттер для текущей скорости.
        :return: Текущая скорость транспортного средства.
        """
        return self._speed

    @property
    def max_speed(self):
        """
        Геттер для максимальной скорости.
        :return: Максимальная скорость транспортного средства.
        """
        return self._max_speed

    def increase_speed(self, increment):
        """
        Увеличивает скорость транспортного средства на заданное значение.
        Скорость не может превышать максимальную.
        :param increment: Значение, на которое увеличивается скорость.
        """
        self._speed = min(self._speed + increment, self._max_speed)

    def decrease_speed(self, decrement):
        """
        Уменьшает скорость транспортного средства на заданное значение.
        Скорость не может быть меньше 0.
        :param decrement: Значение, на которое уменьшается скорость.
        """
        self._speed = max(self._speed - decrement, 0)

    def __call__(self):
        """
        Перегрузка метода __call__. Позволяет вызывать объект как функцию.
        :return: Строка с информацией о текущей скорости.
        """
        return f"Текущая скорость: {self._speed} км/ч"


class Bus(Vehicle):
    '''
    Класс Bus наследует от Vehicle
    '''
    def __init__(self, capacity, max_speed):
        """
        Конструктор класса Bus.
        Инициализирует свойства автобуса, включая пассажиров и места.
        :param capacity: Вместимость автобуса (максимальное количество пассажиров).
        :param max_speed: Максимальная скорость автобуса.
        """
        super().__init__(max_speed)  # Инициализация базового класса Vehicle
        self._capacity = capacity  # Вместимость автобуса
        self._passengers = []  # Список имен пассажиров
        self._seats = {i: None for i in range(1, capacity + 1)}  # Словарь мест (место: пассажир)

    @property
    def capacity(self):
        """
        Геттер для вместимости автобуса.
        :return: Максимальное количество пассажиров.
        """
        return self._capacity

    @property
    def passengers(self):
        """
        Геттер для списка пассажиров.
        :return: Список имен пассажиров в автобусе.
        """
        return self._passengers

    @property
    def has_empty_seats(self):
        """
        Проверяет, есть ли в автобусе свободные места.
        :return: True, если есть свободные места, иначе False.
        """
        return any(seat is None for seat in self._seats.values())

    def board_passenger(self, name):
        """
        Посадка пассажира в автобус.
        :param name: Имя пассажира.
        :raises ValueError: Если в автобусе нет свободных мест.
        """
        if not self.has_empty_seats:
            raise ValueError("Нет свободных мест")
        # Находим первое свободное место и сажаем пассажира
        for seat_number, occupant in self._seats.items():
            if occupant is None:
                self._seats[seat_number] = name
                self._passengers.append(name)
                break

    def disembark_passenger(self, name):
        """
        Высадка пассажира из автобуса.
        :param name: Имя пассажира.
        :raises ValueError: Если пассажира с таким именем нет в автобусе.
        """
        if name not in self._passengers:
            raise ValueError(f"{name} is not on the bus")
        # Находим место пассажира и освобождаем его
        for seat_number, occupant in self._seats.items():
            if occupant == name:
                self._seats[seat_number] = None
                self._passengers.remove(name)
                break

    def __contains__(self, name):
        """
        Перегрузка оператора 'in'. Позволяет проверять, есть ли пассажир в автобусе.
        :param name: Имя пассажира.
        :return: True, если пассажир в автобусе, иначе False.
        """
        return name in self._passengers

    def __iadd__(self, name):
        """
        Перегрузка оператора '+='. Позволяет сажать пассажира в автобус.
        :param name: Имя пассажира.
        :return: self (текущий объект Bus).
        """
        self.board_passenger(name)
        return self

    def __isub__(self, name):
        """
        Перегрузка оператора '-='. Позволяет высаживать пассажира из автобуса.
        :param name: Имя пассажира.
        :return: self (текущий объект Bus).
        """
        self.disembark_passenger(name)
        return self

    def __call__(self):
        """
        Перегрузка метода __call__. Позволяет вызывать объект как функцию.
        :return: Строка с информацией о количестве пассажиров и текущей скорости.
        """
        return f"Bus with {len(self._passengers)} passengers, current speed: {self._speed} km/h"


# Пример использования
if __name__ == "__main__":
    # Создаем автобус вместимостью 50 человек и максимальной скоростью 100 км/ч
    bus = Bus(capacity=50, max_speed=100)

    # Сажаем пассажиров
    bus += "Alice"
    bus += "Bob"

    # Выводим информацию о автобусе
    print(bus())  # Вызов метода __call__

    # Проверяем, есть ли пассажир в автобусе
    print("Alice in bus:", "Alice" in bus)  # Использование операции in

    # Увеличиваем скорость автобуса
    bus.increase_speed(30)
    print(bus())  # Текущая скорость увеличена

    # Высаживаем пассажира
    bus -= "Alice"
    print(bus())  # Вызов метода __call__ после высадки пассажира