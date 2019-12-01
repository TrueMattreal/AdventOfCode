def getLine(path):
	with open(path, 'r') as f:
		for line in f:
			return line.strip()
	
def main():
	line = getLine('D:\\Projects\\AdventOfCode\\2018\\05_0.txt')
	changed = True
	while changed:
		changed = False
		for i in range(len(line) - 1):
			if line[i] != line[i + 1] and (line[i].upper() == line[i + 1] or line[i].lower() == line[i + 1]):
				lineFront = line[:i]
				lineBack = line[i + 2:]
				line = lineFront + lineBack
				changed = True
				break
	print(len(line))

if __name__ == '__main__':
	main()

# 7782
# 34436
# 33768
# 12292