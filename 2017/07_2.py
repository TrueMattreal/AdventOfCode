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

class Disc:
	def __init__(self, name, weight, holdingDiscsName):
		self.name = name
		self.weight = weight
		self.holdingDiscsName = holdingDiscsName
		self.holding = []

	def findHoldings(self, discs):
		for disk in discs:
			if disk.name in self.holdingDiscsName:
				yield disk
	def getWeights(self):
		if len(self.holding) <= 0:
			return self.weight
		return sum(map(Disc.getWeights, self.holding)) + self.weight
	def getDiscs(self):
		for disc in self.holding:
			yield disc
		yield self
	def isBalanced(self):
		weights = []
		for hold in self.holding:
			weights.append(hold.getWeights())
		return len(set(weights)) <= 1
	def getOddDisc(self):
		weights = []
		for disc in self.holding:
			weights.append(disc.getWeights())
		for weight in weights:
			if weights.count(weight) <= 1:
				return self.holding[weights.index(weight)]
			
	@staticmethod
	def getDisc(line):
		name = line.split(' ')[0]
		m = re.search('\d+', line)
		w = int(m.group(0)) if not m == None else 0
		holding =  [s.strip() for s in line.split('->')[-1].split(',')] if '->' in line else []
		return Disc(name, w, holding)

def getLines(path):
	with open(path, 'r') as f:
		return [line for line in f]
	return [line for line in test.split('\n')]

def getBase(discs):
	for disc in discs:
		if not disc.name in flattenList([d.holdingDiscsName for d in discs]):
			return disc

def flattenList(l):
	items = []
	for sublist in l:
		for item in sublist:
			items.append(item)
	return items

def main():
	#lines = [l.split(' ') for l in getLines('07_0'.txt)]
	discs = [Disc.getDisc(line) for line in getLines('07_0.txt')]
	for disc in discs:
		disc.holding = [d for d in disc.findHoldings(discs)]
	base = getBase(discs)
	bases = []
	while not base.isBalanced():
		bases.append(base)
		base = base.getOddDisc()
	
	ma = max(bases[-1].holding, key=lambda x: x.getWeights())
	mi = min(bases[-1].holding, key=lambda x: x.getWeights())
	print ma.weight - (ma.getWeights() - mi.getWeights())


if __name__ == '__main__':
	main()
# 17561