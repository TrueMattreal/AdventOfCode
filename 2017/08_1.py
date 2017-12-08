class Instruction:
	def __init__(self, register, value, condition):
		self.register = register
		self.value = value
		self.condition = condition
	def executeIfTrue(self, registers):
		parts = self.condition.split(' ')
		if not parts[0] in registers:
			registers[parts[0]] = 0
		if not self.register in registers:
			registers[self.register] = 0			
		parts[0] = registers[parts[0]]
		print ' '.join([str(p) for p in parts])
		if eval(' '.join([str(p) for p in parts])):
			registers[self.register] += self.value

def getInstruction(line):
	parts = line.split(' ')
	value = (-1 if parts[1] == 'dec' else 1) * int(parts[2])
	return Instruction(parts[0], value, ' '.join(parts[4:]))

def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]


def main():
	#lines = [l.split(' ') for l in getLines('08_0'.txt)]
	lines = getLines('08_0.txt')
	registers = {}
	instructions = [getInstruction(l) for l in lines]
	for i in instructions:
		i.executeIfTrue(registers)
	print registers[max(registers, key=lambda x: registers.get(x))]

if __name__ == '__main__':
	main()
