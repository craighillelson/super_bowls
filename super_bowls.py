"""__doc__"""

# imports
from collections import namedtuple
import csv
import operator
import functions

# dictionaries
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
MATCH_UPS_DCT = {}

# lists
YET_TO_APPEAR = []
YET_TO_WIN = []
WINNERS = []
LOSERS = []
MATCH_UPS = []
MVPS = []
COACHES_WON = []
COACHES_LOST = []
HOST_CITIES = []
SITES = []
CURRENT_TEAMS = []
OPPONENTS = []

# import csv and populate a dictionary
with open('csvs/super_bowls.csv') as f:
    F_CSV = csv.reader(f)
    HEADINGS = next(F_CSV)
    ROW = namedtuple('Row', HEADINGS)
    for r in F_CSV:
        row = ROW(*r)
        RESULTS[row.superbowl] = [row.winner, row.winnerscore, row.loser,
                                  row.loserscore]
        match_up = row.winner, row.loser
        MATCH_UPS.append(match_up)
        WINNERS.append(row.winner)
        LOSERS.append(row.loser)
        APPEARED = WINNERS + LOSERS
        MVPS.append(row.mvp)
        COACHES_WON.append(row.winningcoach)
        COACHES_LOST.append(row.losingcoach)
        HOST_CITIES.append(row.city)
        SITES.append(row.site)
        point_differential = int(row.winnerscore) - int(row.loserscore)
        FINAL_SCORE_MARGIN[row.superbowl] = point_differential
        combined_score = int(row.winnerscore) + int(row.loserscore)
        POINT_TOTAL[row.superbowl] = combined_score
        team_appearances = (row.winner, row.loser)
        if row.line != 'Pick \'em' and row.winner != row.favorite:
            UPSETS[row.superbowl] = [row.winner, float(row.line)]
        else:
            pass

print(functions.RTN())

# results
functions.header('results')
for game, result in RESULTS.items():
    print(f'Super Bowl {game}: {result[0]} {result[1]} - '
          f'{result[2]} {result[3]}')
print(functions.RTN())

# appearances
functions.tally_and_print('appearances', APPEARED, TEAM_APPEARANCES)

# match ups
functions.header('most common match ups')
MATCH_UPS_LST = MATCH_UPS
for teams in sorted(MATCH_UPS_LST):
    opposing_teams = teams[0], teams[1]
    opponents = sorted(opposing_teams)
    OPPONENTS.append(opponents)

for opposing_teams in OPPONENTS:
    count = OPPONENTS.count(opposing_teams)
    opponents = opposing_teams[0] + ' vs ' + opposing_teams[1]
    MATCH_UPS_DCT[opponents] = count

for opposing_teams, num_times_faced in sorted(MATCH_UPS_DCT.items(),
                                              key=lambda x: x[1], reverse=True):
    if num_times_faced > 1:
        print(opposing_teams, num_times_faced)
    else:
        pass

print(functions.RTN())

# yet to appear
functions.yet_to_appear_or_win('teams yet to appear', YET_TO_APPEAR, APPEARED)

# yet to win
functions.yet_to_appear_or_win('teams yet to win', YET_TO_WIN, WINNERS)

# winners
functions.tally_and_print('team wins', WINNERS, TEAM_WIN_TOTALS)

# losers
functions.tally_and_print('team losses', LOSERS, TEAM_LOSS_TOTALS)

# mvps
functions.tally_and_print('mvps', MVPS, MVPS_TOTALS)

# players to win multiple mvps
functions.header('players to win multiple mvps')
SORTED_MVP_TOTALS = sorted(MVPS_TOTALS.items(), key=operator.itemgetter(0))
for player, number_of_mvp_trophies in sorted(SORTED_MVP_TOTALS,
                                             key=operator.itemgetter(1),
                                             reverse=True):
    if number_of_mvp_trophies > 1:
        print(player, number_of_mvp_trophies)
    else:
        pass
print(functions.RTN())

# winning coaches
functions.tally_and_print('winning coaches', COACHES_WON, COACH_WIN_TOTALS)

# losing coaches
functions.tally_and_print('losing coaches', COACHES_LOST, COACH_LOSS_TOTALS)

# coaches who've won and lost
functions.header('coaches who\'ve won and lost')
COACHES_WON_AND_LOST = set(COACHES_WON) & set(COACHES_LOST)
for coach in sorted(COACHES_WON_AND_LOST):
    print(coach)
print(functions.RTN())

# total score
functions.score_math('total score', POINT_TOTAL)

# final score margin
functions.score_math('final score margin', FINAL_SCORE_MARGIN)

# upsets
functions.header('upsets')
for super_bowl, team_spread in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    print(f'Super Bowl {super_bowl}: {team_spread[0]} +{team_spread[1] * -1}')

print(functions.RTN())

# sites
functions.tally_and_print('sites', SITES, SITES_TOTALS)

# host cities
functions.tally_and_print('host cities', HOST_CITIES, HOST_CITIES_TOTALS)
