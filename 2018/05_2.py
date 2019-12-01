def getLine(path):
	with open(path, 'r') as f:
		for line in f:
			return line.strip()
	
def main():
	line = getLine('D:\\Projects\\AdventOfCode\\2018\\05_0.txt')
	changed = True
	m = 50000
	for c  in 'abcdefghijklmnopqrstuvwxyz':
		tempM = len(line.replace(c, '').replace(c.upper(), ''))
		if tempM < m:
			m = tempM
	print(m)

if __name__ == '__main__':
	main()

#47962