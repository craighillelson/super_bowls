"""__doc__"""

# imports
from collections import namedtuple
import csv
import functions

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

RTN = lambda: "\n"

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

functions.header("results")
for game, result in RESULTS.items():
    print(f"Super Bowl {game}: {result[0]} {result[1]}, {result[2]} "\
          f"{result[3]}")
print(RTN())

functions.tally_and_print("appearances", APPEARED, TEAM_APPEARANCES,
                          TEAM_APPEARANCES)

functions.header("teams yet to appear")
YET_TO_APPEAR = set(CURRENT_TEAMS) - set(APPEARED)
for team in sorted(YET_TO_APPEAR):
    print(team)
print(RTN())

functions.header("teams yet to win")
YET_TO_WIN = set(CURRENT_TEAMS) - set(WINNERS)
for team in sorted(YET_TO_WIN):
    print(team)
print(RTN())

functions.tally_and_print("team wins", WINNERS, TEAM_WIN_TOTALS,
                          TEAM_WIN_TOTALS)

functions.tally_and_print("team losses", LOSERS, TEAM_LOSS_TOTALS,
                          TEAM_LOSS_TOTALS)

functions.tally_and_print("mvps", MVPS, MVPS_TOTALS, MVPS_TOTALS)

functions.tally_and_print("winning coaches", COACHES_WON, COACH_WIN_TOTALS,
                          COACH_WIN_TOTALS)

functions.tally_and_print("losing coaches", COACHES_LOST, COACH_LOSS_TOTALS,
                          COACH_LOSS_TOTALS)

functions.header("coaches who've won and lost")
COACHES_WON_AND_LOST = set(COACHES_WON) & set(COACHES_LOST)
for coach in sorted(COACHES_WON_AND_LOST):
    print(coach)
print(RTN())

functions.header("total score")
functions.score_math(POINT_TOTAL)
print(RTN())

functions.header("final score margin")
functions.score_math(FINAL_SCORE_MARGIN)
print(RTN())

functions.header("upsets")
UPSETS = {sb_attribute[0]: [sb_attribute[3], float(sb_attribute[11])]
          for sb, sb_attribute in SUPER_BOWLS.items()
          if sb_attribute[10] != "Pick 'em"
          and sb_attribute[3] != sb_attribute[10]}

for sb, sb_attribute in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    print(f"Super Bowl {sb}: {sb_attribute[0]}, +{sb_attribute[1] * -1}")
print(RTN())

functions.tally_and_print("sites", SITES, SITES_TOTALS, SITES_TOTALS)
functions.tally_and_print("host cities", HOST_CITIES, HOST_CITIES_TOTALS,
                          HOST_CITIES_TOTALS)
