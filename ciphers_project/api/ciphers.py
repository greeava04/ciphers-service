def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if 'a' <= c <= 'z':
            c_encoded = ((ord(c) - ord('a') + shift) % 26) + ord('a')
        elif 'A' <= c <= 'Z':
            c_encoded = ((ord(c) - ord('A') + shift) % 26) + ord('A')
        else:
            c_encoded = ord(c)
        cipher_text += chr(c_encoded)
    return cipher_text