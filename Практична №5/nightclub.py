age = int(input("Введіть ваш вік: "))
passport = input("Чи маєте паспорт? (yes/no): ")
vip = input("Чи є ви VIP? (yes/no): ")

# VIP має пріоритет
if vip == "yes" and passport == "yes" and age >= 18:
    print("Вхід дозволено (VIP)")

# Загальні правила
elif age >= 18 and passport == "yes":
    print("Вхід дозволено")

# Причини відмови

elif age <= 18 and passport == "yes" and vip == "yes":
    print("Вхід заборонено: якщо тобі немає 18 років то у тебе немає паспорта")

elif age < 18:
    print("Вхід заборонено: вам немає 18 років")

elif passport != "yes":
    print("Вхід заборонено: потрібен паспорт")