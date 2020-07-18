"""Functions."""

import csv
import operator
from collections import namedtuple

RTN = lambda: '\n'

CURRENT_TEAMS_LST = []
CURRENT_TEAMS_DCT = {}
TEAMS = {}

with open('csvs/current_teams.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        team = f'{row.city} {row.nickname}'
        CURRENT_TEAMS_LST.append(team)
        CURRENT_TEAMS_DCT[row.nickname] = row.city

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

FRANCHISES = set(CURRENT_TEAMS_DCT.keys()).intersection(TEAMS.keys())


def header(title):
    """Print header."""
    print(title.upper())


def yet_to_appear_or_win(list_headline, appeared_or_won, appeared_or_won_teams,
                         yet_to_appear_or_win):
    """Among current teams, find those who haven't yet appeared in or won \
    the game."""
    header(list_headline)
    appeared_or_won = set(appeared_or_won_teams)
    yet_to_appear_or_win = set(CURRENT_TEAMS_LST) - appeared_or_won
    for team in sorted(yet_to_appear_or_win):
        city_nickname = team.split()
        nickname = city_nickname[-1]
        if nickname not in FRANCHISES:
            print(team)
    print(RTN())


def count(lst_, dct_):
    """Tally wins or losses."""
    for sb_team in lst_:
        dct_[sb_team] = lst_.count(sb_team)


def print_totals(category):
    """Print total wins or losses."""
    sorted_totals = sorted(category.items(), key=operator.itemgetter(0))
    for unit, total in sorted(sorted_totals, key=operator.itemgetter(1),
                              reverse=True):
        print(unit, total)
    print(RTN())


def score_math(total_or_diff_header, final_score):
    """Run calculations on score."""
    header(total_or_diff_header)
    for sb_number, total_or_diff in sorted(final_score.items(),
                                           key=lambda x: x[1], reverse=True):
        print(f"Super Bowl {sb_number}: {total_or_diff}")
    print(RTN())


def tally_and_print(category_header, team, team_tally):
    """Print header, calculate totals, and print results."""
    header(category_header)
    count(team, team_tally)
    print_totals(team_tally)
