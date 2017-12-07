import re

test = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

class Disk:
	def __init__(self, name, w, holding):
		self.name = name
		self.w = w
		self.holding = holding
		self.objects = []

def getDisk(line):
	name = line.split(' ')[0]
	m = re.search('\d+', line)
	w = int(m.group(0)) if not m == None else 0
	holding =  [s.strip() for s in line.split('->')[-1].split(',')] if '->' in line else []
	return Disk(name, w, holding)

def getLines(path):
	with open(path, 'r') as f:
		return [getDisk(line) for line in f]
	#return [getDisk(line) for line in test.split('\n')]
	
def isInHoldings(disk, disks):
	for d in disks:
		if disk.name in d.holding:
			return True
	return False

def main():
	#lines = [l.split(' ') for l in getLines('07_0'.txt)]
	disks = getLines('07_0.txt')
	for disk in disks:
		#print disk.name, disk.w, disk.holding
		if not isInHoldings(disk, disks):
			print disk.name

if __name__ == '__main__':
	main()
