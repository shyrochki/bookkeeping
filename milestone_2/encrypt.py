def encrypted_input(users_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_sentence = " "
    for char in users_text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            new_index = (index - key) % 26
            new_letter = alphabet[new_index]
            if char.isupper():
                new_letter = new_letter.upper()
            encrypted_sentence += new_letter
        else:
            encrypted_sentence += char
    return encrypted_sentence

users_text = input("What do you want to encrypt? ")
key = int(input("What is the key? "))
print(f"Your text is: {users_text} and your key is: {key}")
encrypted_sentence = encrypted_input(users_text, key)
print("Your encrypted sentence is: ", encrypted_sentence)
