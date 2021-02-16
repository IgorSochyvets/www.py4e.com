import time

list = []
count = 0
total = 0
spam = 0

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        print(line.strip())
        atpos = line.find(' ')
        dataString = line[atpos+1:].strip()
        total = total + float(dataString)
        count = count + 1
#    time.sleep(0.01)
spam = round(total / count, 4)
print("The average spam confidence: ", spam)