import md5

input = "ojvtpuvg"
# input = "abc"
password = ""
i = 0
while len(password) < 8:
	hash = md5.new(input + str(i)).hexdigest()
	if hash.startswith("00000"):
		password += hash[5]
	i += 1

print password