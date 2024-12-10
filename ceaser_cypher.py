# Ceaser Cypher
from includes.art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def ceaser(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
    print(f"here is the {encode_or_decode}d result:{output_text}")

should_we_continue = True
while should_we_continue:
    direction = input("Type encode to encrypt,type decode to decrypt:\n").lower()
    text=input("type your message:").lower()
    shift = int(input("Type the shift number:"))

    ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)

    continue_ =input("Do you want to encode or decode another message? (yes/no): ").lower()
    if continue_ == 'yes':
        should_we_continue = True
    else:
        should_we_continue = False
        print("Thank you for using Ceaser Cypher")
        exit()


