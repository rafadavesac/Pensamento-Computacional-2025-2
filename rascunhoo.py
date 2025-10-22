
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text,shift_amount):
    text_index = 0
    encoded_word = ''
    for letter in text:
        index_shift = alphabet.index(text[text_index]) + shift

        if index_shift > 25:
            index_shift = shift - 1

            letter = alphabet[index_shift]
            encoded_word += letter
            text_index += 1
            
        else:
            letter = alphabet[index_shift]
            encoded_word += letter
            text_index += 1

    print(encoded_word)

#encrypt(original_text=text,shift_amount=shift)



def decrypt(original_text, shift_amount):
    text_index = 0
    decoded_word = ''
    for letter in text:
        index_shift = alphabet.index(text[text_index]) - shift

        if index_shift <= 0:
            index_shift = 26 - shift

            letter = alphabet[index_shift]
            encoded_word += letter
            text_index -= 1
            
        else:
            letter = alphabet[index_shift]
            encoded_word += letter
            text_index -= 1

    print(decoded_word)

decrypt(original_text=text,shift_amount=shift)
'''

print(len(alphabet))

print(-3%26)

letter = 2

print(type(letter))

