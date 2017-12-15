def x(lst, mul, mod):
	last = lst[-1]
	while len(lst) < 5000000:
		last = (last * mul) % 2147483647
		if last % mod == 0:
			lst.append(last)
	return lst

def main():
	genA = [277]
	genB = [349]
	genAMul = 16807
	genBMul = 48271
	genA = x(genA, genAMul, 4)
	print "A"
	genB = x(genB, genBMul, 8)
	print "B"

	same = 0
	for i in xrange(min([len(genA), len(genB)])):
		if bin(genA[i])[-16:] == bin(genB[i])[-16:]:
			same += 1
	print same	

if __name__ == '__main__':
	main()
