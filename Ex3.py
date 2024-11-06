number_for_game = 4267
count_guess = 0
number_of_user = int(input("Введите число: "))
while number_of_user != number_for_game:
    if number_of_user > number_for_game:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif number_of_user < number_for_game:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    count_guess += 1
    number_of_user = int(input("Введите число: "))
print(f"Вы угадали! Количество попыток: {count_guess}")
    

