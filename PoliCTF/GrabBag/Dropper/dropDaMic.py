# Copied and updated from: http://code.activestate.com/recipes/578407-simple-morse-code-translator-in-python/
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', '-': '-....-', '{': '.--.-', 
        '}': '.--.--'
        }
# Extended characters found here: https://github.com/agwells/dotdash-keyboard-android/wiki/Wells-extended-Morse-code

f = open("drop.txt", "r")
s = f.readlines()[0]

morse = s.replace("11111", "\n").replace("0000", "- ").\
          replace("000", "-").replace("11", " ").replace("1", "").replace("0", ".")


flag = ""

for word in morse.split("\n"):

    for unit in word.split(" "):
        for char in CODE:
            if CODE[char] == unit:
                flag += char
    # This is where the 5 11111's were
    flag += "\n"

# Hint said flag was lowercase
print flag.lower()

# RyanAiden
