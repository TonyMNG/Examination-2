
class Menu:
    def __init__(self, guess_game):
        self.guess_game = guess_game

    def display_main_menu():
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

    def display_play_menu():
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

    def get_menu_choice():
        return int(input("Enter Choice: "))
    
    def get_play_choice():
        return int(input("Choose your option: "))
    
    def menu_choice(self, choice):

        if choice == 1:
            Menu.display_play_menu()
            play_choice = Menu.get_play_choice()
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
            # Write rules here
            print("")
        elif choice == 5:
            print("Quitting game...")
            return False
        else:
            print("Invalid choice")

        return True