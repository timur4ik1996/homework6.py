# Словарь
my_dict = {"Igor": 1996, "Ivan": 1997, "Nastya": 1991}
print(my_dict)
print(my_dict.get("Igor"))
print(my_dict.get("Katy"))
my_dict.update({"Yra": 1987,"Sasha": 2000})
a = my_dict.pop("Ivan")
print(a)
print(my_dict)

# Множество
my_set = {6, 8, 3, 4, 6, 4, 5, 4, 12}
print(my_set)
print(my_set.add(22))
print(my_set.add(26))
print(my_set.remove(6))
print(my_set)
