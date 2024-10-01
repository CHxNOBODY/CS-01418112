def play_hangman():
    word = input()
    guessed_letters = []
    gallows = ["", "", "", "", "", ""]
    blanks = ["-"] * len(word)

    while True:
        guess = input()
        if guess == "0":
            break
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue
        guessed_letters.append(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    blanks[i] = guess
        else:
            gallows.append("X")
            if len(gallows) == 6:
                print("You lost! The word was " + word)
                return
        print(" ".join(blanks))

play_hangman()