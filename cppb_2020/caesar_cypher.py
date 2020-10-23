def encode_char(input_char,key):
    '''This function take two arguments, an input character and a numeric key,
    and returns an output character. The input character is converted to it's
    ASCII code number. The key is used to move from one printable
    ASCII character to another.'''
    
    code_no = ord(input_char) #Convert character to ASCII code no.
    code_no -= 32             #Accout for control chars (0-31)
    code_no += key            #Apply key
    code_no = code_no % 95    #Convert back to 0-94 (95 printable chars)
    code_no += 32             #Convert back to ASCII code no.
    output_char = chr(code_no)#Convert back into a character

    return output_char

def caesar_cypher(input_string,key):
    encoded_string = ""
    for character in input_string:
        encoded_string += encode_char(character,key)
    
    return encoded_string

print(caesar_cypher("hello!",5))
print(caesar_cypher("mjqqt&",-5))
