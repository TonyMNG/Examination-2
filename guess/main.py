from guess import Guess


def menu_choice(choice):
    gameboard = Guess()

    if choice == 1:
        print("""
            ___________________________
            |        * Menu *         |
            |                         |
            |    1. Solo              |
            |    2. PvP               |
            |    3. Against Computer  |
            |                         |
            |    5. Return            |
            ___________________________
        """)
        play_choice = int(input("Choose your option: "))
        if play_choice == 1:
            gameboard.guess_game(1)
        elif play_choice == 2:
            print("Always nice to play with a friend.")
            gameboard.guess_game(2)
        elif play_choice == 3:
            print("May the best player win!")
            gameboard.guess_game(3)
        elif play_choice == 5:
            return None
        else:
            print("Invalid choice")
    elif choice == 2:
        # write rules here
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
            |    1. Play game         |
            |    2. See rules         |
            |                         |
            |    5. Quit game         |
            ___________________________
        """)
        choice = int(input("            Enter Choice: "))

        if choice == 5:
            keep_going = menu_choice(choice)

        else:
            menu_return = menu_choice(choice)
            if menu_return is None:
                continue


if __name__ == "__main__":
    main()
