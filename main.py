"""
Simple Caesar Cipher Tool
Eksplorasi dasar kriptografi & manipulasi string dalam Python.
"""

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    message = "Exploring Cyber Security and AI"
    shift_key = 4
    
    encrypted = encrypt(message, shift_key)
    decrypted = decrypt(encrypted, shift_key)
    
    print(f"Original  : {message}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")
