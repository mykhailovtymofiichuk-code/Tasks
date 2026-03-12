letter = input("Введіть букву: ")

vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"

if letter in vowels:
    print("Це голосна буква")
else:
    print("Це не голосна буква")