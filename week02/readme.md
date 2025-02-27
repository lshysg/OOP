# Week02

### Практическая работа

## Класс «Автобус»

Класс представляет собой модель автобуса и включает следующие свойства и методы.

---

### Свойства:
- **`speed`** (скорость) — текущая скорость автобуса.
- **`capacity`** (вместимость) — максимальное количество пассажиров.
- **`maxSpeed`** (максимальная скорость) — предельная скорость автобуса.
- **`passengers`** (пассажиры) — список имен пассажиров.
- **`hasEmptySeats`** (наличие свободных мест) — булевое значение, указывающее, есть ли свободные места.
- **`seats`** (места) — словарь, представляющий места в автобусе.

---

### Методы:
1. **Посадка и высадка пассажиров:**
   - Посадка одного или нескольких пассажиров.
   - Высадка одного или нескольких пассажиров.

2. **Управление скоростью:**
   - Увеличение скорости на заданное значение.
   - Уменьшение скорости на заданное значение.

3. **Операции:**
   - Оператор `in` — проверка наличия пассажира с заданной фамилией.
   - Оператор `+=` — посадка пассажира(ов) с заданной фамилией.
   - Оператор `-=` — высадка пассажира(ов) с заданной фамилией.

---

### Пример использования:

```python
# Создание объекта автобуса
class Bus:
    def __init__(self, speed, capacity, maxSpeed):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed
        self.passengers = []
        self.seats = {}

    def __iadd__(self, passenger):
        if isinstance(passenger, list):
            self.passengers.extend(passenger)
        else:
            self.passengers.append(passenger)
        return self

    def __isub__(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
        return self

    def __contains__(self, passenger):
        return passenger in self.passengers

    def increase_speed(self, value):
        self.speed = min(self.speed + value, self.maxSpeed)

    def decrease_speed(self, value):
        self.speed = max(self.speed - value, 0)

# Пример использования
bus = Bus(speed=60, capacity=50, maxSpeed=100)

# Посадка пассажиров
bus += "Иванов"
bus += ["Петров", "Сидоров"]

# Увеличение скорости
bus.increase_speed(20)

# Проверка наличия пассажира
if "Иванов" in bus:
    print("Иванов в автобусе")

# Высадка пассажира
bus -= "Петров"