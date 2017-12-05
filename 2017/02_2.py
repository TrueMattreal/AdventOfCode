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

def getEvenDiv(nums):
    for num in rows[i]:
        for x in rows[i]:
            if num % x == 0 and num != x:
                print num, x
                return num, x
diffs = 0
for i in xrange(len(rows)):
    nums = []
    top, low = getEvenDiv(rows)
                
            
    diffs += top / low
print diffs
# 35860
# 37738 too igh
