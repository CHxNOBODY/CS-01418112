word = input()

guessed_letters = ['-' for _ in range(len(word))]

while True:
    guess = input()
    if guess == '0':
        break
    for i, letter in enumerate(word):
        if letter == guess:
            guessed_letters[i] = guess

print(''.join(guessed_letters))