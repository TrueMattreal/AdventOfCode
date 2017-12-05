class Row:
    def __init__(self, numbers):
        self.numbers = numbers

rows = []
with open('02_0.txt', 'r') as f:
    for line in f:
        values = filter(bool, line.split('\t'))
        numbers = []
        for val in values:
            numbers.append(int(val))
        rows.append(numbers)

diffs = 0
for row in rows:
    top = max(row)
    low = min(row)
    diffs += top - low

print diffs
