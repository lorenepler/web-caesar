def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - 65
    elif letter.islower():
        return ord(letter) - 97

def rotate_character(char, rot):
    if char.isalpha():
        ciph_pos = ((alphabet_position(char)) + int(rot)) % 26 ##take alphabet_position and add rot # to it
        if char.isupper():
            ciph_letter = chr(ciph_pos+65)   ##locate letter at this new ordinal position
            return(ciph_letter)             ##and return it
        else:
            ciph_letter = chr(ciph_pos+97)   ##lower has a different ordinal value than uppper
            return(ciph_letter)
    else:
        return char

def encrypt(text, rot):
    encrypt_text = ""
    for char in text:
        encrypt_char = rotate_character(char, rot)
        encrypt_text += encrypt_char
    return encrypt_text
