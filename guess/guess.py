import random
import string


class Guess:

    def __init__(self):
        pass
 
    def guess_game(self, choice):
        words = ['London', 'Ankara', 'Abuja', 'Stockholm', 'Oslo',
                 'Copenhagen', 'Paris', 'Berlin', 'Rome', 'Madrid', 'Athens',
                 'Vienna', 'Brussels', 'Amsterdam']
      
        user_turns = 6
        player_name = input("Enter your name: ")
        guessed_letters = set()
        random_word = random.choice(words)

        if choice == 1:
            # Solo
            while user_turns > 0:
                user_guess = input("\nGuess an alphabet character: ").lower()

                if user_guess.lower() == "quit".lower():
                    print("Quitting solo mode.")
                    break

                if user_guess in guessed_letters:
                    print("You already guessed this character.")
                    continue

                if not user_guess.isascii() or not user_guess.isalpha():
                    print("Invalid input. Must enter an alphabetic character.")
                    continue

                if len(user_guess) > 1:
                    if user_guess.lower() == random_word.lower():
                        print("You guessed correctly immediatly!")
                        break
                    else:
                        print("You took a risky guess, this will deduct -2 turns.")
                        user_turns -= 2
                else:
                    if user_guess in random_word.lower():
                        print(f"\n * '{user_guess}' was found in word. *")
                        if user_guess not in guessed_letters:
                            guessed_letters.add(user_guess)
                    else:
                        print(f"\n * '{user_guess}' was NOT found in word. *")
                        guessed_letters.add(user_guess)
                        user_turns -= 1
                        print(f"You have {user_turns} turns left.")

                        if user_turns == 0:
                            print("You lost!, the word is: " + random_word)
                            print("Better luck next time!")
                            break
                        continue

                print("\nGuessed characters:", ", ".join(guessed_letters).upper() if guessed_letters else "None")
                print(f"You have {user_turns} turns left.")

                guess_word = "".join([char if char.lower() in guessed_letters 
                                      else "_ " for char in random_word])
                print(guess_word)

                if "_" not in guess_word:
                    print(f"*** Congratulations {player_name}, you won! ***")
                    print(f"The guess word was: {random_word}")
                    break

        elif choice == 2:
            # 2 players
            play_turn = True
            player2_turns = 6
            player2_name = input("Enter Player 2 name: ")
            print(f"{player_name} starts first.")

            while user_turns > -1 or player2_turns > -1:
                if user_turns == 0 and player2_turns == 0 and "_" in guess_word:
                    print("\nIt's a draw! None of you managed to find the guessing word.")
                    print(f"The guess word was: {random_word}")
                    break

                guess_word = "".join([char if char.lower() in guessed_letters 
                                      else "_ " for char in random_word])
                print(guess_word)

                # player 1
                if play_turn:
                    print(f"\n{player_name}s turn.")
                    user_guess = input("Guess an alphabet character: ".lower())

                    if user_guess == "quit":
                        print(f"{player_name} chose to quit game.")
                        break
                    if not user_guess.isascii() or not user_guess.isalpha():
                        print("Invalid input. Must enter an alphabetic character.")
                        continue
                    if user_guess in guessed_letters:
                        print("You already guessed this character.")
                        continue
                    
                    if len(user_guess) > 1:
                        if user_guess.lower() == random_word.lower():
                            print(f"{player_name} WON by guessing correctly immediatly.")
                            break
                        else:
                            print(f"{player_name} took a risky guess, this will deduct -2 turns.")
                            user_turns -= 2
                            print(f"{player_name} has {user_turns} turns left.")
                            play_turn = False
                    else:
                        if user_guess in random_word.lower():
                            print(f"{player_name} guessed correctly.")
                            if user_guess not in guessed_letters:
                                guessed_letters.add(user_guess)
                        else:
                            print(f"{player_name} guessed wrong")
                            guessed_letters.add(user_guess)
                            user_turns -= 1
                            print(f"{player_name} has {user_turns} turns left.")
                            play_turn = False

                    guess_word = "".join([char if char.lower() in guessed_letters 
                                         else "_ " for char in random_word])
                    if "_" not in guess_word:
                        print(f"*** Congratulations {player_name}, you won! ***")
                        print(f"The guess word was: {random_word}")
                        break

                # player 2
                else:
                    print(f"{player2_name}s turn.")
                    player2_guess = input("Guess an alphabet character: ".lower())

                    if player2_guess == "quit":
                        print(f"{player2_name} chose to quit game.")
                        break
                    if player2_guess in guessed_letters:
                        print("You already guessed this character.")
                        continue
                    if not player2_guess.isascii() or not player2_guess.isalpha():
                        print("Invalid input. Must enter an alphabetic character.")
                        continue

                    if len(player2_guess) > 1:
                        if player2_guess.lower() == random_word.lower():
                            print(f"{player2_name} WON by guessing correctly immediatly.")
                            break
                        else:
                            print(f"{player2_name} took a risky guess, this will deduct -2 turns.")
                            player2_turns -= 2
                            print(f"{player_name} has {user_turns} turns left.")
                            play_turn = True
                    else:
                        if player2_guess in random_word.lower():
                            print(f"{player2_name} guessed correctly.")
                            if player2_guess not in guessed_letters:
                                guessed_letters.add(player2_guess)
                        else:
                            print(f"{player2_name} guessed wrong")
                            guessed_letters.add(player2_guess)
                            player2_turns -= 1
                            print(f"{player2_name} has {player2_turns} turns left.")
                            play_turn = True
                    guess_word = "".join([char if char.lower() in guessed_letters 
                                         else "_ " for char in random_word])
                    if "_ " not in guess_word:
                        print(f"*** Congratulations {player2_name}, you won! ***")
                        print(f"The guess word was: {random_word}")
                        break

        elif choice == 3:
            # Playing against pc
            computer_turns = 8
            play_turn = True
            random_word = random.choice(words)
            guessed_letters = set()
            
            while True:
                # print(f"{player_name} starts.")
                guess_word = "".join([char if char.lower() in guessed_letters 
                                      else "_ " for char in random_word])
                print(guess_word)
                
                # User
                if play_turn:
                    print(f"\n{player_name}s turn.")
                    user_guess = input("Guess an alphabet character: ".lower())

                    if user_guess == "quit":
                        print(f"{player_name} chose to quit game.")
                        break
                    if not user_guess.isascii() or not user_guess.isalpha():
                        print("Invalid input. Must enter an alphabetic character.")
                        continue
                    if user_guess in guessed_letters:
                        print("You already guessed this character.")
                        continue
                    
                    if len(user_guess) > 1:
                        if user_guess.lower() == random_word.lower():
                            print(f"{player_name} WON by guessing correctly immediatly.")
                            break
                        else:
                            print(f"{player_name} took a risky guess, this will deduct -2 turns.")
                            user_turns -= 2
                            print(f"{player_name} has {user_turns} turns left.")
                            play_turn = False
                    else:
                        if user_guess in random_word.lower():
                            print(f"{player_name} guessed correctly.")
                            if user_guess not in guessed_letters:
                                guessed_letters.add(user_guess)
                        else:
                            print(f"{player_name} guessed wrong")
                            guessed_letters.add(user_guess)
                            user_turns -= 1
                            print(f"{player_name} has {user_turns} turns left.")
                            play_turn = False

                    guess_word = "".join([char if char.lower() in guessed_letters 
                                         else "_ " for char in random_word])
                    if "_" not in guess_word:
                        print(f"*** Congratulations {player_name}, you won! ***")
                        print(f"The guess word was: {random_word}")
                        break

                else:
                    # Computer
                    print("\nComputers turn.")
                    computer_guess = random.choice(string.ascii_lowercase)
                    print(f"Computer guessed: {computer_guess}")

                    if computer_guess in guessed_letters:
                        # print("You already guessed this character.")
                        continue

                    if computer_guess in random_word.lower():
                        print("Computer guessed correctly.")
                        if computer_guess not in guessed_letters:
                            guessed_letters.add(computer_guess)
                    else:
                        print("Computer guessed wrong")
                        guessed_letters.add(computer_guess)
                        computer_turns -= 1
                        print(f"Computer has {computer_turns} turns left.")
                        play_turn = True

                    guess_word = "".join([char if char.lower() in guessed_letters 
                                         else "_ " for char in random_word])
                    if "_ " not in guess_word:
                        print(f"Computer won!")
                        print(f"The guess word was: {random_word}")
                        break

                # End of game
                # if turns == 0:
                #     print("Computer won! The word is: " + random_word)
                #     print("Better luck next time!")
                #     break
                # elif computer_turns == 0:
                #     print("You won over computer! The word is: " + random_word)
                #     break




