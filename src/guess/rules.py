"""
Module: rules.py
Description: Contains the Rules class for managing game rules.
"""


class Rules:

    def display_rules():
        """
        Displays the rules of the Guess Game.
        """
        print("""
        Guess Game - Rules:

        Objective:
        The objective of the game is to guess the hidden word before running out of turns.

        In-game:
        - (Any player) Typing 'quit' during a game will abort the game and return to main menu.

        Game Modes:
        - Solo Mode: Play alone against the computer.
        - PvP Mode: Two players take turns guessing the word.
        - PvC Mode: Play against the computer.

        Turns:
        - Each player, including the computer, starts with a fixed number of turns. Players have '6' turns and computer has '8' turns.
        - (All modes), The player's turns are deducted by minus 1 for each incorrect guess.
        - (PvP mode, PvC mode), each player's turns are counted separately, and turns continues until someone makes a wrong guess.

        Guessing:
        - Players can guess a single letter or the entire word.
        - If a player guesses a letter correctly, it is revealed in the hidden word.
        - If a player guesses the entire word correctly, the game ends immediately.
        - If a player's guess is incorrect, their turns are deducted by minus 1 point, and the incorrect guess is recorded.
        - If entire word guess is incorrect it will deduct minus 2 points as a penalty.

        Winning and Losing:
        - In Solo Mode and PvC Mode, the player wins if they guess the word correctly within the given number of turns.
        - (All modes) A player wins by guessing the last remaining character or by guessing the whole word.
        - (PvP mode) If both players run out of turns and the guess word remains, it will result in a draw.
        - (Solo mode) If a player runs out of turns before guessing the word, they lose the game.

        Scoring:
        - Each win will add plus 1 point for wins to the players name on scoreboard.
        """)


if __name__ == "__main__":
    Rules.display_rules()
