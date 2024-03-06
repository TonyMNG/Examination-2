import random

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


            random_word = random.choice(words)
            while turns > 0:
                print(f"{player_name} starts first.")
                user_guess = input("Guess a letter: ")


                for char in random_word: 
                    if char in user_guess:
                        print(char, end=" ")
                        print("Character exists in word")
                        
                    else:
                        print("_", end=" ")
                        turns -= 1
                        wrong_guess += 1

                        guessed_letters += user_guess

                if turns == 0:
                        print("Computer won! The word is: " + random_word)
                        print("Better luck next time!")
                        break   




