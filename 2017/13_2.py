# doesnt work. sry

class Firewall:
	def __init__(self, level, layers):
		self.level = level
		self.layers = layers - 1
		self.scanner = 0
		self.dir = 1
	def scannerAdd(self):
		if self.scanner >= self.layers:
			self.dir = -1
		if self.scanner <= 0:
			self.dir = 1
		self.scanner += self.dir

def getLines(path):
	with open(path, 'r') as f:
		return [line.strip() for line in f]
	
def main():
	#lines = [l.split(' ') for l in getLines('13_0'.txt)]
	lines = getLines('13_0.txt')
	firewalls = []
	for l in lines:
		parts = map(int,l.split(':'))
		firewalls.append(Firewall(parts[0], parts[1]))
			
	packet = -1
	found = [None]
	startSec = 0
	while len(found) >  0:
		startSec += 1
		found = []
		packet = -1
		s = startSec
		for f in firewalls:
			scanner = startSec % (f.layers * 2)
			if scanner > f.layers:
				f.scanner = scanner - f.scanner
				f.dir = -1
			else:
				f.scanner = scanner
				f.dir = 1
			if f.scanner == f.layers:
				f.dir = -1
			if f.scanner == 0:
				f.dir = 1
		print startSec
		while packet < firewalls[-1].level:
			s += 1
			if s >= startSec:
				packet += 1
			thisF = None
			for f in firewalls:
				if f.level == packet:
					thisF = f
			if thisF != None and thisF.scanner == 0:
				found.append(thisF)
				break
			for f in firewalls:
				f.scannerAdd()

	print 
	print "Result:", startSec
	print reduce(lambda x,y: x + y, [f.level * (f.layers +1) for f in found], 0)

if __name__ == '__main__':
	main()
