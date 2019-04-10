"""__doc__"""

# imports
import csv
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

WINNERS = []
LOSERS = []
MVPS = []
COACHES_WON = []
COACHES_LOST = []
HOST_CITIES = []

# import csv and populate a dictionary
with open('super_bowls.csv') as f:
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
with open('teams.csv') as f:
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
    for player_or_team, win_or_loss_total in sorted(category.items(),
                                                    key=lambda x: x[1],
                                                    reverse=True):
        print(player_or_team, win_or_loss_total)
    print(RTN())


def score_math(final_score):
    """ run calculations on score """
    for sb_number, total_or_diff in sorted(final_score.items(),
                                           key=lambda x: x[1], reverse=True):
        print(f"Super Bowl {sb_number}: {total_or_diff}")
    print(RTN())


# loop through dictionary and organize contents
for k, v in SUPER_BOWLS.items():
    RESULTS[v[0]] = v[3], v[4], v[5], v[6]
    team_appearances = (v[3], v[5])
    WINNERS.append(v[3])
    LOSERS.append(v[5])
    APPEARED = WINNERS + LOSERS
    MVPS.append(v[7])
    COACHES_WON.append(v[8])
    COACHES_LOST.append(v[9])
    spread = int(v[4]) - int(v[6])
    FINAL_SCORE_MARGIN[v[0]] = spread
    combined_score = int(v[4]) + int(v[6])
    POINT_TOTAL[v[0]] = combined_score
    HOST_CITIES.append(v[2])

print(RTN())

header("results")
for game, result in RESULTS.items():
    print(f"Super Bowl {game}: {result[0]}, {result[1]}, {result[2]}, "\
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
UPSETS = {v[0]: [v[3], float(v[11])]
          for k, v in SUPER_BOWLS.items()
          if v[10] != "Pick 'em"
          and v[3] != v[10]}

for team, line in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    print(f"Super Bowl {team}: {line[0]}, {line[1]}")

print(RTN())

header("host cities")
count(HOST_CITIES, HOST_CITIES_TOTALS)
print_totals(HOST_CITIES_TOTALS)

print(RTN())
