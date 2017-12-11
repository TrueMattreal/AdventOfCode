def getLines(path):
	with open(path, 'r') as f:
		return f.readline().strip().split(',')

def getDistance(x,y):
	dis = x / 0.5
	i = y - x
	dis += i
	return dis

def main():
	cmds = getLines('11_0.txt')
	y = 0
	x = 0
	m = 0
	for cmd in cmds:
		if cmd == 'n':
			y+=1
		if cmd == 's':
			y-=1
		if cmd == 'nw':
			y+=0.5
			x-=0.5
		if cmd == 'ne':
			y+=0.5
			x+=0.5
		if cmd == 'sw':
			y-=0.5
			x-=0.5
		if cmd == 'se':
			y-=0.5
			x+=0.5
		dis = getDistance(x, y)
		if dis > m:
			m = dis
			print x, y
	print m

if __name__ == '__main__':
	main()
