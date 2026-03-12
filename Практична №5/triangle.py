a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

if a + b > c and a + c > b and b + c > a:
    print("Такий трикутник може існувати")
else:
    print("Такий трикутник НЕ може існувати")