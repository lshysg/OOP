from терминал import Терминал

if __name__ == "__main__":
    терминал1: Терминал = Терминал()
    print(терминал1)
    while True:
        терминал1.показать_меню()
        пункт_меню: str = input()
        терминал1.обработать_команду(пункт_меню)