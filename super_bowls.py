"""__doc__"""

# imports
import csv
import operator
from collections import namedtuple

# define lambda and functions
RTN = lambda: "\n"

SUPER_BOWLS = {}
RESULTS = {}
UPSETS = {}
POINT_TOTAL = {}
FINAL_SCORE_MARGIN = {}
MVPS_TOTALS = {}
TEAM_APPEARANCES = {}
TEAM_LOSS_TOTALS = {}
TEAM_WIN_TOTALS = {}
COACH_LOSS_TOTALS = {}
COACH_WIN_TOTALS = {}
HOST_CITIES_TOTALS = {}
SITES_TOTALS = {}

WINNERS = []
LOSERS = []
MVPS = []
COACHES_WON = []
COACHES_LOST = []
HOST_CITIES = []
SITES = []

# import csv and populate a dictionary
with open('csvs/super_bowls.csv') as f:
    F_CSV = csv.reader(f)
    HEADINGS = next(F_CSV)
    ROW = namedtuple('Row', HEADINGS)
    for r in F_CSV:
        row = ROW(*r)
        SUPER_BOWLS[row.date] = [
            row.superbowl, row.site, row.city, row.winner, row.winnerscore,
            row.loser, row.loserscore, row.mvp, row.winningcoach,
            row.losingcoach, row.favorite, row.line,
            ]

# populate list of current teams
with open('csvs/teams.csv') as f:
    F_CSV = csv.DictReader(f)
    for row in F_CSV:
        CURRENT_TEAMS = [row['team'] for row in F_CSV]

def header(title):
    """ print header """
    print(title.upper())


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


def score_math(final_score):
    """ run calculations on score """
    for sb_number, total_or_diff in sorted(final_score.items(),
                                           key=lambda x: x[1], reverse=True):
        print(f"Super Bowl {sb_number}: {total_or_diff}")
    print(RTN())


# loop through dictionary and organize contents
for sb, sb_attribute in SUPER_BOWLS.items():
    RESULTS[sb_attribute[0]] = sb_attribute[3], sb_attribute[4], \
                               sb_attribute[5], sb_attribute[6]
    team_appearances = (sb_attribute[3], sb_attribute[5])
    WINNERS.append(sb_attribute[3])
    LOSERS.append(sb_attribute[5])
    APPEARED = WINNERS + LOSERS
    MVPS.append(sb_attribute[7])
    COACHES_WON.append(sb_attribute[8])
    COACHES_LOST.append(sb_attribute[9])
    spread = int(sb_attribute[4]) - int(sb_attribute[6])
    FINAL_SCORE_MARGIN[sb_attribute[0]] = spread
    combined_score = int(sb_attribute[4]) + int(sb_attribute[6])
    POINT_TOTAL[sb_attribute[0]] = combined_score
    HOST_CITIES.append(sb_attribute[2])
    SITES.append(sb_attribute[1])

print(RTN())

header("results")
for game, result in RESULTS.items():
    print(f"Super Bowl {game}: {result[0]} {result[1]}, {result[2]} "\
          f"{result[3]}")

print(RTN())

header("appearances")
count(APPEARED, TEAM_APPEARANCES)
print_totals(TEAM_APPEARANCES)

header("teams yet to appear")
YET_TO_APPEAR = set(CURRENT_TEAMS) - set(APPEARED)
for team in sorted(YET_TO_APPEAR):
    print(team)

print(RTN())

header("teams yet to win")
YET_TO_WIN = set(CURRENT_TEAMS) - set(WINNERS)
for team in sorted(YET_TO_WIN):
    print(team)

print(RTN())

header("team wins")
count(WINNERS, TEAM_WIN_TOTALS)
print_totals(TEAM_WIN_TOTALS)

header("team losses")
count(LOSERS, TEAM_LOSS_TOTALS)
print_totals(TEAM_LOSS_TOTALS)

header("mvps")
count(MVPS, MVPS_TOTALS)
print_totals(MVPS_TOTALS)

header("winning coaches")
count(COACHES_WON, COACH_WIN_TOTALS)
print_totals(COACH_WIN_TOTALS)

header("losing coaches")
count(COACHES_LOST, COACH_LOSS_TOTALS)
print_totals(COACH_LOSS_TOTALS)

header("coaches who've won and lost")
COACHES_WON_AND_LOST = set(COACHES_WON) & set(COACHES_LOST)
for coach in sorted(COACHES_WON_AND_LOST):
    print(coach)

print(RTN())

header("total score")
score_math(POINT_TOTAL)

header("final score margin")
score_math(FINAL_SCORE_MARGIN)

header("upsets")
UPSETS = {sb_attribute[0]: [sb_attribute[3], float(sb_attribute[11])]
          for sb, sb_attribute in SUPER_BOWLS.items()
          if sb_attribute[10] != "Pick 'em"
          and sb_attribute[3] != sb_attribute[10]}

for sb, sb_attribute in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    print(f"Super Bowl {sb}: {sb_attribute[0]}, +{sb_attribute[1] * -1}")

print(RTN())

header("sites")
count(SITES, SITES_TOTALS)
print_totals(SITES_TOTALS)

header("host cities")
count(HOST_CITIES, HOST_CITIES_TOTALS)
print_totals(HOST_CITIES_TOTALS)
