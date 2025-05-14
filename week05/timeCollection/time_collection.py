import json
from time_pr import Time

class TimeCollection:
    """
    Класс-контейнер для хранения объектов Time.
    """
    def __init__(self, initial_data=None):
        # Инициализация контейнера, при необходимости можно передать список объектов Time
        self._data = initial_data if initial_data else []

    def __str__(self):
        # Удобное строковое представление всех объектов Time в коллекции
        return "\n".join(f"{idx}: {time}" for idx, time in enumerate(self._data))

    def __getitem__(self, index):
        # Позволяет получать элементы по индексу или срезу
        return self._data[index]

    def add(self, value: Time):
        # Добавляет объект Time в коллекцию
        if not isinstance(value, Time):
            raise TypeError("Можно добавлять только объекты Time")
        self._data.append(value)

    def remove(self, index: int):
        # Удаляет объект Time по индексу
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Индекс вне диапазона")

    def save(self, filename: str):
        # Сохраняет коллекцию в JSON-файл
        with open(filename, 'w') as file:
            json.dump([time.__dict__ for time in self._data], file)

    def load(self, filename: str):
        # Загружает коллекцию из JSON-файла
        with open(filename, 'r') as file:
            raw_data = json.load(file)
        self._data = [Time(**item) for item in raw_data]
