passphrases = []
lines = 0
with open('04_0.txt', 'r') as f:
	for line in f:
		lines += 1
		words = line[:-1].split(' ')
		
		unique = set(words)
		if len(words) == len(unique):
			passphrases.append(unique)

sort = []
real = 0
for passphrase in passphrases:
	sort = []
	for word in passphrase:
		sort.append(''.join(sorted(word)))
	

	if len(set(sort)) == len(passphrase):
		real += 1
		
print real