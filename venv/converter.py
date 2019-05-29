f = open("keyword.txt", 'r')
g = open("convertedkw.txt","w")
while True:
    line = f.readline()
    if not line: break
    line = line.replace("\n","\",\"")
    g.write(line)
f.close()
g.close()