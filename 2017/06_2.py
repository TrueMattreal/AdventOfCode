def getLines(path):
	with open(path, 'r') as f:
		return [int(i) for i in [line.strip().split('\t') for line in f][0]]
	
def main():
	#lines = [l.split(' ') for l in getLines('06_0'.txt)]
	seen = []
	line = getLines('06_0.txt')
	#line = [0,2,7,0]

	while not line in seen:
		seen.append(line)
		line = [i for i in line]
		mI = line.index(max(line))
		x = line[mI]
		line[mI] = 0
		i = mI + 1
		while x > 0:
			i %= len(line)
			if x / (len(line) - 1) < 0:
				line[i] = x;
				x = 0
			else:
				line[i] += 1
				x -= 1
			i += 1

	print len(seen) - seen.index(line)

if __name__ == '__main__':
	main()