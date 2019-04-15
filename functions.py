""" __doc__ """

import csv
import operator

RTN = lambda: "\n"

# populate list of current teams
with open('csvs/teams.csv') as f:
    F_CSV = csv.DictReader(f)
    for row in F_CSV:
        CURRENT_TEAMS = [row['team'] for row in F_CSV]

def header(title):
    """ print header """
    print(title.upper())


def yet_to_appear_or_win(list_headline, yet_to, appeared_or_won):
    """ among current teams, find those who haven't yet appeared in or won \
    the game """
    header(list_headline)
    yet_to = set(CURRENT_TEAMS) - set(appeared_or_won)
    for team in sorted(yet_to):
        print(team)
    print(RTN())


def count(lst_, dct_):
    """ tally wins or losses """
    for sb_team in lst_:
        dct_[sb_team] = lst_.count(sb_team)


def print_totals(category):
    """ print total wins or losses """
    sorted_totals = sorted(category.items(), key=operator.itemgetter(0))
    for unit, total in sorted(sorted_totals, key=operator.itemgetter(1),
                              reverse=True):
        print(unit, total)
    print(RTN())


def score_math(total_or_diff_header, final_score):
    """ run calculations on score """
    header(total_or_diff_header)
    for sb_number, total_or_diff in sorted(final_score.items(),
                                           key=lambda x: x[1], reverse=True):
        print(f"Super Bowl {sb_number}: {total_or_diff}")
    print(RTN())


def tally_and_print(category_header, team, team_tally):
    """ print header, calculate totals, and print them """
    header(category_header)
    count(team, team_tally)
    print_totals(team_tally)
