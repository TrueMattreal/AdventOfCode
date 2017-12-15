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
	found = []
	while packet < firewalls[-1].level:
		packet += 1
		thisF = None
		for f in firewalls:
			if f.level == packet:
				thisF = f
		if thisF != None and thisF.scanner == 0:
			found.append(thisF)
			#for f in firewalls:
			#	f.scannerAdd()
		for f in firewalls:
			f.scannerAdd()

	print [f.level for f in found]
	print reduce(lambda x,y: x + y, [f.level * (f.layers +1) for f in found], 0)

if __name__ == '__main__':
	main()
