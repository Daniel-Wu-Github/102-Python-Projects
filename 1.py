import numpy as np

# Load the integers from the file
with open("module12quizF23.txt", "r") as file:
    integers = [int(line.strip()) for line in file]

# Rearrange the numbers into a 100 x 100 matrix
matrix = np.array(integers).reshape(100, 100)

# Determine the key values
key_values = [
    matrix[:5, 85].sum(),            # The sum of the first 5 numbers in the 86th column
    np.mean(matrix[4]),                 # The average of the numbers in the 5th row
    matrix[62, -5:].sum(),              # The sum of the last five numbers in the 63rd row
    np.min(matrix[0]),                  # The minimum number in the 1st row
    np.max(matrix[29])                  # The maximum number in the 30th row
]

# Convert key values to corresponding letters
key = ''.join([chr(int(val) % 26 + ord('a')) for val in key_values])

# Define the Vigenère cipher decryption function
def decrypt_vigenere(ciphertext, key):
    decrypted_message = ''
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord(key[i % key_length]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char  # Keep non-alphabetic characters unchanged
        decrypted_message += decrypted_char
    return decrypted_message

# Encrypted message
encrypted_message = "zilhpzsyucavkzbf"

# Decipher the message using the key
decrypted_message = decrypt_vigenere(encrypted_message, key)

# Print the deciphered message and the key
print("Deciphered Message:", decrypted_message)
print("Key:", key)