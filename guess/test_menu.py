import unittest
from unittest.mock import patch, MagicMock
from menu import Menu

class TestMenu(unittest.TestCase):
    @patch('builtins.print')
    def test_display_main_menu(self, mock_print):
        menu = Menu(None)  # Passing None as guess_game since it's not required for this test
        menu.display_main_menu()
        mock_print.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1"])
    def test_get_menu_choice(self, mock_input, mock_print):
        menu = Menu(None)  # Passing None as guess_game since it's not required for this test
        choice = menu.get_menu_choice()
        mock_print.assert_called_once()
        self.assertEqual(choice, 1)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1"])
    def test_menu_choice_play_option(self, mock_input, mock_print):
        guess_game_mock = MagicMock()
        menu = Menu(guess_game_mock)
        keep_going = menu.menu_choice(1)
        guess_game_mock.solo_mode.assert_called_once()
        self.assertTrue(keep_going)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["2"])
    def test_menu_choice_read_rules_option(self, mock_input, mock_print):
        guess_game_mock = MagicMock()
        menu = Menu(guess_game_mock)
        result = menu.menu_choice(2)
        self.assertEqual(result, 2)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["5"])
    def test_menu_choice_quit_option(self, mock_input, mock_print):
        guess_game_mock = MagicMock()
        menu = Menu(guess_game_mock)
        result = menu.menu_choice(5)
        self.assertFalse(result)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["10"])  # Invalid choice
    def test_menu_choice_invalid_option(self, mock_input, mock_print):
        guess_game_mock = MagicMock()
        menu = Menu(guess_game_mock)
        result = menu.menu_choice(10)
        self.assertTrue(result)  # Should continue


if __name__ == "__main__":
    unittest.main()
