import binascii


def toBinary(word):
    word = bytes(word, encoding='ascii')
    print(word)
    return word


def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(message, key):
    m = toHex(toBinary(message))
    k = toHex(toBinary(key))
    c = m ^ k
    return c

def decrypt(code, key):
    k = toHex(toBinary(key))
    m = code ^ k
    return toString(m)

message = input("Skriv inn en melding: ")
key = input("Skriv inn en nøkkel: ")
code = encrypt(message, key)

print(decrypt(code, key))