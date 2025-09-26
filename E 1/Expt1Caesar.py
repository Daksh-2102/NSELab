# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 10:14:44 2025

@author: navee
"""
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # only letters
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char  # keep spaces/punctuation same
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

# input
text = "HELLO WORLD"
shift = 3
encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

