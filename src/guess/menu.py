"""
Module: menu.py
Description: This module contains the Menu class for the Guess Game application.
"""


class Menu:
    """
    A class to represent a menu in a Guess Game application.
    """
    def __init__(self, guess_game):
        """
        Initializes the Menu with a GuessGame instance.

        Args:
            guess_game (GuessGame): An instance of the GuessGame class.
        """
        self.guess_game = guess_game

    def display_main_menu(self):
        """
        Displays the main menu options.
        """
        print("""
            ___________________________
            |        * Menu *         |
            |                         |
            |    1. Play game         |
            |    2. Read rules        |
            |    3. Scoreboard        |
            |                         |
            |    5. Quit game         |
            ___________________________
        """)

    def display_play_menu(self):
        """
        Displays the play menu options.
        """
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

    def get_menu_choice(self):
        """
        Gets the user's choice from the main menu.

        Returns:
            int: The user's choice.
        """
        return int(input("Enter Choice: "))

    def get_play_choice(self):
        """
        Gets the user's choice from the play menu.

        Returns:
            int: The user's choice.
        """
        return int(input("Choose your option: "))

    def menu_choice(self, choice):
        """
        Processes the user's menu choice.

        Args:
            choice (int): The user's choice from the menu.

        Returns:
            bool or None: True to continue, False to quit,
            None to return to previous menu.
        """
        if choice == 1:
            self.display_play_menu()
            play_choice = self.get_play_choice()
            if play_choice == 1:
                self.guess_game.solo_mode()
            elif play_choice == 2:
                print("Always nice to play with a friend.")
                self.guess_game.PvP_mode()
            elif play_choice == 3:
                print("May the best player win!")
                self.guess_game.PvC_mode()
            elif play_choice == 5:
                return None
            else:
                print("Invalid choice")
        elif choice == 2:
            return choice
        elif choice == 5:
            print("Quitting game...")
            return False
        else:
            print("Invalid choice")

        return True
