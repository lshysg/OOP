from time_pr import Time

# Создание объектов Time
t1 = Time(10, 30, 45)
t2 = Time(14, 15, 20)

# Вывод времени
print("Time 1:", t1)
print("Time 2:", t2)

# Сложение и вычитание времени
t3 = t1 + t2
t4 = t2 - t1

print("Time 1 + Time 2:", t3)
print("Time 2 - Time 1:", t4)

# Сохранение и загрузка времени
t1.save("time1.json")
t1.load("time1.json")
print("Loaded Time 1:", t1)

# Преобразование времени в секунды и обратно
seconds = t1.to_seconds()
t5 = Time.from_seconds(seconds)
print("Time 1 in seconds:", seconds)
print("Time from seconds:", t5)

# Проверка корректности времени
print("Is 25:70:80 a valid time?", Time.is_valid_time(25, 70, 80))