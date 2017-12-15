hashKnot = __import__('10_2')

def containsHash(input):
	for i in input:
		for c in i:
			if c == '#':
				return True
	return False

def findConnected(rows):
	for y in range(len(rows)):
		for x in range(len(rows[y])):
			if rows[y][x] == '#':

def getAroud(rows, x, y):
	

def main():
	input = "jzgqcdpd"
	
	output = []
	for i in range(128):
		row = ""
		hash = hashKnot.main(input + '-' + str(i))
		for c in hash:
			row += bin(int(c, 16))[2:].zfill(4)
		output.append(row.replace('1', '#').replace('0', '.'))
	while containsHash(output):


if __name__ == '__main__':
	main()
