import json
from typing import Self

class Time:
    """
    Класс Time представляет время в формате часов, минут и секунд.
    Поддерживает операции сложения, вычитания, сохранения и загрузки из JSON-файла,
    а также преобразование времени в секунды и обратно.
    """

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        """
        Инициализация объекта Time.        
        """
        if not self.is_valid_time(hours, minutes, seconds):
            raise ValueError("Invalid time value")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        """
        Возвращает строковое представление времени в формате "HH:MM:SS".
        """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __add__(self, other: Self) -> Self:
        """
        Сложение двух объектов Time.
        """
        total_seconds = self.to_seconds() + other.to_seconds()
        return self.from_seconds(total_seconds)

    def __sub__(self, other: Self) -> Self:
        """
        Вычитание одного объекта Time из другого.
        """
        total_seconds = self.to_seconds() - other.to_seconds()
        return self.from_seconds(total_seconds)

    @classmethod
    def from_string(cls, str_value: str) -> Self:
        """
        Создает объект Time из строки в формате "HH:MM:SS".
        """
        hours, minutes, seconds = map(int, str_value.split(':'))
        return cls(hours, minutes, seconds)

    def save(self, filename: str) -> None:
        """
        Сохраняет объект Time в JSON-файл.
        """
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def load(self, filename: str) -> None:
        """
        Загружает объект Time из JSON-файла.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        self.hours = data['hours']
        self.minutes = data['minutes']
        self.seconds = data['seconds']

    def to_seconds(self) -> int:
        """
        Преобразует время в общее количество секунд.
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, seconds: int) -> Self:
        """
        Создает объект Time из общего количества секунд.
        """
        # Нормализация времени
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        # Если часы >= 24, оставляем остаток от деления на 24
        hours %= 24
        return cls(hours, minutes, seconds)

    @staticmethod
    def is_valid_time(hours: int, minutes: int, seconds: int) -> bool:
        """
        Проверяет, является ли время корректным.
        """
        return 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60