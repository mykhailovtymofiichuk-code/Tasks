password = input("Введіть пароль: ")

if len(password) < 8:
    print("Пароль занадто короткий")

elif password.isdigit():
    print("Пароль не повинен складатися тільки з цифр")

elif password.isalpha():
    print("Пароль не повинен складатися тільки з букв")

else:
    print("Пароль виглядає достатньо надійним")