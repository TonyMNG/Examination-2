import random
import string

class guess:
    def guess_game(choice):

        turns = 8
        wrong_guess = 0
        player_name = input("Enter your name: ")
        guessed_letters = set()


        if choice == 1:
            # Solo

            random_word = random.choice(words)
            while turns > 0:
                user_guess = input("Guess a letter: ")

                # guess immediatly implementation - not finished
                # if user_guess == random_word:
                #     print("Woah! You guessed correctly immediatly!")
                #     turns -= 1
                #     break

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



        elif choice == 3:
            # Playing against pc
            computer_turns = 8
            user_turn = True
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
                        guessed_letters += user_guess

                #User
                if user_turn:
                    user_guess = input("Guess a letter: ")

                    if all(char in random_word for char in user_guess):
                        print("Fast win!!!!")
                        break

                    guessed_letters += user_guess

                    if user_guess in random_word:
                        print("You guessed correctly.")
                        user_turn = True
                    else:
                        print("You guessed wrong")
                        turns -= 1
                        print(f"You have {turns} left.")
                        return False

                else:
                    #Computer
                    print("Computer's turn: ")
                    computer_guess = random.choice(string.ascii_lower())
                    
                    guessed_letters += computer_guess
                    if all(char in random_word for char in computer_guess):
                        continue
                    elif computer_guess in guessed_letters:
                        computer_guess = random.choice(string.ascii_lower())
                    else: 
                        computer_turns -= 1
                

                #End of game
                if turns == 0:
                        print("Computer won! The word is: " + random_word)
                        print("Better luck next time!")
                        break   
                elif computer_turns == 0:
                    print("You won over computer! The word is: " + random_word)
                    break




