def getLines(path):
	#return [3, 4, 1, 5]
	with open(path, 'r') as f:
		return map(int, f.readline().strip().split(','))
	
def getInput(path):
	with open(path, 'r') as f:
		return  f.readline().strip()

def getSublist(l, s, e):
	return [l[i%len(l)] for i in xrange(s, s + e)]

def setSublist(l, s, sl):
	newList = list(l)
	for i in xrange(len(sl)):
		newList[(s + i)%len(newList)] = sl[i]
	return newList

def main():
	#lines = [l.split(' ') for l in getLines('10_0'.txt)]
	lengths = getLines('10_0.txt')
	numbers = [i for i in xrange(256)]
	skip = 0
	i = 0
	numbersList = [numbers]
	for length in lengths:
		sublist = getSublist(numbers, i , length)
		sublist = sublist[::-1]
		numbers = setSublist(numbers, i, sublist)
		numbersList.append(numbers)

		i += length + skip
		i %= len(numbers)
		skip += 1

	solution = numbersList[-1]
	print solution[0] * solution[1], solution

if __name__ == '__main__':
	main()
