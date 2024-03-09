import unittest
from unittest.mock import patch, MagicMock
from main import main, Menu, Scoreboard, Rules


class TestMain(unittest.TestCase):
    @patch('builtins.print')
    @patch('main.Menu')
    @patch('main.Scoreboard')
    @patch('main.Rules')
    def test_main(self, mock_rules, mock_scoreboard, mock_menu, mock_print):
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.get_menu_choice.side_effect = [5, 1, 3, 4]  # Mocking user input

        main()

        mock_menu_instance.display_main_menu.assert_called_once()
        mock_menu_instance.get_menu_choice.assert_called_with()

        # Assert other expected method calls as needed


if __name__ == "__main__":
    unittest.main()
