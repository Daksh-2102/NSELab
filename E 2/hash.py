# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 16:11:16 2025

@author: navee
"""

import hashlib

class IntegrityChecker:
    def __init__(self, algorithm: str = "sha256"):
        self.algorithm = algorithm.lower()
        if self.algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")

    def compute_hash(self, data: str) -> str:
        """Compute hash of input text using selected algorithm."""
        h = hashlib.new(self.algorithm)
        h.update(data.encode())
        return h.hexdigest()

    def verify_integrity(self, text1: str, text2: str) -> bool:
        """Check if two texts produce the same hash."""
        return self.compute_hash(text1) == self.compute_hash(text2)


if __name__ == "__main__":
    # Choose hashing algorithm
    algo = input("Enter hash algorithm (default sha256): ").strip() or "sha256"
    checker = IntegrityChecker(algo)

    text1 = input("\nEnter original text: ").strip()
    text2 = input("Enter tampered text: ").strip()

    hash1 = checker.compute_hash(text1)
    hash2 = checker.compute_hash(text2)

    print("\n--- Hash Results ---")
    print(f"Original Text : {text1}")
    print(f"Tampered Text : {text2}")
    print(f"Original Hash : {hash1}")
    print(f"Tampered Hash : {hash2}")

    if checker.verify_integrity(text1, text2):
        print("\n✅ Data integrity verified (no tampering).")
    else:
        print("\n❌ Data has been tampered (hashes differ).")
