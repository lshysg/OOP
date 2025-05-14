from time_pr import Time
from time_collection import TimeCollection

# Создаем несколько объектов Time
t1 = Time(8, 20, 15)
t2 = Time(9, 45, 30)
t3 = Time(23, 59, 59)

# Создаем коллекцию и добавляем объекты
collection = TimeCollection()
collection.add(t1)
collection.add(t2)
collection.add(t3)

# Вывод коллекции
print("Initial collection:")
print(collection)

# Удаление и вывод после удаления
collection.remove(1)
print("\nAfter removing second element:")
print(collection)

# Сохраняем в файл
collection.save("times.json")

# Загружаем новую коллекцию из файла
new_collection = TimeCollection()
new_collection.load("times.json")
print("\nLoaded collection from file:")
print(new_collection)
