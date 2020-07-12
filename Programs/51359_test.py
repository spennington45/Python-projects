f = open("data.txt", "r")
write1 = open("dataplus.txt", "w")
write2 = open("dataminus.txt", "w")

for line in f:
	if int(line) > 0:
		write1.write(line)
	elif int(line) < 0: 
		write2.write(line)
		
f.close()
write1.close()
write2.close()
