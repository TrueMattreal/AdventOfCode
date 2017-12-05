passphrases = 0
lines = 0
with open('04_0.txt', 'r') as f:
	for line in f:
		lines += 1
		words = line[:-1].split(' ')
		
		unique = set(words)
		if len(words) == len(unique):
			passphrases += 1
		else:
			print words, unique, len(words), len(unique)
print passphrases, lines