name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on the dirt road, it has come to and end: ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across it:").lower()

    if answer == "swim":
        print("You swam and eaten by the crocodile.")
    elif answer == "walk":
        print("You walk for many miles, and run out energy.")
    else:
        print("Not a valid option! You Lose.")

elif answer == "right":
    print("You are good to go.")
    'continue'
else:
    print("Not a valid option, You lose.")


