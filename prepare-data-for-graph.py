import csv
import sys
import time

filename = sys.argv[1]
csvname = sys.argv[2]

thresholds = [0] * 1000

for i in range(1000):
    thresholds[i] = int(10 ** (float(i) / 100))

cnts = [0] * 1000

totalcnt = 0

start = time.time()

with open(filename, 'r') as f:
    for line in f:
        totalcnt += 1
        for i in range(1000):
            if int(line) <= thresholds[i]:
                cnts[i] += 1
        if totalcnt % 10000 == 0:
            end = time.time()
            print("Processed {} entries; time taken: {}".format(totalcnt, end - start))
            start = time.time()

data = []

for i, v in enumerate(cnts):
    data.append((thresholds[i], float(v) / totalcnt))

data = set(data)

with open(csvname, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

end = time.time()

print("Write complete; time taken: {}".format(end - start))

