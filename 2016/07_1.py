import re
def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def findABBAs(line):
	for i in xrange(len(line) - 4):
		part = line[i:i+4]
		if part[0] == part[-1] and part[1] == part[2] and part[0] != part[1]:
			yield part
	
def isInBrackets(line, abba):
	match = re.search('\[.+\]', line)
	if abba not in match.group(0):
		print line, abba
		return True
	return False

def main():
	supportTLS = []
	#lines = [l.split(' ') for l in getLines('07_0'.txt)]
	lines = getLines('07_0.txt')
	for line in lines:
		for abba in findABBAs(line):
			if not isInBrackets(line, abba):
				supportTLS.append(line)
	
	print len(supportTLS)

if __name__ == '__main__':
	main()
