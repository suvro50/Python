# random generat the random numbers
import random

def play_game():
    lucky_number=random.randint(1,50)

    while True:
        user_num=int(input("Enter your lucky number: "))

        if user_num==lucky_number:
            print("You own the game. Game over!!")
            break
        elif user_num < lucky_number:
            print("You guss too low")
        else:
            print("Your guss too high")

    print("Thank you for playing..") 

play_game()