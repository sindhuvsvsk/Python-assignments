import os


def readfile(fileobj):
    fileobj.readline()
    while True:
        data = fileobj.readline()
        if not data:
            break
        yield data


path = ".\data"
print("Current working directory \n %s" % os.getcwd())
os.chdir(path)
print("Directory changed successfully \n %s" % os.getcwd())


d = {}
for file in os.listdir("."):
    with open(file, 'r') as f:
        for line in readfile(f):
            airline = line.strip().split(',')[4]
            d[airline] = d.get(airline, 0) + 1
flightsbyairline = sorted(d.items(), key=lambda x: x[1], reverse=True)
total = str(sum(d.values()))
os.chdir("..")
with open('flights_by_airline.csv', 'w+') as f1:
    f1.write("Airlines, #Flights\n")
    for s in flightsbyairline:
        f1.write("%s, %s \n" % (s[0], s[1]))
    f1.write('Total,' + total)
