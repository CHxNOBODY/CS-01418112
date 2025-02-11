def print_rangoli(size):
    if size <= 0 or size > 26:
        print("-")
        return

    import string
    
    # Create the alphabet list
    alphabet = string.ascii_lowercase[:size]

    # Create the pattern for each row
    rows = []
    for i in range(size):
        # Get the letters for this row
        letters = alphabet[size - i - 1:size]
        pattern = "-".join(letters[::-1] + letters[1:])
        rows.append(pattern.center(4 * size - 3, '-'))

    # Print the full rangoli
    print("\n".join(rows + rows[-2::-1]))

# Input from user
try:
    n = int(input("Enter the size of the Rangoli (1-26): "))
    print_rangoli(n)
except ValueError:
    print("-")
