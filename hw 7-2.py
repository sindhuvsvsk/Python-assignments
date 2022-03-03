import os
import re
from dateutil.parser import parse
from collections import OrderedDict

output = list(os.popen("ls -l"))
words = len((output[0].split(" ")))
if words == 2:
    output = output[1:]
file_size = 0
dateandfiledict = {}
for line in output:
    words = re.search(
        r'(\d+) ([a-zA-Z]+ .\d+ \d{2}:\d{2}|[a-zA-Z]+ .\d+ .\d{4}) ([A-Z]{4}\d{3} [A-Z]{2}\d{1}.[a-z]{3}|[a-zA-Z.]+)',
        line)
    file_size = file_size + int(words.group(1))
    date = words.group(2)
    file = words.group(3)
    dateandfiledict[date] = file
print(f"Total file size : {file_size}")
final = OrderedDict(sorted(dateandfiledict.items(), key=lambda date: parse(date[0])))
print("Earliest modified file and its time of modification:" + str(list(final.items())[0]))
print("latest modified file and its time of modification:" + str(list(final.items())[-1]))
