import difflib

def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('02_0'.txt)]
	lines = getLines('02_0.txt')
	#for i,s in enumerate(difflib.ndiff(a, b)):
	for x in range(len(lines)):
		for y in range(x, len(lines)):
			changes = 0
			same = []
			for s in difflib.ndiff(lines[x], lines[y]):
				if s[0] in ['+', '-']:
					changes += 1
				else:
					same.append(s.strip())
			if changes == 2:
				print(''.join(same))

if __name__ == '__main__':
	main()
