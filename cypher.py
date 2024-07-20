def vigenere(msg,key,dir=1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_msg = ""
    key_index = 0
    for char in msg.lower():
        if not char.isalpha():
            new_msg += char
        else:
            key_index += 1
            index = alphabet.find(char)
            offset = alphabet.index(key[key_index%len(key)])
            new_index = (index + offset*dir+26)%26
            new_msg += alphabet[new_index]
    return new_msg

encrypt = vigenere("Hello World","ciaomondo",1)
print(encrypt)

decrypt = vigenere(encrypt,"ciaomondo",-1)
print(decrypt)