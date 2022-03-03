import urllib.request as urllib
import json

feb_weather_data = []
finallist = []
tempforeachdate = {}
for number in range(1, 30):
    response = urllib.urlopen('https://www.metaweather.com/api/location/2487956/2020/2/%s' % number)
    data = response.read()
    feb_weather_data.append(json.loads(data.decode("utf-8")))
for entry in feb_weather_data:
    filteredlist = filter(lambda entry: entry['created'].split('T')[0] == entry['applicable_date'], entry)
    finallist.append(list(filteredlist))
for eachday in finallist:
    total = 0
    count = 0
    max_temp = max(eachday, key=lambda x: x['the_temp'])
    min_temp = min(eachday, key=lambda x: x['the_temp'])
    for x in eachday:
        total = total + x['the_temp']
        count = count + 1
    avg = total / count
    tempforeachdate.update({max_temp['applicable_date']: [max_temp['the_temp'], min_temp['the_temp'], avg]})
with open("temp_stats.json", "w") as json_file:
    json.dump(tempforeachdate, json_file)
with open("temp_stats.json", "r") as json_file:
    content = json_file.read()
print(content)
