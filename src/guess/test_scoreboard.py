import unittest
from unittest.mock import patch, mock_open
from scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard("test_scores.txt")

    def tearDown(self):
        self.scoreboard = None

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data="John                5\n")
    def test_draw(self, mock_open, mock_print):
        self.scoreboard.draw()
        mock_open.assert_called_once_with("test_scores.txt", 'r')
        mock_print.assert_called()

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open)
    def test_add_score(self, mock_open, mock_print):
        self.scoreboard.add_score("Alice", 10)
        mock_open.assert_called_once_with("test_scores.txt", 'a')
        mock_open().write.assert_called_once_with("Alice                10\n")

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data="John                5\n")
    def test_display_scores(self, mock_open, mock_print):
        self.scoreboard.display_scores()
        mock_open.assert_called_once_with("test_scores.txt", 'r')
        mock_print.assert_called()


if __name__ == "__main__":
    unittest.main()
