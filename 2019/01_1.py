def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]

def main():
	lines = getLines('01_0.txt')
	total = 0
	for line in lines:
		total += int(int(line) / 3) - 2
	print(total)


if __name__ == '__main__':
	main()
