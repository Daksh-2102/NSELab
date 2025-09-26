# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 23:51:22 2025

@author: navee
"""

import hashlib
import time
import random

# Pre-shared secret (server-side)
SECRET_KEY = "Dakshsecret"

# Server generates random challenge with timestamp
def generate_challenge():
    challenge = str(random.randint(10000, 99999))
    timestamp = int(time.time())  # current time in seconds
    return challenge, timestamp

# Client computes response
def compute_response(challenge, secret):
    data = challenge + secret
    return hashlib.sha256(data.encode()).hexdigest()

# Server verifies response and detects replay
used_nonces = set()

def verify_response(challenge, response, timestamp):
    if challenge in used_nonces:
        return f"Replay Attack Detected! (Challenge issued at {timestamp})"
    expected = compute_response(challenge, SECRET_KEY)
    if response == expected:
        used_nonces.add(challenge)
        return f"Authentication Successful (Challenge issued at {timestamp})"
    return "Authentication Failed"

# --- Simulation with User Input ---
challenge, ts = generate_challenge()
print(f"\nServer Challenge: {challenge} (Issued at: {time.ctime(ts)})")

# Client enters secret key
user_secret = input("Enter your secret key: ")

# Client computes response
response = compute_response(challenge, user_secret)
print("Client Response:", response)

# Server verifies
print("Server Verification:", verify_response(challenge, response, ts))

# Simulate replay attack with delay
print("\n--- Replay Attack Simulation ---")
time.sleep(3)  # attacker tries replay after 3 seconds
print(f"Replay Attempt at {time.ctime()} ->", verify_response(challenge, response, ts))


