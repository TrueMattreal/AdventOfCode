class Room:
    def __init__(self, name, id, checksum):
        self.name = name
        self.id = int(id)
        self.checksum = checksum

class Count:
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count

rooms = []
with open('4_0', 'r') as f:

    #f = ["aaaaa-bbb-z-y-x-123[abxyz]"]
    for line in f:
        parts = line.split('-')
        checksum = parts[-1].split('[')[-1][:-2]
        name = ''.join(parts[0:-1])
        id = parts[-1].split('[')[0]
        rooms.append(Room(name, id, checksum))

def getCount(string):
    letterCount = []
    passedLetters = []
    stringList = list(string)
    stringList.sort()
    for s in stringList:
        if s in passedLetters:
            continue
        passedLetters.append(s)
        letterCount.append(Count(s, string.count(s)))
    return letterCount
        
def orderCount(countList):
    checksum = ""
    for i in xrange(5):
        if len(countList) <= 0:
            break
        most = max(countList, key=lambda x: x.count)
        countList.remove(most)
        checksum += most.letter
    return checksum

def showCount(count):
    for c in count:
        print c.letter, c.count
        
sumOfIds = 0
for room in rooms:
    #print room.name
    count = getCount(room.name)
    #showCount(count)
    checksum = orderCount(count)
    if checksum == room.checksum:
        print room.id
        sumOfIds += room.id
print sumOfIds


