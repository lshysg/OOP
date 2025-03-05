class Roman:
    """Класс Roman реализует работу с римскими числами."""

    # Константы класса
    ARABIC_MIN = 1
    ARABIC_MAX = 3999
    ROMAN_MIN = "I"
    ROMAN_MAX = "MMMCMXCIX"

    LETTERS = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
    NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, value):
        """Инициализация класса."""
        if not isinstance(value, (int, str)):
            raise TypeError(f"Не могу создать римское число из {type(value)}")

        if isinstance(value, int):
            self.__check_arabic(value)
            self._arabic = value
        elif isinstance(value, str):
            self._arabic = self.to_arabic(value)

    def __add__(self, other):
        """Создать новый объект как сумму 'self' и 'other'."""
        if isinstance(other, Roman):
            return Roman(self._arabic + other._arabic)
        elif isinstance(other, int):
            return Roman(self._arabic + other)
        else:
            raise TypeError(f"Не могу сложить Roman с {type(other)}")

    def __sub__(self, other):
        """Создать новый объект как разность self и other."""
        if isinstance(other, Roman):
            return Roman(self._arabic - other._arabic)
        elif isinstance(other, int):
            return Roman(self._arabic - other)
        else:
            raise TypeError(f"Не могу вычесть {type(other)} из Roman")

    def __mul__(self, other):
        """Создать новый объект как произведение self и other."""
        if isinstance(other, Roman):
            return Roman(self._arabic * other._arabic)
        elif isinstance(other, int):
            return Roman(self._arabic * other)
        else:
            raise TypeError(f"Не могу умножить Roman на {type(other)}")

    def __floordiv__(self, other):
        """Создать новый объект как частное self и other."""
        if isinstance(other, Roman):
            return Roman(self._arabic // other._arabic)
        elif isinstance(other, int):
            return Roman(self._arabic // other)
        else:
            raise TypeError(f"Не могу разделить Roman на {type(other)}")

    def __truediv__(self, other):
        """Создать новый объект как частное self и other."""
        return self.__floordiv__(other)

    def __str__(self):
        """Вернуть строковое представление класса."""
        return Roman.to_roman(self._arabic)

    @staticmethod
    def __check_arabic(value):
        """Возбудить исключение ValueError, если 'value' не принадлежит
        [ARABIC_MIN; ARABIC_MIN]."""
        if not (Roman.ARABIC_MIN <= value <= Roman.ARABIC_MAX):
            raise ValueError(f"Арабское число {value} должно быть в диапазоне [{Roman.ARABIC_MIN}; {Roman.ARABIC_MAX}]")

    @staticmethod
    def __check_roman(value):
        """Возбудить исключение ValueError, если 'value' содержит
        недопустимые символы (не входящие в LETTERS)."""
        for char in value:
            if char not in Roman.LETTERS:
                raise ValueError(f"Римское число содержит недопустимый символ: {char}")

    @property
    def arabic(self):
        """Вернуть арабское представление числа."""
        return self._arabic

    @staticmethod
    def to_arabic(roman):
        """Преобразовать римское число 'roman' в арабское."""
        def letter_to_number(letter):
            """Вернуть арабское значение римской цифры 'letter'."""
            letter = letter.upper()
            if letter == 'M':
                return 1000
            elif letter == 'D':
                return 500
            elif letter == 'C':
                return 100
            elif letter == 'L':
                return 50
            elif letter == 'X':
                return 10
            elif letter == 'V':
                return 5
            elif letter == 'I':
                return 1
            else:
                raise ValueError(f"Недопустимая римская цифра: {letter}")

        Roman.__check_roman(roman)

        i = 0
        value = 0

        while i < len(roman):
            number = letter_to_number(roman[i])
            i += 1

            if i == len(roman):
                value += number
            else:
                next_number = letter_to_number(roman[i])
                if next_number > number:
                    value += next_number - number
                    i += 1
                else:
                    value += number

        Roman.__check_arabic(value)
        return value

    @staticmethod
    def to_roman(arabic):
        """Преобразовать арабское число 'arabic' в римское."""
        Roman.__check_arabic(arabic)

        roman = ""
        n = arabic

        for i, number in enumerate(Roman.NUMBERS):
            while n >= number:
                roman += Roman.LETTERS[i]
                n -= Roman.NUMBERS[i]

        return roman