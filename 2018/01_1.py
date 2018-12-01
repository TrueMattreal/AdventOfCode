def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]

def main():
	#lines = [l.split(' ') for l in getLines('01_0'.txt)]
	lines = getLines('01_0.txt')
	freq = 0
	for l in lines:
		if l[0] == '+':
			freq += int(l[1:])
		else:
			freq -= int(l[1:])
	print(freq)

if __name__ == '__main__':
	main()
