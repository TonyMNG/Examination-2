
def menu_choice(choice):
    if choice == 1:
        print("Lets play a Solo game.")
    elif choice == 2:
        print("Always nice to play with a friend.")
    elif choice == 3:
        print("May the best player win!")
    elif choice == 4:
        print("")
    elif choice == 5:
        print("Quitting game...")
        return False
    else:
        print("Invalid choice")
        return True


def main():
    keep_going = True

    print("\n   * Welcome to our Guess Game - Capital Cities Edition! *")

    while keep_going:

        print("""
            ___________________________
            |        * Menu *         |
            |                         |
            |    1. Play solo         |
            |    2. Play PvP          |
            |    3. Play PC           |
            |    4. See rules         |
            |                         |
            |    5. Quit game         |
            ___________________________
        """)
        choice = int(input("            Enter Choice: "))
        keep_going = menu_choice(choice)

            
if __name__ == "__main__":
    main()
