import re

def count(alphabet, text):
    regex = '[' + alphabet + alphabet.lower() + ']'
    match = re.findall(regex, text)
    return len(match)

f = open('input_7_2.txt', 'r')
alphabets = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,
            'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0,
            'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0,
            'Y':0, 'Z':0}

for x in alphabets.keys() :
    alphabets[x] += count(x, f.read())
    f.seek(0)

print(alphabets)

list_alphabet = []
list_count = []

for x, y in alphabets.items() :
    list_count.append(y)

list_count.sort(reverse=True)
print(list_count)

for c in list_count :
    for x, y in alphabets.items() :
        if c > 0 and c == y :
            if x not in list_alphabet :
                list_alphabet.append(x)

print(list_alphabet)