from random import randint
num = randint(1, 1000)
print("Я хочу сыграть с тобой в игру =)\n"
      "Угадай за 10 попыток число от 1 до 1000")

for i in range(10):
    print("Попытка № ", i+1)
    guess = int(input())
    if guess == num:
        print("Угадал! ", num)
        break
    if i == 9:
        print("Не угадал, ха-ха-ха! Я загадал: ", num)
        break
    elif guess < num:
        print("Больше ;)")
    elif guess > num:
        print("Меньше ;)")


