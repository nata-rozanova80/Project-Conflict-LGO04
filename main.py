import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его!")

    while not guessed:
        player_guess = input("Введите ваше предположение: ")

        # Проверяем, является ли ввод числом
        if not player_guess.isdigit():
            print("Пожалуйста, введите число.")
            continue

        player_guess = int(player_guess)
        attempts += 1

        if player_guess < number_to_guess:
            print("Слишком низко! Попробуйте еще раз.")
        elif player_guess > number_to_guess:
            print("Слишком высоко! Попробуйте еще раз.")
        else:
            guessed = True
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")

if __name__ == "__main__":
    guess_the_number()
