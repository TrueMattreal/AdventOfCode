# needs some time

def getCmds(path):
	with open(path, 'r') as f:
		return f.readline().strip().split(',')
	
def main():
	lines = getCmds('16_0.txt')
	programs = list("abcdefghijklmnop")
	for i in xrange(1000000000):
		line = lines[i%len(lines)]
		if i % 1000000 == 0:
			print i
		move = line[0]
		params = line[1:].split('/')
		if move == 's':
			i = int(params[0])
			programs = programs[-i:] + programs[:len(programs)-i]
		elif move == 'p':
			i = programs.index(params[0])
			j = programs.index(params[1])
			programs[i] = params[1]
			programs[j] = params[0]
		elif move == 'x':
			i = int(params[0])
			j = int(params[1])
			programs[i], programs[j] = programs[j], programs[i]
	print ''.join(programs)

if __name__ == '__main__':
	main()