def to_camel_case():
    s = input()
    separators = "-_=$."
    words = []
    current_word = ""

    for char in s:
        if char in separators:
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    camel_case_str = words[0].lower()
    for word in words[1:]:
        camel_case_str += word.capitalize()

    print(camel_case_str)

to_camel_case()