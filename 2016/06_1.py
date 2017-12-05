word = ""
counts = {}
with open('06_0.txt', 'r') as f:
	for line in f:
		line = line.strip()
		for i, c in enumerate(list(line)):
			if not i in counts:
				counts[i] = {}
			if not c in counts[i]:
				counts[i][c] = 1
			else:
				counts[i][c] += 1


for i in counts:
	letters = counts[i]
	word += min(letters, key=lambda x: letters[x])
	
print word