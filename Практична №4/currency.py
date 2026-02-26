uah = float(input("Сума в гривнях: "))
rate = float(input("Курс долара: "))

# Розрахунок конвертації
usd = uah / rate

# :.2f у f-рядку каже Python залишити рівно 2 знаки після коми
print(f"Результат: {usd:.2f} USD")