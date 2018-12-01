def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]

def main():
	#lines = [l.split(' ') for l in getLines('01_0'.txt)]
	lines = getLines('01_0.txt')
	freq = 0
	freqs = [0]
	lines = ['+3', '+3', '+4', '-2', '-4']
	while True:
		for l in lines:
			if l[0] == '+':
				freq += int(l[1:])
			else:
				freq -= int(l[1:])
			if (freq in freqs):
				print(freq)
				return
			freqs.append(freq)

if __name__ == '__main__':
	main()
