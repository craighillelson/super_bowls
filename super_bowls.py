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

YET_TO_APPEAR = []
YET_TO_WIN = []
WINNERS = []
LOSERS = []
MVPS = []
COACHES_WON = []
COACHES_LOST = []
HOST_CITIES = []
SITES = []
CURRENT_TEAMS = []

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

print(functions.RTN())

functions.header("results")
for game, result in RESULTS.items():
    print(f"Super Bowl {game}: {result[0]} {result[1]}, {result[2]} "\
          f"{result[3]}")
print(functions.RTN())

functions.tally_and_print("appearances", APPEARED, TEAM_APPEARANCES)
functions.yet_to_appear_or_win("teams yet to appear", YET_TO_APPEAR, APPEARED)
functions.yet_to_appear_or_win("teams yet to win", YET_TO_WIN, WINNERS)
functions.tally_and_print("team wins", WINNERS, TEAM_WIN_TOTALS)
functions.tally_and_print("team losses", LOSERS, TEAM_LOSS_TOTALS)
functions.tally_and_print("mvps", MVPS, MVPS_TOTALS)
functions.tally_and_print("winning coaches", COACHES_WON, COACH_WIN_TOTALS)
functions.tally_and_print("losing coaches", COACHES_LOST, COACH_LOSS_TOTALS)

functions.header("coaches who've won and lost")
COACHES_WON_AND_LOST = set(COACHES_WON) & set(COACHES_LOST)
for coach in sorted(COACHES_WON_AND_LOST):
    print(coach)
print(functions.RTN())

functions.score_math("total score", POINT_TOTAL)
functions.score_math("final score margin", FINAL_SCORE_MARGIN)

functions.header("upsets")
UPSETS = {
    sb_attribute[0]: [sb_attribute[3], float(sb_attribute[11])]
    for sb, sb_attribute in SUPER_BOWLS.items()
    if sb_attribute[10] != "Pick 'em"
    and sb_attribute[3] != sb_attribute[10]
    }

for sb, sb_attribute in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    print(f"Super Bowl {sb}: {sb_attribute[0]}, +{sb_attribute[1] * -1}")
print(functions.RTN())

functions.tally_and_print("sites", SITES, SITES_TOTALS)
functions.tally_and_print("host cities", HOST_CITIES, HOST_CITIES_TOTALS)
