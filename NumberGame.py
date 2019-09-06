# This creates the random number
import random
number = random.randrange(1, 100)
x = 1
y = 100
print("Enter a number between",x, "and",y)
# User inputs a guess between 1 and 100
while True:
    try:
        Guess = int(input())
        print("You guessed", Guess)
        if (Guess < x) or (Guess > y):
            print("Enter another number")
        elif Guess > number:
            y = Guess
            print("Too high! Enter a number between",x, "and",y)
        elif Guess < number:
            x = Guess
            print("Too low! Enter a number between",x, "and",y)
        elif Guess == number:
            print("You lose! Buy the next round.")
            input("Press Enter to exit")
            quit()
    except ValueError:
        print("This is not a number. Try again.")

