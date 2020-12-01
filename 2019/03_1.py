def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]

def getPairs(list):
	for i, item in enumerate(list):
		if item == list[-1]:
			break;
		yield item, list[i + 1]

def getDir(pair):
	return 'H' if pair[0]['x'] == pair[1]['x'] else 'V'

def main():
	lines = [l.split(',') for l in getLines('03_0.txt')]
	paths = []
	for instSet in lines:
		x = 0
		y = 0
		points = []
		for inst in instSet:
			dir = inst[0]
			dis = int(inst[1:])
			if dir == 'R':
				x += dis
			if dir == 'L':
				x -= dis
			if dir == 'U':
				y -= dis
			if dir == 'D':
				y += dis
			points.append({'x': x, 'y': y})
		paths.append(points)
	intersections = []
	for pi, path in enumerate(paths):
		for pair in getPairs(path):
			for otherPath in paths[i + 1]:
				for otherPair in getPairs(otherPath):
					firstDir = getDir(pair)
					secondDir = getDir(otherPair)
					if (firstDir == secondDir):
						continue
					if firstDir

	print(intersections)

if __name__ == '__main__':
	main()
