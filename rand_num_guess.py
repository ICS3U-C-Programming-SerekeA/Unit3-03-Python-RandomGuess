# !/usr/bin/env python3
# created by: Sereke Asfeday
# Date: 15, October, 2026
# This program generates a random number between 1 and 9 then asks the user to guess.
# if tgey guessed correct it displays a message that they guessed correctly,
# if not it displays a message that they guessed incorrectly.

import random


def main():
    # generate a random number between 1 and 9
    random_number = random.randint(1, 9)

    # the program will ask the user for their guess
    user_input = int(input("Guess a number between 1 and 9: "))

    if user_input == random_number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct number was", random_number)


if __name__ == "__main__":
    main()
