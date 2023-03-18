number = 0
while number < 1 or number > 100000:
    number = int(input("Введите число от 1 до 100000: "))

simple = True

i = 2
while i < number:
    if number % i == 0:
        simple = False
        break
    i += 1
print("Число ", number," простое: ", simple)

