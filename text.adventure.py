health = 100

name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")
print("You start with", health, "health points.\n")

print("You are standing on a dirt road that ends in a fork.")
answer = input("Do you go left or right? (left/right): ").lower()

if answer == "left":
    answer = input("\nYou come to a wide river. Do you want to walk around it or swim across it? (walk/swim): ").lower()

    if answer == "swim":
        print("You tried to swim across but got bitten by a crocodile.")
        health -= 50
        print("You survived, but lost 50 health. Current health:", health)
    elif answer == "walk":
        print("You walked for hours and got very tired.")
        health -= 30
        print("You lost 30 health. Current health:", health)
    else:
        print("Not a valid option! You Lose.")
        health = 0

elif answer == "right":
    print("\nYou head right and enter a dark forest.")
    answer = input("You hear rustling in the bushes. Do you investigate or keep walking? (investigate/walk): ").lower()

    if answer == "investigate":
        print("A wild animal attacks you! 🐺")
        health -= 70
        print("You managed to escape, but lost 70 health. Current health:", health)
    elif answer == "walk":
        print("You ignore the noise and find a small village up ahead.")
        answer = input("The villagers seem friendly. Do you talk to them or sneak around? (talk/sneak): ").lower()

        if answer == "talk":
            print("They offer you food and shelter. 🎉 You Win!")
            health += 30
            print("You gain 30 health. Final health:", health)
        elif answer == "sneak":
            print("They catch you sneaking and assume you're a threat. You are captured. ⚔️ You Lose.")
            health = 0
        else:
            print("Not a valid option! You Lose.")
            health = 0
    else:
        print("Not a valid option! You Lose.")
        health = 0

else:
    print("Not a valid option! You Lose.")
    health = 0

# Final result
if health <= 0:
    print("\nGame Over. 😢 Your final health is 0.")
else:
    print("\nCongratulations! 🎉 Your adventure ends with", health, "health points.")
