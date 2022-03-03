import pandas as pd
import statistics as stat
import numpy as np

cities = pd.read_csv("cities.csv")
cities.isnull().sum()
# Replaced null values with corresponding mean values of the column
cities.fillna(cities.mean(), inplace=True)

area_km = sorted(zip(cities['city'], (cities['area_total_km2'])), key=lambda x: x[1])
print("Smallest city in terms of area in kms: %s" % (str(area_km[0])))
print("Largest city in terms of area in kms: %s" % (str(area_km[-1])))
print()

breakpoint()
area_mi = sorted(zip(cities['city'], (cities['area_total_sq_mi'])), key=lambda x: x[1])
print("Smallest city in terms of area in miles: %s" % (str(area_mi[0])))
print("Largest city in terms of area in miles: %s" % (str(area_mi[-1])))
print()

print("Top 10 cities in terms of elevation in meters:")
ele_m = sorted(zip(cities['city'], cities['elevation_m']), key=lambda x: x[1], reverse=True)[:10]
for city_elevation in ele_m:
    print(city_elevation)

print()
print("Top 10 cities in terms of elevation in feet:")
ele_ft = sorted(zip(cities['city'], cities['elevation_ft']), key=lambda x: x[1], reverse=True)[:10]
for city_elevation in ele_ft:
    print(city_elevation)
print()

area_total = cities['area_total_sq_mi']
print(f"Average total area in miles:{stat.mean(area_total):8,.4f}")
area_land = cities['area_land_sq_mi']
print(f"Average land area in miles:{stat.mean(area_land):8,.4f}")
area_water = cities['area_water_sq_mi']
print(f"Average water area in miles:{stat.mean(area_water):8,.4f}")

print()

area_total = cities['area_total_km2']
print(f"Average total area in kms:{stat.mean(area_total):8,.4f}")
area_land = cities['area_land_km2']
print(f"Average land area in kms:{stat.mean(area_land):8,.4f}")
area_water = cities['area_water_km2']
print(f"Average water area in kms:{stat.mean(area_water):8,.4f}")

print()
print("Cities between latitude of 36 and 38 and longitude of -120 and -116")
count = 0
for city, lat, long in zip(cities['city'], cities['latd'], cities['longd']):
    if 36 < lat < 38 and -120 < long < -116:
        print(city, " :", lat, ",", long)
        count += 1
print("Total no of cities within the latitude and longitude range is %s" % (str(count)))

print()
population = cities['population_total']
q1 = np.percentile(population, 25)
q3 = np.percentile(population, 75)
print(f"First quartile:{q1}")
print(f"Third quartile: {q3}")
iqr = q3-q1
print(f"Inter quartile range: {iqr}")
print()
print("Cities that fall in iqr range:")
count = 0
for city, population in zip(cities['city'], (cities['population_total'])):
    if q1 < population < q3:
        print(city, ",", population)
        count += 1
print("Total no of cities within inter quartile range is %s" % (str(count)))
