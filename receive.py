hasData = 0
dataFile = "data"
gotFile = "got"
gotData = False

with open(gotFile, "w") as f:
    f.write(str(1))
    f.close()

e = ""
print("Waiting for data...")
while True:
    with open(gotFile) as f:
        hasData = f.read()
        if hasData is "2":
            break
    if hasData is "0":
        while not gotData:
            with open(dataFile) as f:
                bit = f.read()

                print("BIT: " + bit)
                if bit is "":
                    gotData = False
                else:
                    gotData = True
        e += bit
        with open(gotFile, "w") as f:
            f.write(str(1))
            f.close()
        gotData = False

a = ""

n = 8
split = [e[i:i+n] for i in range(0, len(e), n)]
print("Data recived: " + str(split))
loop = 0
for i in split:
    t = split[loop]
    r = int(t, 2)
    a += str(chr(r))
    loop += 1
print("Message Converted: " + a)
