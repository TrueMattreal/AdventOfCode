from collections import Counter

def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('02_0'.txt)]
	lines = getLines('02_0.txt')
	allCounts = {}
	for l in lines:
		counts = Counter(l)
		already = []
		linesCounts ={}
		for key in counts:
			times = counts[key]
			if times in already or times == 1:
				continue
			if times not in linesCounts:
				linesCounts[times] = 0
			linesCounts[times] += 1	
			already.append(times)

		print(allCounts)
		for key in linesCounts:
			if key not in allCounts:
				allCounts[key] = 0
			allCounts[key] += 1

	checksum = 1
	for key in allCounts:
		checksum *= allCounts[key]
	print(checksum)

if __name__ == '__main__':
	main()
