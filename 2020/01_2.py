def getLines(path):
	with open(path, 'r') as f:
		return [int(line.strip()) for line in f]
	
def main():
	lines = getLines('01_0.txt')
	for start, x in enumerate(lines):
		for start2, y in enumerate(lines[start + 1:]):
			for z in lines[start2 + 1:]:
				if y + x + z == 2020:
					print(x, y, z, x*y*z)
					exit()

if __name__ == '__main__':
	main()
