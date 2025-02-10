target = 72
guesscount = 0
 
while True:
    guess = int(input("Enter your guess: "))
    
    guesscount += 1
    
    if guess < 0 or guess > 100:
        print("Sorry, your guess is out of range.")
    elif guess < target:
        print("Sorry, your guess is too low")
    elif guess > target:
        print("Sorry, your guess is too high.")
    else:
        print("Congratulations, your guess is correct.")
        print(f'Total number of guesses is {guesscount}')
        
        break