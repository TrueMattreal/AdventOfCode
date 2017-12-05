lines = []
with open('03_0.txt', 'r') as f:
    for line in f:
        numbers = []
        for number in filter(bool, line.split(' ')):
            numbers.append(int(number))
        lines.append(numbers)

def canBeTriangle(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False
    if sides[1] + sides[2] <= sides[0]:
        return False
    if sides[2] + sides[0] <= sides[1]:
        return False
    return True

possibles = 0
for lineIndex in xrange(0, len(lines), 3):
    for i in xrange(3):
        sides = (lines[lineIndex][i],
            lines[lineIndex + 1][i],
            lines[lineIndex + 2][i])
        print sides
        if canBeTriangle(sides):
            possibles += 1

print len(lines)
print possibles
