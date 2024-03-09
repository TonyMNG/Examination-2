"""
Module: scoreboard.py
Description: Contains the Scoreboard class for managing game scores.
"""


class Scoreboard:
    """
    A class to manage game scores and display the scoreboard.
    """
    def __init__(self, filename):
        """
        Initializes the Scoreboard with the given filename.

        Args:
            filename (str): The name of the file to store scores.
        """
        self.filename = filename

    def draw(self):
        """
        Draws the scoreboard by displaying player names and their respective scores.
        """
        self.display_scores()

    def add_score(self, name, score):
        """
        Adds a new score entry to the scoreboard.

        Args:
            name (str): The name of the player.
            score (int): The score achieved by the player.
        """
        with open(self.filename, 'a') as file:
            file.write(f"{name.ljust(20)} {score}\n")

    def display_scores(self):
        """
        Displays the scores stored in the scoreboard file.
        """
        with open(self.filename, 'r') as file:
            scores = file.readlines()
            print("======= Scoreboard =======")
            print("Player ============ Wins =")
            for line in scores:
                print(line.strip())
            print("==========================")


scoreboard = Scoreboard("scores.txt")
