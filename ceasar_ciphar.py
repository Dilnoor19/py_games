alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
            "y", "z"]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            # Preserve characters not in the alphabet (e.g., spaces, punctuation)
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
    direction = input("Which function do you want to execute ('encode' or 'decode'):\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    print("")
    restart = input("Type 'yes' if you want to go again. otherwise, type 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Thank you for using the Caesar Cipher program!")
        print("Goodbye!")
    elif restart != "yes":
        print("Invalid input.")
        print("Goodbye!")
        should_continue = False