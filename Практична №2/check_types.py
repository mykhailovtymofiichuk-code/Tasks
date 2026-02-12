# Створення змінної temp1 типу int
temp1 = 42

# Створення змінної temp2 типу float
temp2 = 3.14

# Створення змінної temp3 типу str
temp3 = "Python"

# Створення змінної temp4 типу bool
temp4 = True

# Створення змінної temp5 типу int (0 — це теж int)
temp5 = 0

# Виведення значення temp1 та його типу
print("temp1 =", temp1, "| Тип:", type(temp1))

# Виведення значення temp2 та його типу
print("temp2 =", temp2, "| Тип:", type(temp2))

# Виведення значення temp3 та його типу
print("temp3 =", temp3, "| Тип:", type(temp3))

# Виведення значення temp4 та його типу
print("temp4 =", temp4, "| Тип:", type(temp4))

# Виведення значення temp5 та його типу
print("temp5 =", temp5, "| Тип:", type(temp5))

# Перетворення значення (bool) у числове (int)
converted_value = int(temp4)

# Виведення результату конвертації
print("Числове значення temp4:", converted_value)

# Перевірка типу після конвертації
print("Тип після конвертації:", type(converted_value))
