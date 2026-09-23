import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position] 
        else:
            cipher_text += letter

    return cipher_text


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter

    return decrypted_text


def caesar(text, shift, direction):

    if direction == "encode":
        return encrypt(text, shift)
    elif direction == "decode":
        return decrypt(text, shift)
    
    return "That's not a valid choice"

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = caesar(text, shift, direction)
    print(f"Here is the {direction}d result: {result}\n")
    
    go_again = input("Would you like to go again? 'Yes' or 'No'.\n").lower()
    if go_again == "yes":
        continue
    else:
        print("Goodbye, Friend!")
        break