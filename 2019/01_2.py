def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]

def main():
	lines = getLines('01_0.txt')
	total = 0
	for i, line in enumerate(lines):
		fuel = int(line)
		while True:
			fuel = int(fuel / 3) - 2
			if fuel <= 0:
				break;
			total += fuel
	print(total)


if __name__ == '__main__':
	main()
