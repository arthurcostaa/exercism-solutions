from string import ascii_letters, ascii_lowercase, ascii_uppercase


MAX_KEY = len(ascii_lowercase)


def rotate(text, key):
    encrypted = list(text)

    for index, char in enumerate(text):
        if char in ascii_letters:
            char_index = ascii_lowercase.index(char.lower())

            encrypted_index = (
                char_index + key
                if (char_index + key) < MAX_KEY
                else (char_index + key) % MAX_KEY
            )

            if char.isupper():
                encrypted[index] = ascii_uppercase[encrypted_index]
            else:
                encrypted[index] = ascii_lowercase[encrypted_index]

    return ''.join(encrypted)
