import random

play_again = 'y'


while play_again == 'y':
    if play_again == 'n':
        print("Thanks for playing. Bye!")
        break

    random_number = random.randint(1, 10)

    game_on = True

    while game_on:
        guessed_number = int(input("Guess a number between 1 and 10: "))

        if guessed_number == random_number:
            print("You guessed it! You won!")
            game_on = False
            play_again = input("Do you want to keep playing? (y/n) ")
        elif guessed_number > random_number:
            print("Too high, try again!")
        elif guessed_number < random_number:
            print("Too low, try again!")


