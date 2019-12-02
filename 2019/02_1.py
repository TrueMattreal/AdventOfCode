def getLines(path):
	with open(path, 'r') as f:
		return [line.strip().split(',') for line in f][0]

def main():
	items = [int(l) for l in getLines('02_0.txt')]
	inst = []
	for item in items:
		if len(inst) == 0 and item == 99:
			break
		if len(inst) < 4:
			inst.append(item)
			if len(inst) < 4:
				continue
		prog = inst[0]
		param1 = items[inst[1]]
		param2 = items[inst[2]]
		target = inst[3]
		print(inst)
		if prog == 1:
			items[target] = param1 + param2
		elif prog == 2:
			items[target] = param1 * param2
		else:
			print("mist", items)
			exit()
		inst = []

	print(items)

if __name__ == '__main__':
	main()
