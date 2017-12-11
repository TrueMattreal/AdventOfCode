def getLines(path):
	with open(path, 'r') as f:
		return f.readline().strip().split(',')

def main():
	cmds = getLines('11_0.txt')
	y = 0
	x = 0
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
	print x, y	
	# it was faster to calculate the rest (even if it was only three lines as you can see in 11_2)
	# so I got rank 45 :)
# 460 + 225

if __name__ == '__main__':
	main()
