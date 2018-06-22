f = open("userpoints.txt", "r")

wholelist=[]
for line in f.readlines():
        line = line.split()
        wholelist.append(line)
        #print(line)


wholelist.sort(key=lambda x: float(x[1]))

print('/n/n/n/n')

for x in wholelist:
        print(x)


print(len(wholelist))
