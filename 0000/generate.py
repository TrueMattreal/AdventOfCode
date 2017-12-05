sourceFileContent = """def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('{0}_0'.txt)]
	lines = getLines('{0}_0.txt')

	print lines	

if __name__ == '__main__':
	main()
"""


for i in xrange(1, 26):
	day = '{:0>2}'.format(i)
	for j in xrange(3):
		with open(day + '_' + str(j) + ('.py' if j > 0 else '.txt'), 'w') as f:
			if j == 0:
				f.write("")
			else:
				f.write(sourceFileContent.format(day))