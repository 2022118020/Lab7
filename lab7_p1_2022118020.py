import re

f = open('input_7_1.txt', 'r')
f_list = [0]
for line in f :
    f_list.append(line.strip())

function_list = {}

for l in range(len(f_list)) :
    match = re.search(r'def \w+', str(f_list[l]))
    if match :
        function_list[match.group()[4:]] = [l]

print(function_list)

for function in function_list.keys() :
    for l in range(len(f_list)) :
        match = re.search((function +'[\s]*\('), str(f_list[l]))
        if match :
            temp_list = match.group()
            if l not in function_list[function] :
                function_list[function].append(l)

for x, y in function_list.items() :
    print('%s: def in %d, calls in' %(x, y[0]), y[1:])