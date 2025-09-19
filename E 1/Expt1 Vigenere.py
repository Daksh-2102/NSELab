# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 10:15:26 2025

@author: navee
"""
class VigenereCipher:
    def __init__(self, key: str):
        # Always keep key in uppercase for consistency
        self.key = key.upper()

    def __shift_char(self, char: str, key_index: int, encrypt: bool = True) -> str:
        """Helper method to shift a character during encryption/decryption."""
        if not char.isalpha():
            return char  # Leave non-alphabet characters unchanged

        base = 'A' if char.isupper() else 'a'
        shift = ord(self.key[key_index % len(self.key)]) - ord('A')

        if not encrypt:
            shift = -shift  # Reverse shift for decryption

        return chr((ord(char) - ord(base) + shift) % 26 + ord(base))

    def encrypt(self, plaintext: str) -> str:
        result = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                result.append(self.__shift_char(char, key_index, encrypt=True))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                result.append(self.__shift_char(char, key_index, encrypt=False))
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)


# Example usage
if __name__ == "__main__":
    text = "HELLO WORLD"
    key = "KEY"

    cipher = VigenereCipher(key)

    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)

    print("Original :", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
