price = float(input("Введіть суму покупки: "))
age = int(input("Ваш вік: "))
student = input("Ви студент? (yes/no): ")
vip = input("VIP клієнт? (yes/no): ")
weekend = input("Сьогодні вихідний? (yes/no): ")
birthday = input("Сьогодні ваш день народження? (yes/no): ")

discount = 0

# 50%
if vip == "yes":
    discount = 50

elif student == "yes" and weekend == "yes" and price > 500:
    discount = 50

# 30%
elif student == "yes" or age < 14 or age > 60:
    discount = 30

# 15%
elif weekend == "yes":
    discount = 15

# День народження
if birthday == "yes":
    discount = discount * 2
    if discount > 70:
        discount = 70

final_price = price - (price * discount / 100)

print("Початкова ціна:", price)
print("Знижка:", discount, "%")
print("Фінальна ціна:", final_price)