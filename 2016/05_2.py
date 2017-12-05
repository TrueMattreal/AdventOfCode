import md5
import hashlib 

input = "ojvtpuvg"
#input = "abc"
password = [None for i in xrange(8)]
i = -1
while None in password:
	i += 1
	hash = hashlib.md5(input + str(i)).hexdigest()
	if hash.startswith("00000"):
		if hash[5] in "abcdef":
			continue
		index = int(hash[5])
		if index >= 8:
			continue
		if password[index] != None:
			continue
		password[index] = hash[6]
		print password, i
	if i % 1000000 == 0: print i
	
print "".join(password)