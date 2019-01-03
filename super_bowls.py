"""__doc__"""

# move functions to another file

# imports
import csv
import operator
from collections import namedtuple

# define lambda and functions
RTN = lambda: "\n"

def header(title):
    """ print header """
    print title.upper()

def tally(sb_mvp, sb_mvps, player_selected):
    """ compute total in a given category """
    i = 0
    for sb_mvp in sb_mvps:
        if sb_mvp == player_selected:
            i = i + 1
    return i

def win_totals(winner, lst, winner_count, mvp, mvps, mvps_dict):
    """ calculate win totals """
    for winner in sorted(lst):
        winner_count = tally(mvp, mvps, winner)
        mvps_dict[winner] = winner_count

SUPER_BOWLS = {}

with open('super_bowls.csv') as f:
    F_CSV = csv.reader(f)
    HEADINGS = next(F_CSV)
    ROW = namedtuple('Row', HEADINGS)
    for r in F_CSV:
        row = ROW(*r)
        SUPER_BOWLS[row.date] = [
            row.superbowl, row.site, row.winner, row.winnerscore, row.loser, row.loserscore,
            row.mvp, row.winningcoach, row.losingcoach
            ]

# move list of teams to another file

# create list to be populated
CURRENT_NFL_TEAMS = []

# populate list of current teams
with open('teams.csv') as f:
    F_CSV = csv.DictReader(f)
    for row in F_CSV:
        team = row['team']
        CURRENT_NFL_TEAMS.append(team)

# create lists to be populated later
MVPS = []
WINNERS = []
LOSERS = []
YET_TO_WIN = []
WINNING_COACHES = []
LOSING_COACHES = []
SITES = []
WINNNERS_SCORES = []
LOSERS_SCORES = []
TEAMS_WON_AND_LOST = []
COACHES_WON_AND_LOST = []

# create dictionaries to be populated later
MVPS_DICT = {}
CHAMPIONS = {}
WINNING_COACHES_DICT = {}
LOSERS_DICT = {}
LOSING_COACHES_DICT = {}
SITES_DICT = {}
TOTAL_SCORE_DICT = {}

# sort dictionary
SORTED_DICT = sorted(SUPER_BOWLS.items(), key=operator.itemgetter(0), reverse=True)

# populate list
for k, v in SORTED_DICT:
    super_bowl_name = v[0]
    # super_bowl_names.append(super_bowl_name)
    SITE = v[1]
    SITES.append(SITE)
    MVP = v[6]
    MVPS.append(MVP)
    WINNER = v[2]
    WINNERS.append(WINNER)
    LOSER = v[4]
    LOSERS.append(LOSER)
    WINNING_COACH = v[7]
    WINNING_COACHES.append(WINNING_COACH)
    LOSING_COACH = v[8]
    LOSING_COACHES.append(LOSING_COACH)
    WINNER_SCORE = v[3]
    LOSER_SCORE = v[5]
    TOTAL_SCORE = int(WINNER_SCORE) + int(LOSER_SCORE)

# convert lists to a sets
UNIQUE_MVPS = set(MVPS)
UNIQUE_WINNERS = set(WINNERS)
UNIQUE_WINNING_COACHES = set(WINNING_COACHES)
UNIQUE_LOSING_COACHES_TEAMS = set(LOSERS)
UNIQUE_LOSING_COACHES = set(LOSING_COACHES)
UNIQUE_SITES = set(SITES)

print RTN()

# populate a dictionary with player and MVP win total as the keys and values
win_totals('player', UNIQUE_MVPS, 'MVP_count', MVP, MVPS, MVPS_DICT)

# results
header("results")
for k, v in SORTED_DICT:
    print "%s: %s %s %s %s" % (v[0], v[2], v[3], v[4], v[5])

print RTN()

# print MVPs
header("MVPs sorted alphabetically")
for PLAYER, COUNT in sorted(MVPS_DICT.items()):
    print("%s: %s") % (PLAYER, COUNT)

print RTN()

# print MVPs sorted by numbers of MVP trophies won
header("MVPs sorted by number of MVP trophies won")
for player, count in sorted(MVPS_DICT.iteritems(),
                            key=lambda (player, count): (count, player), reverse=True):
    print("%s: %s") % (player, count)

print RTN()

# populate dictionary with teams and super bowl win total as keys and values
win_totals('champ', UNIQUE_WINNERS, 'WINNER_count', WINNER, WINNERS, CHAMPIONS)

# print teams sorted by number of times they've won the super bowl
header("CHAMPIONS")
for champ, WINNER_count in sorted(CHAMPIONS.iteritems(), key=lambda
        (champ, WINNER_count): (WINNER_count, champ), reverse=True):
    print("%s: %s") % (champ, WINNER_count)

print RTN()

win_totals('LOSING_TEAM', UNIQUE_LOSING_COACHES_TEAMS, 'LOSING_TEAM_COUNT', LOSER,
           LOSERS, LOSERS_DICT)

# print("losing teams".upper())
header("losing teams")
for LOSING_TEAM, LOSING_TEAM_COUNT in sorted(LOSERS_DICT.iteritems(),
                                             key=lambda (LOSING_TEAM, LOSING_TEAM_COUNT):
                                             (LOSING_TEAM_COUNT, LOSING_TEAM), reverse=True):
    print "%s: %s" % (LOSING_TEAM, LOSING_TEAM_COUNT)

print RTN()

win_totals('coach', UNIQUE_WINNING_COACHES, 'winning_coach_count', WINNING_COACH, WINNING_COACHES,
           WINNING_COACHES_DICT)

# print("coaches with most super bowl wins".upper())
header("coaches with most super bowl wins")
for WINNING_COACH, WINNING_COACH_COUNT in sorted(WINNING_COACHES_DICT.iteritems(), key=lambda
        (winning_coach, winning_coach_count): (winning_coach_count, winning_coach), reverse=True):
    print("%s: %s") % (WINNING_COACH, WINNING_COACH_COUNT)

print RTN()

win_totals(
    'coach', UNIQUE_LOSING_COACHES, 'losing_coach_count', LOSING_COACH,
    LOSING_COACHES, LOSING_COACHES_DICT
    )

# print losing coaches in descending order of losses
header("coaches with most super bowl losses")
for LOSING_COACH, losing_coach_count in sorted(LOSING_COACHES_DICT.iteritems(), key=lambda
        (LOSING_COACH, losing_coach_count): (losing_coach_count, LOSING_COACH), reverse=True):
    print("%s: %s") % (LOSING_COACH, losing_coach_count)

print RTN()

# print list of coaches who have won and lost the game
header("coaches who have won and lost the super bowl")
for coach in UNIQUE_WINNING_COACHES:
    if coach in UNIQUE_LOSING_COACHES:
        print coach
        COACHES_WON_AND_LOST.append(coach)
    else:
        pass

QTY_COACHES_WON_AND_LOST = len(COACHES_WON_AND_LOST)

print RTN()

# print teams yet to win the super bowl
header("teams yet to win the super bowl")
YET_TO_WIN = set(CURRENT_NFL_TEAMS) - set(WINNERS)
for team in sorted(YET_TO_WIN):
    print team

print RTN()

# print host site in descending order ranked by number of times each
# site has hosted the game
header("host sites")
win_totals('SITE', UNIQUE_SITES, 'site_count', SITE, SITES, SITES_DICT)

for site, site_count in sorted(SITES_DICT.iteritems(), key=lambda (site, site_count):
                               (site_count, site), reverse=True):
    print "%s: %s" % (site, site_count)

print RTN()

for k, v in sorted(SUPER_BOWLS.items()):
    TOTAL_SCORE = int(v[3]) + int(v[5])
    TOTAL_SCORE_DICT[v[0]] = TOTAL_SCORE

# print total scores in descending order
header("total scores descending")
for k, v in sorted(TOTAL_SCORE_DICT.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    print "%s: %s" % (k, v)

print RTN()

# print total scores in ascending order
header("total scores ascending")
for k, v in sorted(TOTAL_SCORE_DICT.iteritems(), key=lambda (k, v): (v, k)):
    print "%s: %s" % (k, v)

print RTN()
