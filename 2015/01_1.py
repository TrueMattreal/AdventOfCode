def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('01_0'.txt)]
	lines = getLines('01_0.txt')

	print lines	

if __name__ == '__main__':
	main()
