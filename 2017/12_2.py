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
	groups = []
	for line in lines:
		(id, connected) = line.split('<->', 1)
		connected = [int(c.strip()) for c in connected.split(',')]
		programs.append(Program(int(id), connected))
	length = 0
	groups.append([programs[0]])
	programs.pop(0)
	while len(programs) > 0:
		if len(groups[-1]) != length:
			length = len(groups[-1])
		else:
			groups.append([programs[0]])
			programs.pop(0)

		for i in range(20):
			for p in programs:
				for c in groups[-1]:
					if p.id in c.contains or c.id in p.contains:
						groups[-1].append(p)
						programs.pop(programs.index(p))
						break
	print len(groups), [len(g) for g in groups]


if __name__ == '__main__':
	main()
