alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
encryptedAlphabet = []
encryptedBy = 1

gen = lambda l, n: l[-n:] + l[:-n]


def encrypt(to):
    cipher = ""

    for char in list(to):
        index = alphabet.index(char)
        encryptedChar = encryptedAlphabet[index]
        cipher += encryptedChar

    return cipher


encryptedAlphabet = gen(alphabet, encryptedBy)
word = raw_input("what word would you like to encrypt?")
print("encrypted >> ", encrypt(word))
