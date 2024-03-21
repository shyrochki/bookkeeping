def decrypted_input(users_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_sentence = " "
    for char in users_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            new_index = (index + key) % 26
            new_letter = alphabet[new_index]
            if char.isupper():
                new_letter = new_letter.upper()
            decrypted_sentence += new_letter
        else:
            decrypted_sentence += char
    return decrypted_sentence

users_text = input("What do you want to decrypt? ")
key = int(input("What key was used? "))
print(f"Your text is: {users_text} and your key is: {key}")
decrypted_sentence = decrypted_input(users_text, key)
print("Your encrypted sentence is:", decrypted_sentence)