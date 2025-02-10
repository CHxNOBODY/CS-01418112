def decode_message(encoded_message):
    decoded_message = ""
    i = 0
    vowels = "aeiou"

    while i < len(encoded_message):  
        if encoded_message[i] in vowels and i + 2 < len(encoded_message) and encoded_message[i+1] == 'p' and encoded_message[i+2] == encoded_message[i]:      
            decoded_message += encoded_message[i]
            i += 3
        else:
            decoded_message += encoded_message[i]
            i += 1
    return decoded_message

encoded_message = input()
decoded_message = decode_message(encoded_message)
print(decoded_message)
