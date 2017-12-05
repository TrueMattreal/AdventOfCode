class Cell:
	def __init__(self, x, y, val):
		self.x = x
		self.y = y
		self.val = val

def goDirection(x, y, direction, length = 1):
	direction %= 4
	if direction == 0:
		y += length
	if direction == 1:
		x += length
	if direction == 2:
		y -= length
	if direction == 3:
		x -= length
	return x, y
		
def shouldGoLeft(x, y):
	if x == y:
		return True
	if x < 0 and y > 0 and abs(x) == y:
		return True
	if x > 0 and y <= 0 and x - 1 == abs(y):
		return True
	return False

def getVal(x, y, cells):
	val = 0
	for cell in cells:
		if cell.x >= x - 1 and cell.x <= x + 1 and cell.y >= y - 1 and cell.y <= y + 1:
			val += cell.val
	return val
	
goal = 289326
cells = []
direction = 1
while len(cells) <= 0 or cells[-1].val < 289326:
	if len(cells) <= 0:
		cells.append(Cell(0, 0, 1))
		continue
	x, y = goDirection(cells[-1].x, cells[-1].y, direction)
	cell = Cell(x, y, getVal(x, y, cells))
	cells.append(cell)
	if shouldGoLeft(x, y):
		direction -= 1

print cells[-1].val