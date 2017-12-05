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

    #f = ["qzmt-zixmtkozy-ivhz-343"]
    for line in f:
        
        parts = line[::-1].split('-', 1)
        parts[0], parts[1] = parts[1][::-1], parts[0][::-1]
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
        if s in passedLetters or s == '-':
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

def cipherToText(cipher, rots):
    # 97 - 122
    text = ""
    for c in cipher:
        if c == '-':
            text += ' '
        else:
            base = ord(c) - 97
            roted = (base + rots) % (123 - 97)
            val = roted + 97
            text += chr(val)
    return text


for room in rooms:
    #print room.name
    count = getCount(room.name)
    #showCount(count)
    checksum = orderCount(count)
    text = cipherToText(room.name, room.id)
    if checksum == room.checksum and text == "northpole object storage":
        print text, room.id
