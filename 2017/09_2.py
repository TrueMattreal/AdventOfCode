def getLines(path):
	#return "<{o\"i!a,<{i<a>"
	with open(path, 'r') as f:
		return f.readline().strip()
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('09_0'.txt)]
	line = getLines('09_0.txt')
	nextIgnore = False
	groupIndex = 0
	groups = []
	garbage = []
	openAngle = False
	for c in line:
		if nextIgnore:
			nextIgnore = False
			continue
		if c == '!':
			nextIgnore = True
			continue
		if openAngle:
			if c == '>':
				openAngle = False
				continue
			garbage.append(c)
			continue
		if c == '<':
			openAngle = True
			continue
		if c == '{':
			groupIndex += 1
			continue
		if c == '}':
			if groupIndex > 0:
				groups.append(groupIndex)
				groupIndex -= 1
				continue

	print garbage, len(garbage)	

if __name__ == '__main__':
	main()
