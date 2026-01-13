# Morse Code Decoder
# Finds all possible decrypted messages

CODE_MAP = {
    ".": "E", "._": "A", "_": "T", "..": "I", "...": "S",
    "....": "H", ".._": "U", "..._": "V", "._.": "R",
    "._..": "L", ".__": "W", ".__.": "P", ".___": "J",
    "_..": "D", "_._": "K", "_._.": "C", "_.._": "X",
    "__": "M", "__.": "G", "__..": "Z", "__._": "Q",
    "___": "O", "_...": "B", ".._.": "F", "_.": "N",
    "_.__": "Y"
}

def decode(encrypted, index, current, results):
    if index == len(encrypted):
        results.append(current)
        return

    for code, letter in CODE_MAP.items():
        if encrypted.startswith(code, index):
            decode(encrypted, index + len(code), current + letter, results)

encrypted = "__.._...__"
results = []
decode(encrypted, 0, "", results)

for r in results:
    print(r)
