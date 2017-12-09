def getLines(path):
	#return "{{<!>},{<!>},{<!>},{<a>}}"
	with open(path, 'r') as f:
		return f.readline().strip()
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('09_0'.txt)]
	line = getLines('09_0.txt')
	nextIgnore = False
	groupIndex = 0
	groups = []
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

	print sum(groups)	

if __name__ == '__main__':
	main()
