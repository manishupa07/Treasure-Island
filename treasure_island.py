import time

def intro():
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure.")
    time.sleep(2)

def start():
    print("You are at a crossroad. Where do you want to go? Type 'left' or 'right'.")
    choice = input().lower()
    if choice == "left":
        print("You chose the left path. You encounter a lake.")
        lake()
    elif choice == "right":
        print("You chose the right path. You encounter a forest.")
        forest()
    else:
        print("Invalid choice. Please try again.")
        start()

def lake():
    print("Do you want to 'swim' across or 'wait' for a boat?")
    choice = input().lower()
    if choice == "wait":
        print("You waited for a boat and successfully crossed the lake.")
        island()
    elif choice == "swim":
        print("You tried to swim across the lake but were eaten by a giant fish. Game Over!")
        play_again()
    else:
        print("Invalid choice. Please try again.")
        lake()

def forest():
    print("You encounter a bear blocking your path. What do you do? 'fight' or 'run'?")
    choice = input().lower()
    if choice == "fight":
        print("You tried to fight the bear but it was too strong. Game Over!")
        play_again()
    elif choice == "run":
        print("You ran away from the bear and escaped into the forest.")
        island()
    else:
        print("Invalid choice. Please try again.")
        forest()

def island():
    print("You arrive at the treasure island and see three doors: 'red', 'blue', and 'yellow'.")
    choice = input().lower()
    if choice == "red":
        print("You opened the door and found the treasure! You win!")
        play_again()
    elif choice == "blue":
        print("You opened the door and were attacked by a swarm of bees. Game Over!")
        play_again()
    elif choice == "yellow":
        print("You opened the door and fell into a pit of snakes. Game Over!")
        play_again()
    else:
        print("Invalid choice. Please try again.")
        island()

def play_again():
    print("Do you want to play again? 'yes' or 'no'?")
    choice = input().lower()
    if choice == "yes":
        start()
    elif choice == "no":
        print("Thank you for playing! Goodbye.")
    else:
        print("Invalid choice. Please try again.")
        play_again()

def main():
    intro()
    start()

if __name__ == "__main__":
    main()
