def getLengths(path):
	with open(path, 'r') as f:
		return  f.readline().strip()

def getSublist(l, s, e):
	return [l[i%len(l)] for i in xrange(s, s + e)]

def setSublist(l, s, sl):
	newList = list(l)
	for i in xrange(len(sl)):
		newList[(s + i)%len(newList)] = sl[i]
	return newList

def main():
	lengths = [ord(c) for c in getLengths('10_0.txt')]
	lengths.extend([17,31,73,47,23])
	input = [i for i in xrange(256)]
	skip = 0
	i = 0
	for round in xrange(64):
		for length in lengths:
			sublist = getSublist(input, i , length)
			sublist = sublist[::-1]
			input = setSublist(input, i, sublist)

			i += length + skip
			i %= len(input)
			skip += 1
	solution = input
	print solution
	denseHash = []
	for i in xrange(16):
		denseHash.append(reduce(lambda x,y: x^y, solution[16*i:16*i+16]))

	print ''.join([hex(h)[2:].zfill(2) for h in denseHash])

if __name__ == '__main__':
	main()
