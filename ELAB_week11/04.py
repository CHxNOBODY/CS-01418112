def hangman_game():
    word = input()
    guessed_letters = set()

    while True:
        guess = input()
        if guess == '0':
            break
        if guess in word:
            guessed_letters.add(guess)

    correct_count = sum(1 for letter in word if letter in guessed_letters)
    total_count = len(word)

    print(f"{correct_count}/{total_count}")

hangman_game()