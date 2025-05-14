#include <iostream>
#include <string>

class Session { // Дополнительный класс
private:
    std::string date;
    std::string time;
    std::string movieName;

public:
    // Геттеры
    std::string getDate() { return date; }
    std::string getTime() { return time; }
    std::string getMovieName() { return movieName; }

    // Сеттеры
    void setDate(std::string d) { date = d; }
    void setTime(std::string t) { time = t; }
    void setMovieName(std::string m) { movieName = m; }

    // Перегруженные методы установки свойств
    void setProperties() {
        std::string input;
        std::cout << " Date: ";
        std::getline(std::cin, input);
        setDate(input);

        std::cout << " Time: ";
        std::getline(std::cin, input);
        setTime(input);

        std::cout << " Movie name: ";
        std::getline(std::cin, input);
        setMovieName(input);
    }

    void setProperties(std::string d, std::string t, std::string m) {
        setDate(d);
        setTime(t);
        setMovieName(m);
    }
};

class Cinema { // Основной класс
private:
    std::string name;
    std::string address;
    Session sessions[10];

public:
    // Геттеры и сеттеры
    std::string getName() { return name; }
    std::string getAddress() { return address; }

    void setName(std::string n) { name = n; }
    void setAddress(std::string a) { address = a; }

    // Добавление сеанса
    void addSession(Session s, int index) {
        if (index >= 0 && index < 10) {
            sessions[index] = s;
        }
    }

    // Получение сеанса
    Session getSession(int index) {
        if (index >= 0 && index < 10) {
            return sessions[index];
        }
        return Session(); // Возвращаем пустой объект по умолчанию
    }
};

int main() {
    Cinema cinema;
    std::string input1, input2, input3;

    std::cout << "Enter cinema name: ";
    std::getline(std::cin, input1);
    cinema.setName(input1);

    std::cout << "Enter cinema address: ";
    std::getline(std::cin, input2);
    cinema.setAddress(input2);

    // Первые 2 сеанса — метод без параметров
    for (int i = 0; i < 5; i++) {
        std::cout << "\nEnter details for Session " << i + 1 << ":\n";
        Session session;
        session.setProperties();
        cinema.addSession(session, i);
    }

    // Остальные 2 сеанса — метод с параметрами
    for (int i = 5; i < 10; i++) {
        std::cout << "\nEnter details for Session " << i + 1 << ":\n";
        std::cout << " Date: ";
        std::getline(std::cin, input1);

        std::cout << " Time: ";
        std::getline(std::cin, input2);

        std::cout << " Movie name: ";
        std::getline(std::cin, input3);

        Session session;
        session.setProperties(input1, input2, input3);
        cinema.addSession(session, i);
    }

    // Вывод информации
    std::cout << "\n\n=== Cinema Information ===\n";
    std::cout << "Name: " << cinema.getName() << "\n";
    std::cout << "Address: " << cinema.getAddress() << "\n";

    std::cout << "\n=== Sessions ===\n";
    for (int i = 0; i < 10; i++) {
        Session s = cinema.getSession(i);
        std::cout << "Session " << i + 1 << ": "
                  << "Date: " << s.getDate() << ", "
                  << "Time: " << s.getTime() << ", "
                  << "Movie: " << s.getMovieName() << "\n";
    }

    return 0;
}
