
def getLines(path):
	with open(path, 'r') as f:
		return [int(line.strip()) for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('05_0'.txt)]
	ins = getLines('05_0.txt')
	i = 0
	steps = []
	while i < len(ins):
		steps.append(ins[i])
		cmd = ins[i]
		if cmd >= 3:
			ins[i] -= 1
		else:
			ins[i] += 1
		i += cmd
		

	print len(steps)

if __name__ == '__main__':
	main()

	# 25136209