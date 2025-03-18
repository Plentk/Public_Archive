def caesar_cipher(word, shift=1):
    output = ""
    for char in word:
        if not char.isalpha():
            output += char
            continue
        base = 65 if char.isupper() else 97
        shift_char = chr((ord(char) - base + shift) % 26 + base)
        output += shift_char
        # print(f"{char} -> {shift_char}")
    # print(f"Initial plaintext: {word}")
    print(f"The final ciphertext is: {output}")
    return output
instring = str(input("Input text to decrypt: "))
for shift in range(26):
    print(26 - shift)
    caesar_cipher(instring, shift)