# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 10:15:26 2025

@author: navee
"""
class VigenereCipher:
    def __init__(self, key: str):
        self.key = key.lower()
        self.key_length = len(self.key)
        self.key_int = [ord(i) - ord('a') for i in self.key]

    def encrypt(self, text: str) -> str:
        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                offset = self.key_int[i % self.key_length]
                result += chr((ord(char) - base + offset) % 26 + base)
            else:
                result += char
        return result

    def decrypt(self, ciphertext: str) -> str:
        result = ""
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                offset = self.key_int[i % self.key_length]
                result += chr((ord(char) - base - offset) % 26 + base)
            else:
                result += char
        return result


# Example usage
if __name__ == "__main__":
    cipher = VigenereCipher("key")
    plaintext = "Network Security"

    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

