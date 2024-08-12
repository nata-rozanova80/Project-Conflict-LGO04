import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Приветствуем вас в игре 'Угадай число'!")
    print("Я загадал число от 1 до 100. Удачи!")

    while not guessed:
        player_guess = input("Введите ваше предположение: ")

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
            print(f"Вы сделали это! Число было {number_to_guess}, и вы угадали его за {attempts} попыток!")

        if __name__ == "__main__":  # Обратите внимание на правильное использование __name__
            guess_the_number()