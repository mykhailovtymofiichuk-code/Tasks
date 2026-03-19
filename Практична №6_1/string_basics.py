full_name = "Іван Петренко"

# В Python відлік починається з 0, бо так працює більшість мов програмування.
# Тобто:
# І = 0, в = 1, а = 2 і т.д.

print("Перший символ:", full_name[0])
print("Третій символ:", full_name[2])
print("Останній символ:", full_name[-1])


# Крок 3: Розділення імені та прізвища

user_input = input("Введіть ім'я та прізвище: ")

# Знаходимо пробіл
space_index = user_input.find(" ")

# Робимо зрізи
first_name = user_input[:space_index]
last_name = user_input[space_index + 1:]

print("Ім'я:", first_name)
print("Прізвище:", last_name)