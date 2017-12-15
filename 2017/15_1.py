

def main():
	genA = [277]
	genB = [349]
	genAMul = 16807
	genBMul = 48271

	same = 0
	for i in xrange(40000000):
		foo = genA[-1] * genAMul
		foo %= 2147483647
		genA.append(foo)
		foo = genB[-1] * genBMul
		foo %= 2147483647
		genB.append(foo)
		if bin(genA[-1])[-16:] == bin(genB[-1])[-16:]:
			same += 1



	print same	

if __name__ == '__main__':
	main()
