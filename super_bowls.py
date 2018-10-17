# imports
import csv
import operator
from collections import namedtuple
from collections import OrderedDict

# define lambda and functions 
rtn = lambda : '\n'

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
		super_bowls[row.date] = [row.superbowl, row.site, row.winner, row.winnerscore, row.loser, row.loserscore, row.mvp, row.winningcoach]

# create list to be populated
current_nfl_teams = []

# populate list of current teams
with open('teams.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		team = row['team']
		current_nfl_teams.append(team)

# create list to be populated later
mvps = []
winners = []
runners_up = []

# create dictionaries to be populated later
mvps_dict = {}
champions = {}

# sort dictionary
sorted_dict = sorted(super_bowls.items(), key=operator.itemgetter(0), reverse=True)

# populate list
for k, v in sorted_dict:
	mvp = v[6]
	mvps.append(mvp)
	winner = v[2]
	winners.append(winner)

# convert list to a set
unique_mvps = set(mvps)
unique_winners = set(winners)

# populate a dictionary with player and mvp win total as the keys and values
win_totals('player', unique_mvps, 'mvp_count', mvp, mvps, mvps_dict)

print(rtn())

# print mvps
print("mvps sorted alphabetically").upper()
for player, count in sorted(mvps_dict.items()):
	print("%s: %s") % (player, count)

print(rtn())

# print mvps sorted by numbers of mvp trophies won
print("mvps sorted by number of mvp trophies won").upper()
for player, count in sorted(mvps_dict.iteritems(), key=lambda (player, count): (count, player), reverse=True):
	print("%s: %s") % (player, count)

# populate dictionary with teams and super bowl win total as keys and values
win_totals('champ', unique_winners, 'winner_count', winner, winners, champions)

print(rtn())

# print teams sorted by number of times they've won the super bowl
print("champions").upper()
for champ, winner_count in sorted(champions.iteritems(), key=lambda (champ, winner_count): (winner_count, champ), reverse=True):
	print("%s: %s") % (champ, winner_count)

print(rtn())

# print teams yet to win the super bowl
print("yet to win the super bowl").upper()
runners_up = set(current_nfl_teams) - set(winners)
for team in sorted(runners_up):
	print(team)

print(rtn())

# add questions
# which team has won the most super bowls?
# who has won the mvp more than anyone else?
# what (insert number) teams have yet to win the super bowl?
# who are the only two players to be voted co-mvps?
# what city has hosted the super bowl more than any other?
# what coach has won the super bowl more than any other?