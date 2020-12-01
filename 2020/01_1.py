def getLines(path):
	with open(path, 'r') as f:
		return [int(line.strip()) for line in f]
	
def main():
	lines = getLines('01_0.txt')
	for start, x in enumerate(lines):
		for y in lines[start + 1:]:
			if y + x == 2020:
				print(x, y, x*y)
				exit()

if __name__ == '__main__':
	main()
