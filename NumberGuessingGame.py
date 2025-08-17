import random, time

is_running = True

hard_scores = []
medium_scores = []
easy_scores = []

while is_running:
    print()
    print("Welcome to the Number Guessing Game")
    print("You are to guess my number which ranges from 1-100!")

    print()
    print("0 - Exit Game")
    print("1 - Easy   (10 Guesses)")
    print("2 - Medium (5 Guesses)")
    print("3 - Hard   (3 Guesses)")

    difficulty = input("Which difficulty would you like to choose?: ")
    guess_amount = 0
    
    if not difficulty.isdigit():
        print("Please enter the numbers listed above!")
        continue

    difficulty = int(difficulty)

    if difficulty == 0:
        break

    elif difficulty == 1:
        allowed_guesses = 10
        print(f"Your best score for this difficulty is: {min(easy_scores, default=None)}")

    elif difficulty == 2:
        allowed_guesses = 5
        print(f"Your best score for this difficulty is: {min(medium_scores, default=None)}")

    elif difficulty == 3:
        allowed_guesses = 3
        print(f"Your best score for this difficulty is: {min(hard_scores, default=None)}")

    else:
        print("Invalid input! Only choose numbers 1, 2, or 3\n")
        continue

    correct_number = random.randint(1,100)

    print()
    print(f"The game has begun! You have {allowed_guesses} guesses to correctly guess the number!")
    game_time_start = time.time()

    while True:
        guess = input("Enter your guess: " )


        guess = int(guess)
        guess_amount += 1

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100!")
            continue

        if not guess.isdigit():
            print("Something went wrong! Please try again")
            continue
        
        if guess == correct_number:
            game_time_end = time.time()
            print(f"It took you {game_time_end - game_time_start:.2f} seconds to guess the number!")
            print(f"You guessed the number correctly! It was {correct_number}.")
            print(f"It took you {guess_amount} attempts")

            if difficulty == 3:
                hard_scores.append(guess_amount)
            elif difficulty == 2:
                medium_scores.append(guess_amount)
            elif difficulty == 1:
                easy_scores.append(guess_amount)
            break

        elif guess_amount == allowed_guesses:
            print(f"You lost! The number was {correct_number}\n")
            break

        elif guess > correct_number:
            print("Your guess is too high")
                
        else:
            print("Your guess is too low")
                
    while True:
        play_again = input("Would you like to play again? (Y/N): ").capitalize()
        if play_again in ('Y', 'N'):
            break
        else:
            print("Invalid input!")

    if play_again == 'N':
        is_running = False
