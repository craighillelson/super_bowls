"""Query Super Bowl results."""

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
APPEARED = set()
WON = set()
YET_TO_APPEAR = []
YET_TO_WIN = []
WINNING_TEAMS = []
LOSING_TEAMS = []
MATCH_UPS = []
MVPS = []
COACHES_WON = []
COACHES_LOST = []
HOST_CITIES = []
SITES = []
OPPONENTS = []

# import csv and populate a dictionary
with open("csvs/super_bowls.csv", "r") as f:
    F_CSV = csv.reader(f)
    HEADINGS = next(F_CSV)
    ROW = namedtuple('Row', HEADINGS)
    for r in F_CSV:
        row = ROW(*r)
        RESULTS[row.superbowl] = [row.winner, row.winnerscore, row.loser,
                                  row.loserscore]
        match_up = row.winner, row.loser
        MATCH_UPS.append(match_up)
        WINNING_TEAMS.append(row.winner)
        LOSING_TEAMS.append(row.loser)
        APPEARED_TEAMS = WINNING_TEAMS + LOSING_TEAMS
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

# results
functions.header('results')
for game, result in RESULTS.items():
    winners = result[0]
    winners_point_total = result[1]
    losers = result[2]
    losers_point_total = result[3]
    print(f'Super Bowl {game}: {winners} {winners_point_total} - '
          f'{losers} {losers_point_total}')

# most appearances by team
functions.tally_and_print('appearances', APPEARED_TEAMS, TEAM_APPEARANCES)

# most common match ups
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

# calculate most consecutive appearances

# teams yet to appear
functions.yet_to_appear_or_win('yet to appear', APPEARED, APPEARED_TEAMS,
                               YET_TO_APPEAR)

# teams yet to win
functions.yet_to_appear_or_win('yet to win', WON, WINNING_TEAMS, YET_TO_WIN)

# winning teams ordered by number of wins
functions.tally_and_print('team wins', WINNING_TEAMS, TEAM_WIN_TOTALS)

# losing teams ordered by number of losses
functions.tally_and_print('team losses', LOSING_TEAMS, TEAM_LOSS_TOTALS)

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

# winning coaches ordered by number of wins
functions.tally_and_print('winning coaches', COACHES_WON, COACH_WIN_TOTALS)

# losing coaches ordered by number of losses
functions.tally_and_print('losing coaches', COACHES_LOST, COACH_LOSS_TOTALS)

# coaches who've won and lost
functions.header('coaches who\'ve won and lost')
COACHES_WON_AND_LOST = set(COACHES_WON) & set(COACHES_LOST)
for coach in sorted(COACHES_WON_AND_LOST):
    print(coach)

# total scores in descending order
functions.score_math('total score', POINT_TOTAL)

# final score margin in descending order
functions.score_math('final score margin', FINAL_SCORE_MARGIN)

# upsets
functions.header('upsets')
for super_bowl, team_line in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    team = team_line[0]
    line = team_line[1] * -1
    BETTING_LINE = '+' + str(line)
    print(f'Super Bowl {super_bowl}: {team} {BETTING_LINE}')

# sites
functions.tally_and_print('sites', SITES, SITES_TOTALS)

# host cities
functions.tally_and_print('host cities', HOST_CITIES, HOST_CITIES_TOTALS)
print('\n')
