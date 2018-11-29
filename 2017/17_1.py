def getLines(path):
	with open(path, 'r') as f:
		return [line.strip().split(' ') for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('17_0'.txt)]
	lines = getLines('17_0.txt')
	skip = 0
	registers = {}
	sound = []
	alpha = "abcdefghijklmnopqrstuvwxyz"
	for c in alpha[:17]:
		registers[c] = 0
	i = -1
	while i < len(lines):

		i += 1
		line = lines[i]
		cmd = line[0]
		if cmd == 'set':
			if line[2] in alpha:
				registers[line[1]] = registers[(line[2])]
			else:
				registers[line[1]] = int(line[2])
		elif cmd == 'add':
			if line[2] in alpha:
				registers[line[1]] += registers[line[2]]
			else:
				registers[line[1]] += int(line[2])
		elif cmd == 'mul':
			if line[2] in alpha:
				registers[line[1]] *= registers[line[2]]
			else:
				registers[line[1]] *= int(line[2])
		elif cmd == 'mod':
			if line[2] in alpha:
				registers[line[1]] %= registers[line[2]]
			else:
				registers[line[1]] %= int(line[2])
		elif cmd == 'rcv' and registers[line[1]] != 0:
			if len(sound) > 1: 
				sound.append(sound[-2])
		elif cmd == 'snd':
			sound.append(registers[line[1]])
		elif cmd == 'jgz':
			pos = 1
			if line[2] in alpha and registers[line[2]] < 0:
				pos = -1
			elif line[2] not in alpha and int(line[2]) > 0:
				pos = -1

			if line[1] in alpha:
				i += registers[(line[1])] * pos
			else:
				i += int(line[1]) * pos
			if pos < 0:
				i -= 1

	print sound, registers

if __name__ == '__main__':
	main()
