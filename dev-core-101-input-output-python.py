name = input("Введите Ваше имя: ")
age = input("Введите Ваш возраст: ")

print(f"Привет, {name}. Тебе {age} лет.")

age = int(age)

if age <= 100:
    print(100-age+2024)
else:
    print("Вам более 100 лет.")
