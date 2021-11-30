import re
import enchant

eng_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '.': '.-.-.-', '?': '..--..', ',': '--..--', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

morse_to_eng = {'....': 'h', '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.-.-.-': '.', '..--..': '?', '--..--': ',', '/': ' '}

def decrypt(message):
    to_ret = ""
    words = message.split("   ")
    for word in words:
            letters = word.split(" ")
            for l in letters:
                if l == "":
                    continue
                to_ret += morse_to_eng[l]
            to_ret += " "

def encrypt(message):
    to_ret = ""
    message = message.lower()
    for c in message:
        if c in eng_to_morse.keys():  
            to_ret += eng_to_morse[c] + ""
        else:
            pass   
    return to_ret

def check_equ(data, message):
    if len(data) != len(message):
        return False
    for i, _ in enumerate(data):
        if data[i] == "x":
            continue
        elif data[i] != message[i]:
            return False
    return True


f = open(r"book.txt", "rb")
book = f.read().decode().replace("\r", " ").replace("\n", " ")

book = book.replace("“", " ")
book = book.replace("’", " ")
book = book.replace("‘", " ")
book = book.replace("”", " ")
book = book.replace("*", " ")
book = book.replace("$", " ")
book = book.replace(",", " ")
book = book.replace(".", " ")
book = book.replace(":", " ")
book = book.replace("?", " ")
book = book.replace("#", " ")
book = book.replace("@", " ")
book = book.replace("!", " ")
book = book.replace("%", " ")

f.close()

data = "x.xx...x.xxx..-xx-.xxxx.-.-xxx.-.x..x.xxxx..x.xxx.-.-.xx-.-xxx..-.xx.x.x.--x.xxx"

b = book.split(" ")
d = enchant.Dict("en_US")

b = list(filter(lambda s: s != "" and d.check(s), b))
print("Finished filtering words.")

next_i = 0
curr_i = 0

while next_i != len(b):
    words = b[curr_i:next_i]
    morsed = encrypt("".join(words))
    if check_equ(data, morsed):
        print(words)
        break

    if len(data) >= len(morsed):
        next_i+=1
    else:
        curr_i+=1












