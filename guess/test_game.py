import unittest
from unittest.mock import patch, MagicMock
from game import GuessGame


class TestGuessGame(unittest.TestCase):
    @patch('builtins.input', side_effect=["quit"])
    @patch('builtins.print')
    def test_solo_mode_quit(self, mock_print, mock_input):
        guess_game = GuessGame()
        guess_game.solo_mode()
        mock_print.assert_called_with("Quitting solo mode.")

    @patch('builtins.input', side_effect=["a"])
    @patch('builtins.print')
    def test_solo_mode_invalid_input(self, mock_print, mock_input):
        guess_game = GuessGame()
        guess_game.get_random_word = MagicMock(return_value="London")
        guess_game.solo_mode()
        mock_print.assert_called_with("Invalid input. Must enter an alphabetic character.")

    @patch('builtins.input', side_effect=["e", "i", "quit"])
    @patch('builtins.print')
    def test_solo_mode_correct_guess(self, mock_print, mock_input):
        guess_game = GuessGame()
        guess_game.get_random_word = MagicMock(return_value="Paris")
        guess_game.solo_mode()
        mock_print.assert_any_call("*** Congratulations Player, you won! ***")

    @patch('builtins.input', side_effect=["p", "quit", "o", "quit"])
    @patch('builtins.print')
    def test_PvP_mode_quit(self, mock_print, mock_input):
        guess_game = GuessGame()
        guess_game.PvP_mode()
        mock_print.assert_any_call("Player 1 chose to quit game.")

    @patch('builtins.input', side_effect=["q", "q", "quit"])
    @patch('builtins.print')
    def test_PvP_mode_draw(self, mock_print, mock_input):
        guess_game = GuessGame()
        guess_game.get_random_word = MagicMock(return_value="Rome")
        guess_game.PvP_mode()
        mock_print.assert_called_with("\nIt's a draw! None of you managed to find the guessing word.")


if __name__ == "__main__":
    unittest.main()
