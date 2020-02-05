""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: '\n'

TEAMS = {}
CURRENT_TEAMS = {}

with open('csvs/current_teams.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        CURRENT_TEAMS[row.nickname] = row.city

with open('csvs/legacy_teams.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        team = row.nickname
        city = row.cities
        if ', ' in city:
            former_cities = city.split(', ')
            TEAMS[team] = former_cities
        else:
            TEAMS[team] = [city]

print(RTN())

print('current teams')
for nickname, city in sorted(CURRENT_TEAMS.items(), \
                             key=lambda x: x[1]):
    print(city, nickname)

print(RTN())

print('legacy teams')
for nickname, cities in sorted(TEAMS.items(), key=lambda x: x[1]):
    i = 0
    if len(city) > 1:
        for former_city in cities:
            print(cities[i], nickname)
            i += 1
    else:
        print(city[0], nickname)

print(RTN())

FRANCHISES = set(CURRENT_TEAMS.keys()).intersection(TEAMS.keys())

print('current teams who were once in other cities')
for franchise in sorted(FRANCHISES):
    print(franchise)

print(RTN())
