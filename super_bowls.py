# move functions to another file

# imports
import csv
import operator
from collections import namedtuple
from collections import OrderedDict

# define lambda and functions
rtn = lambda: '\n'

def header(a):
    print(a.upper())

def tally(a, b, c):
    i = 0
    for a in b:
        if a == c:
            i = i + 1
    return i

def win_totals(a, b, c, d, e, g):
    for a in sorted(b):
        c = tally(d, e, a)
        g[a] = c

super_bowls = {}

with open('super_bowls.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        super_bowls[row.date] = [
            row.superbowl, row.site, row.winner, row.winnerscore,
            row.loser, row.loserscore, row.mvp, row.winningcoach,
            row.losingcoach
            ]

# create list to be populated
current_nfl_teams = []

# populate list of current teams
with open('teams.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        team = row['team']
        current_nfl_teams.append(team)

# create lists to be populated later
mvps = []
winners = []
losers = []
yet_to_win = []
winning_coaches = []
losing_coaches = []
sites = []
winnners_scores = []
losers_scores = []
won_and_lost = []
# super_bowl_names = []

# create dictionaries to be populated later
mvps_dict = {}
champions = {}
winning_coaches_dict = {}
losers_dict = {}
losing_coaches_dict = {}
sites_dict = {}
total_score_dict = {}

# sort dictionary
sorted_dict = sorted(super_bowls.items(), key=operator.itemgetter(0), reverse=True)

# populate list
for k, v in sorted_dict:
    super_bowl_name = v[0]
    # super_bowl_names.append(super_bowl_name)
    site = v[1]
    sites.append(site)
    mvp = v[6]
    mvps.append(mvp)
    winner = v[2]
    winners.append(winner)
    loser = v[4]
    losers.append(loser)
    winning_coach = v[7]
    winning_coaches.append(winning_coach)
    losing_coach = v[8]
    losing_coaches.append(losing_coach)
    winner_score = v[3]
    loser_score = v[5]
    total_score = int(winner_score) + int(loser_score)

# convert list to a set
unique_mvps = set(mvps)
unique_winners = set(winners)
unique_winning_coaches = set(winning_coaches)
unique_losing_teams = set(losers)
unique_losing_coaches = set(losing_coaches)
unique_sites = set(sites)

print(rtn())

# populate a dictionary with player and mvp win total
# as the keys and values
win_totals('player', unique_mvps, 'mvp_count', mvp, mvps, mvps_dict)

# print mvps
header("mvps sorted alphabetically")
for player, count in sorted(mvps_dict.items()):
    print("%s: %s") % (player, count)

print(rtn())

# print mvps sorted by numbers of mvp trophies won
header("mvps sorted by number of mvp trophies won")
for player, count in sorted(mvps_dict.iteritems(), key=lambda (player, count):
    (count, player), reverse=True):
    print("%s: %s") % (player, count)

print(rtn())

# populate dictionary with teams and super bowl win total as keys and values
win_totals('champ', unique_winners, 'winner_count', winner, winners, champions)

# print teams sorted by number of times they've won the super bowl
header("champions")
for champ, winner_count in sorted(champions.iteritems(), key=lambda 
    (champ, winner_count): (winner_count, champ), reverse=True):
    print("%s: %s") % (champ, winner_count)

print(rtn())

win_totals('losing_team', unique_losing_teams, 'losing_team_count', loser, 
    losers, losers_dict)

# print("losing teams".upper())
header("losing teams")
for losing_team, losing_team_count in sorted(losers_dict.iteritems(),
    key=lambda (losing_team, losing_team_count):
    (losing_team_count, losing_team), reverse=True):
    print("%s: %s") % (losing_team, losing_team_count)

print(rtn())

win_totals('coach', unique_winning_coaches, 'winning_coach_count',
    winning_coach, winning_coaches, winning_coaches_dict
    )

# print("coaches with most super bowl wins".upper())
header("coaches with most super bowl wins")
for winning_coach, winning_coach_count in sorted(
    winning_coaches_dict.iteritems(), key=lambda
    (winning_coach, winning_coach_count): (winning_coach_count, winning_coach),
    reverse=True):
    print("%s: %s") % (winning_coach, winning_coach_count)

print(rtn())

win_totals(
    'coach', unique_losing_coaches, 'losing_coach_count', losing_coach, 
    losing_coaches, losing_coaches_dict
    )

# print losing coaches in descending order of losses
header("coaches with most super bowl losses")
for losing_coach, losing_coach_count in sorted(losing_coaches_dict.iteritems(), 
    key=lambda (losing_coach, losing_coach_count): 
    (losing_coach_count, losing_coach), reverse=True):
    print("%s: %s") % (losing_coach, losing_coach_count)

print(rtn())

# print list of coaches who have won and lost the game
header("coaches who have won and lost the super bowl")
for coach in unique_winning_coaches:
    if coach in unique_losing_coaches:
        print(coach)
    else:
        pass

print(rtn())

# print teams yet to win the super bowl
header("teams yet to win the super bowl")
yet_to_win = set(current_nfl_teams) - set(winners)
for team in sorted(yet_to_win):
    print(team)

print(rtn())

# print host site in descending order ranked by number of times each 
# site has hosted the game
header("host sites")
win_totals('site', unique_sites, 'site_count', site, sites, sites_dict)

for site, site_count in sorted(sites_dict.iteritems(), key=lambda 
    (site, site_count): (site_count, site), reverse=True):
    print("%s: %s") % (site, site_count)

print(rtn())

for k, v in sorted(super_bowls.items()):
    total_score = int(v[3]) + int(v[5])
    total_score_dict[v[0]] = total_score

# print total scores in descending order
header("total scores descending")
for k, v in sorted(total_score_dict.iteritems(), key=lambda (k, v): (v, k),
    reverse=True):
    print("%s: %s") % (k, v)

print(rtn())

# print total scores in ascending order
header("total scores ascending")
for k, v in sorted(total_score_dict.iteritems(), key=lambda (k, v): (v, k)):
    print("%s: %s") % (k, v)

print(rtn())