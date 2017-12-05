import re
def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def findABAs(line):
	line = re.sub('\[.+?\]', '', line)
	for i in xrange(len(line)):
		part = line[i:i+3]
		if len(part) == 3 and part[0] == part[2] and part[0] != part[1]:
			yield part
	
def insideOut(s):
	return s[1] + s[0] + s[1]
	
def isInsideOutInBrackets(line, aba):
	matches = re.findall('\[.+?\]', line)
	for match in matches:
		if insideOut(aba) in match:
			print match, insideOut(aba)
			return True
	return False

def supportsSSL(line):
	for aba in findABAs(line):
		if isInsideOutInBrackets(line, aba):
			return True
	return False
	
def main():
	supportSSL = []
	#lines = [l.split(' ') for l in getLines('07_0'.txt)]
	lines = getLines('07_0.txt')
	for line in lines:
		if supportsSSL(line):
			supportSSL.append(line)
	
	print len(supportSSL)

if __name__ == '__main__':
	main()
