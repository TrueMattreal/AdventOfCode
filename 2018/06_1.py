def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	lines = getLines('06_0.txt')
	coords = []
	for l in lines:
		coords.append(list(map(int, l.split(', '))))
	maxX = max(coords, key=lambda c: c[0])[0] + 1
	maxY = max(coords, key=lambda c: c[1])[1] + 1

	board = [[-1 for x in range(maxX)] for y in range(maxY)]
	for y in range(maxY):
		for x in range(maxX):
			shortestDist = maxX + maxY
			shortestId = -1
			for i, coord in enumerate(coords):
				dist = abs(coord[0] - x) + abs(coord[1] - y)
				if dist < shortestDist:
					shortestDist = dist
					shortestId = i
				elif dist == shortestDist:
					shortestId - 1
			if shortestId != -1:
				board[y][x] = shortestId

	blockedIds = []
	sizes = [0 for i in range(len(lines))]
	for y in range(maxY ):
		for x in range(maxX):
			if board[y][x] == -1:
				continue
			id = board[y][x]
			if x == 0 or x == maxX - 1 or y == 0 or y == maxY - 1:
				if id not in blockedIds:
					blockedIds.append(id)
				continue
			sizes[id] += 1
	m = -1
	for i, size in enumerate(sizes):
		if i not in blockedIds and size > m:
			m = size
	print(m)
	print(sizes)
	print(blockedIds)

if __name__ == '__main__':
	main()

# 5
# 3976