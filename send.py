import time

hasSent = 0
hasData = 0
dataFile = "data"
gotFile = "got"
gotData = False

st = "Hello, World!"

msg = ''.join([bin(ord(ch))[2:].zfill(8) for ch in st])
amt = 0

print("DATA: " + str(msg))
while hasSent is 0:
    time.sleep(.01)
    print("Loop: {}/{}".format(str(amt), str(len(msg))))
    print("Progess: {}/100".format(str(int(amt/len(msg)*100))))
    with open(gotFile) as f:
        hasData = f.read()
    if hasData is "1":
        with open(dataFile, "w") as f:
            f.write(str(msg[amt]))
            f.close()

        amt += 1
    with open(gotFile, "w") as f:
        f.write(str(0))
        f.close()
    if amt is len(msg):
        hasSent = 1
        print("DONE")
time.sleep(2)
with open(gotFile, "w") as f:
    f.write(str(2))
    f.close()
