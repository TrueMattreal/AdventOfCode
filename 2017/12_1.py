def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
class Program:
	def __init__(self, id, contains):
		self.id = id
		self.contains = contains

def main():
	#lines = [l.split(' ') for l in getLines('12_0'.txt)]
	lines = getLines('12_0.txt')
	programs = []
	connectedToZero = []
	for line in lines:
		(id, connected) = line.split('<->', 1)
		connected = [int(c.strip()) for c in connected.split(',')]
		programs.append(Program(int(id), connected))
	length = 0
	connectedToZero.append(programs[0])
	while len(connectedToZero) != length:
		print length, len(connectedToZero)
		length = len(connectedToZero)
		for line in programs:
			if line in connectedToZero:
				continue
			for c in connectedToZero:
				if line.id in c.contains:
					connectedToZero.append(line)
					break

	print len(connectedToZero)	

if __name__ == '__main__':
	main()
