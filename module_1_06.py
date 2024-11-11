my_dict = {"Леонид": 2000, "Вася": 2024, "Кирилл": 2012}
print(my_dict)
my_dict["Артем"] = 1988
print(my_dict)
print(my_dict.get("Леонид"))
print(my_dict.get("Артем"))
my_dict.update({"Саша": 1998,
                "Валя": 2003})
print(my_dict)
del my_dict["Артем"]
print(my_dict.get("Артем")) #- нет значения - вывести невозможно
print(my_dict)
my_set = {"DFm", 2, 9 , 35.1, 2, 9,"DFm", "Sokol", 1998} # Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями
print(my_set) # Выведите на экран множество my_set (должны отобразиться только уникальные значения)
my_set.add(5) # если добавить один элемент
print(my_set)
my_set.update([6,12,49,6,12,49,50,51])#  если добавить несколько элементов
print(my_set)
print(my_set.discard(9))
print(my_set)

