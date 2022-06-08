import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.lower()
    line = line.strip()
    for letter in line:
        counts[letter] = counts.get(letter,0) + 1
count = dict()
sum_number = 0
for i in counts.keys():
    sum_number += int(counts[i])
for i in sorted(counts):
    count[i] = (int(counts[i]) / sum_number)*100
print(count)
