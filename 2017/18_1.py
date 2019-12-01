def getLines(path):
# 	return """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2""".split("\n")
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	lines = getLines('18_0.txt')
	vars = {}
	freq = 0
	jumps = 0
	i = 0
	while True:
		l = lines[i]
		#print(l)
		i += 1
		if i >= len(lines):
			i = 0
		parts = l.split(' ')
		cmd = parts[0]
		param1 = parts[1]
		if len(parts) > 2:
			param2 = parts[2]
			param2 = int(param2) if isInt(param2) else vars[param2]
		if cmd == 'snd':
			freq = vars[param1]
		elif cmd == 'set':
			vars[param1] = param2
		elif cmd == 'add':
			vars = addIfNotIn(vars, param1) 
			vars[param1] += param2
		elif cmd == 'mul':
			vars = addIfNotIn(vars, param1) 
			vars[param1] *= param2
		elif cmd == 'mod':
			vars = addIfNotIn(vars, param1) 
			vars[param1] %= param2
		elif cmd == 'rcv': 
			if freq != 0:
				return freq
		elif cmd == 'jgz':
			val = None
			if isInt(param1):
				val = int(param1)
			else:
				vars = addIfNotIn(vars, param1) 
				val = vars[param1]
			if val > 0:
				i += param2

def addIfNotIn(vars, var):
	if var not in vars:
		vars[var] = 0
	return vars

def isInt(var):
	try:
		int(var)
		return True
	except:
		return False

if __name__ == '__main__':
	print(main())
