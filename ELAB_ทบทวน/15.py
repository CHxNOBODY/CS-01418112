def capital_letter(sentence ):
    exceptions = ["for", "and", "with", "of"]
    words = sentence.split()
    capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
    return " ".join(capitalized_words)

# Test the function
text = input()
print(capital_letter(text))