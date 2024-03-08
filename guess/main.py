from guess import Guess
from scoreboard import Scoreboard
from rules import Rules
from menu import Menu


def main():
    keep_going = True
    menu = Menu()

    print("\n   * Welcome to our Guess Game - Capital Cities Edition! *")

    while keep_going:
        Menu.display_main_menu()
        choice = Menu.get_menu_choice()

        if choice == 5:
            keep_going = menu.menu_choice(choice)
        else:
            menu_return = menu.menu_choice(choice)
            if menu_return is None:
                continue


if __name__ == "__main__":
    main()
