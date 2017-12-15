hashKnot = __import__('10_2')

def main():
	input = "jzgqcdpd"
	
	output = ""
	for i in range(128):
		row = ""
		hash = hashKnot.main(input + '-' + str(i))
		for c in hash:
			row += bin(int(c, 16))[2:].zfill(4)
		output += row + '\n'
	print len([i for i in output if i == '1'])

if __name__ == '__main__':
	main()
