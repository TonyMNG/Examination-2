from game import GuessGame
from scoreboard import Scoreboard
from rules import Rules
from menu import Menu

"""
This module contains the main function for the application.
"""


def main():
    """
    This is the main function that runs the application.
    """
    keep_going = True
    guess_game = GuessGame()
    menu = Menu(guess_game)
    scoreboard = Scoreboard("scores.txt")

    print("\n   * Welcome to our Guess Game - Capital Cities Edition! *")

    while keep_going:

        menu.display_main_menu()
        choice = menu.get_menu_choice()

        if choice == 5:
            keep_going = menu.menu_choice(choice)
        elif choice == 2:
            Rules.display_rules()
        elif choice == 3:
            scoreboard.draw()
        else:
            menu_return = menu.menu_choice(choice)
            if menu_return is None:
                continue


if __name__ == "__main__":
    main()
