from typing import Dict, Tuple

class TimeDeposit:
    """Абстрактный класс - срочный вклад."""

    def __init__(self, name: str, interest_rate: float, period_limit: Tuple[int, int], sum_limit: Tuple[float, float]) -> None:
        """Инициализировать атрибуты класса."""
        self.name: str = name
        self._interest_rate: float = interest_rate
        self._period_limit: Tuple[int, int] = period_limit
        self._sum_limit: Tuple[float, float] = sum_limit
        self._check_self()

    def __str__(self) -> str:
        """Вернуть строковое представление депозита."""
        return (f"Наименование:       {self.name}\n"
                f"Валюта:             {self.currency}\n"
                f"Процентная ставка:  {self._interest_rate}\n"
                f"Срок (мес.):        [{self._period_limit[0]}; {self._period_limit[1]})\n"
                f"Сумма:              [{self._sum_limit[0]:,.2f}; {self._sum_limit[1]:,.2f})")

    @property
    def currency(self) -> str:
        return "руб."  # Не изменяется

    def _check_self(self) -> None:
        """Проверить, что данные депозита являются допустимыми."""
        assert 0 < self._interest_rate <= 100, "Неверно указан процент по вкладу!"
        assert 1 <= self._period_limit[0] < self._period_limit[1], "Неверно указаны ограничения по сроку вклада!"
        assert 0 < self._sum_limit[0] <= self._sum_limit[1], "Неверно указаны ограничения по сумме вклада!"

    def _check_user_params(self, initial_sum: float, period: int) -> None:
        """Проверить, что данные депозита соответствуют его ограничениям."""
        is_sum_ok: bool = self._sum_limit[0] <= initial_sum < self._sum_limit[1]
        is_period_ok: bool = self._period_limit[0] <= period < self._period_limit[1]
        assert is_sum_ok and is_period_ok, "Условия вклада не соблюдены!"

    def get_profit(self, initial_sum: float, period: int) -> float:
        """Вернуть прибыль по вкладу вклада клиента."""
        self._check_user_params(initial_sum, period)
        return initial_sum * self._interest_rate / 100 * period / 12

    def get_sum(self, initial_sum: float, period: int) -> float:
        """Вернуть сумму вклада клиента после начисления прибыли."""
        return initial_sum + self.get_profit(initial_sum, period)


class BonusTimeDeposit(TimeDeposit):
    """Cрочный вклад c получением бонуса к концу срока вклада."""

    def __init__(self, name: str, interest_rate: float, period_limit: Tuple[int, int], sum_limit: Tuple[float, float], bonus: Dict[str, float]) -> None:
        """Инициализировать атрибуты класса."""
        super().__init__(name, interest_rate, period_limit, sum_limit)
        self._bonus: Dict[str, float] = bonus
        self._check_self()

    def __str__(self) -> str:
        """Вернуть строковое представление депозита."""
        return (super().__str__() + "\n"
                f"Бонус (%):          {self._bonus['percent']}\n"
                f"Бонус (мин. сумма): {self._bonus['sum']:,.2f}")

    def _check_self(self) -> None:
        """Проверить, что данные депозита являются допустимыми."""
        super()._check_self()
        assert 0 < self._bonus['percent'] <= 100, "Неверно указан процент бонуса!"
        assert 0 < self._bonus['sum'], "Неверно указана минимальная сумма для бонуса!"

    def get_profit(self, initial_sum: float, period: int) -> float:
        """Вернуть прибыль по вкладу вклада клиента."""
        profit: float = super().get_profit(initial_sum, period)
        if initial_sum > self._bonus['sum']:
            profit += profit * self._bonus['percent'] / 100
        return profit


class CompoundTimeDeposit(TimeDeposit):
    """Cрочный вклад c ежемесячной капитализацией процентов."""

    def __str__(self) -> str:
        """Вернуть строковое представление депозита."""
        return (super().__str__() + "\n"
                f"Капитализация %   : Да")

    def get_profit(self, initial_sum: float, period: int) -> float:
        """Вернуть прибыль по вкладу вклада клиента."""
        self._check_user_params(initial_sum, period)
        return initial_sum * (1 + self._interest_rate / 100 / 12) ** period - initial_sum


# Данные для создания депозитов
deposits_data: Dict[str, float | Tuple[int, int] | Tuple[float, float]] = dict(interest_rate=5, period_limit=(6, 18), sum_limit=(1000, 100000))

# Список имеющихся депозитов
deposits: Tuple[TimeDeposit, BonusTimeDeposit, CompoundTimeDeposit] = (
    TimeDeposit("Сохраняй", interest_rate=5, period_limit=(6, 18), sum_limit=(1000, 100000)),
    BonusTimeDeposit("Бонусный", **deposits_data, bonus=dict(percent=5, sum=2000)),
    CompoundTimeDeposit("С капитализацией", **deposits_data)
)