import random
import string


class Guess:
    def guess_game(choice):
        words = ['London', 'Ankara', 'Abuja', 'Stockholm', 'Oslo',
                 'Copenhagen', 'Paris', 'Berlin', 'Rome', 'Madrid', 'Athens',
                 'Vienna', 'Brussels', 'Amsterdam']
      
        turns = 8
        wrong_guess = 0
        player_name = input("Enter your name: ")
        guessed_letters = set()
        random_word = random.choice(words)

        if choice == 1:
            # Solo
            while turns > 0:
                user_guess = input("Guess a letter: ")

                # guess immediatly implementation - not finished
                if user_guess == random_word:
                    print("Woah! You guessed correctly immediatly!")
                    turns -= 1
                    break

                if user_guess in random_word:
                    guessed_letters.add(user_guess)
                else:
                    wrong_guess += 1

                for char in random_word: 
                    if char in user_guess:
                        print(char, end=" ")
                        guessed_letters += char

                    else:
                        print("_", end=" ")
                        turns -= 1
                        wrong_guess += 1

                print("Guessed characters: ", guessed_letters)

                if wrong_guess == 0:
                    print(f"Congratulations {player_name}, you won!")
                    break

                if turns == 0:
                    print("You lost!, the word is: " + random_word)
                    print("Better luck next time!")
                    break

        elif choice == 2:
            # 2 players
            # player1_name = input("Enter Player 1 name: ")
            players_turn = True
            player2_turns = 8
            player2_name = input("Enter Player 2 name: ")

            while turns > 0 or player2_turns > 0:
                print(f"{player_name} starts first.")
                
                for char in random_word:
                    if char in guessed_letters:
                        print(char, end=" ")                        
                    else:
                        print("_", end=" ")
                        guessed_letters += char
                # player 1
                if players_turn:
                    print(f"{player_name}s turn.")
                    user_guess = input("Guess a letter: ")

                    if all(char in random_word for char in user_guess):
                        print("Fast win!!!!")
                        break

                    guessed_letters += user_guess

                    if user_guess in random_word:
                        print(f"{player_name} guessed correctly.")
                        player_turn = False
                    else:
                        print(f"{player_name} guessed wrong")
                        turns -= 1
                        print(f"{player_name} has {turns} left.")

                else:
                    print(f"{player2_name}s turn.")
                    player2_guess = input("Guess a letter: ")

                    if all(char in random_word for char in player2_guess):
                        print("Fast win!!!!")
                        break

                    guessed_letters += player2_guess

                    if player2_guess in random_word:
                        print("You guessed correctly.")
                        player_turn = False
                    else:
                        print("You guessed wrong")
                        player2_turns -= 1
                        print(f"You have {player2_turns} left.")

        elif choice == 3:
            # Playing against pc
            computer_turns = 8
            player_turn = True
            random_word = random.choice(words)
            
            while turns > 0 or computer_turns > 0:
                print(f"{player_name} starts first.")

                for char in random_word:
                    if char in guessed_letters:
                        print(char, end=" ")                        
                    else:
                        print("_", end=" ")
                        turns -= 1
                        wrong_guess += 1
                        guessed_letters += char

                # User
                if player_turn:
                    print(f"{player_name}s turn.")
                    user_guess = input("Guess a letter: ")

                    if all(char in random_word for char in user_guess):
                        print("Fast win!!!!")
                        break

                    guessed_letters += user_guess

                    if user_guess in random_word:
                        print("You guessed correctly.")
                        player_turn = False
                    else:
                        print("You guessed wrong")
                        turns -= 1
                        print(f"You have {turns} left.")

                else:
                    # Computer
                    print("Computer's turn: ")
                    computer_guess = random.choice(string.ascii_lowercase)
                    
                    guessed_letters += computer_guess
                    if computer_guess in guessed_letters:
                        computer_guess = random.choice(string.ascii_lower())
                    elif computer_guess in random_word:
                        print("Computer guessed correctly.")
                        player_turn = False
                    else:
                        computer_turns -= 1
                        print(f"Computer has {computer_turns} left.")
                        player_turn = True

                    print(f"Computer guessed: {computer_guess}")

                # End of game
                if turns == 0:
                    print("Computer won! The word is: " + random_word)
                    print("Better luck next time!")
                    break
                elif computer_turns == 0:
                    print("You won over computer! The word is: " + random_word)
                    break




