from typing import List
from deposit import TimeDeposit

if __name__ == "__main__":
    print("Добро пожаловать в систему подбора вкладов!")

    while True:
        print("\n-----")
        print("Нажмите 1, чтобы подобрать вклад, или что угодно для выхода.")

        answer: str = input()
        if answer == "1":
            initial_sum: float = float(input("1/2: Введите начальную сумму вклада: "))
            period: int = int(input("2/2: Введите срок вклада (мес.): "))

            matched_deposits: List[TimeDeposit] = []
            for deposit in deposits:
                try:
                    deposit._check_user_params(initial_sum, period)
                    matched_deposits.append(deposit)
                except AssertionError:
                    pass

            if len(matched_deposits) > 0:
                print("{0:18} | {1:13} | {2:13}".format(
                    "Вклад", "Прибыль", "Итоговая сумма"
                ))
                for deposit in matched_deposits:
                    print("{0:18} | {1:8,.2f} {3:4} | {2:8,.2f} {3:4}".format(
                          deposit.name,
                          deposit.get_profit(initial_sum, period),
                          deposit.get_sum(initial_sum, period),
                          deposit.currency))
            else:
                print("К сожалению, нет подходящих Вам вкладов.")

        else:
            break

    print("\nСпасибо, что воспользовались терминалом банка! До встречи!")