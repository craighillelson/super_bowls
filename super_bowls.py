"""__doc__"""

# imports
import csv
from collections import namedtuple


# define lambda and functions
RTN = lambda: "\n"

SUPER_BOWLS = {}
UNIQUE_WINNERS_TOTALS = {}
UNIQUE_LOSERS_TOTALS = {}
UNIQUE_MVPS_TOTALS = {}
UNIQUE_WINNING_COACHES = {}
UNIQUE_LOSING_COACHES = {}
UPSETS = {}

CURRENT_TEAMS = []
WINNERS = []

with open('super_bowls.csv') as f:
    F_CSV = csv.reader(f)
    HEADINGS = next(F_CSV)
    ROW = namedtuple('Row', HEADINGS)
    for r in F_CSV:
        row = ROW(*r)
        SUPER_BOWLS[row.date] = [
            row.superbowl, row.site, row.winner, row.winnerscore, row.loser,
            row.loserscore, row.mvp, row.winningcoach, row.losingcoach,
            row.favorite, row.line
            ]

# populate list of current teams
with open('teams.csv') as f:
    F_CSV = csv.DictReader(f)
    for row in F_CSV:
        CURRENT_TEAMS = [row['team'] for row in F_CSV]

def header(title):
    """ print header """
    print(title.upper())


def count_(lst, count_int):
    """ count number of occurances in a list """
    # change name of function to count_
    lst = []
    lst = [lst.append(item[count_int]) for s_b, item in SUPER_BOWLS.items()]
    return lst


def add_to_dct(a_lst, dct):
    """ add values to dictionary """
    for var in set(a_lst):
        dct[var] = a_lst.count(var)


def print_var_total(dct):
    """ print contents of dictionary sorted by values """
    for k_k, v_v in sorted(dct.items(), key=lambda x: x[1], reverse=True):
        print(k_k, v_v)
    print(RTN())


def print_totals(a_a, b_b, c_c, d_d):
    """ print totals in a given category """
    add_to_dct(a_a, b_b)
    header(c_c)
    print_var_total(d_d)


def print_members(a_a):
    """ print contents of a list """
    for member in a_a:
        print(member)


def calculate(output, calc):
    """ run calculations based on the final score """
    for v_v in SUPER_BOWLS.items():
        s_b = v_v[0]
        output = calc
        print(f"{s_b}: {output}")

# populate a list with the output of a given function
WINNERS_LST = count_("winners", 2)
LOSERS_LST = count_("losers", 4)
MVPS_LST = count_("mvps", 6)
WINNING_COACHES_LST = count_("winning_coaches", 7)
LOSING_COACHES_LST = count_("losing_coaches", 8)

print(RTN())

print_totals(WINNERS_LST, UNIQUE_WINNERS_TOTALS, "teams, wins",
             UNIQUE_WINNERS_TOTALS)
print_totals(LOSERS_LST, UNIQUE_LOSERS_TOTALS, "teams, losses",
             UNIQUE_LOSERS_TOTALS)

# teams that have appeared
header("teams that have won and lost")
W_L = UNIQUE_WINNERS_TOTALS.keys() & UNIQUE_LOSERS_TOTALS.keys()
for team in W_L:
    print(team)

print(RTN())

header("teams that have appeared")
APPEARED = UNIQUE_WINNERS_TOTALS.keys() | UNIQUE_LOSERS_TOTALS.keys()
print_members(APPEARED)

print(RTN())

header("current teams yet to appear")
YET_TO_APPEAR = [team
                 for team in CURRENT_TEAMS
                 if team not in APPEARED]
print_members(YET_TO_APPEAR)

print(RTN())

header("teams that haven't won the game")
WINNERS = [k for k, v in UNIQUE_WINNERS_TOTALS.items()]
HAVE_NOT_WON = [team for team in CURRENT_TEAMS
                if team not in WINNERS]
print_members(HAVE_NOT_WON)

print(RTN())

print_totals(MVPS_LST, UNIQUE_MVPS_TOTALS, "mvps", UNIQUE_MVPS_TOTALS)
print_totals(WINNING_COACHES_LST, UNIQUE_WINNING_COACHES, "coaches, wins",
             UNIQUE_WINNING_COACHES)
print_totals(LOSING_COACHES_LST, UNIQUE_LOSING_COACHES, "coaches, losses",
             UNIQUE_LOSING_COACHES)

# coaches who've won and lost the game
header("coaches who have won and lost the super bowl")
COACHES_W_L = UNIQUE_WINNING_COACHES.keys() & UNIQUE_LOSING_COACHES.keys()
print_members(COACHES_W_L)

print(RTN())

# highest score and lowest score
header("total score")
for k, v in sorted(SUPER_BOWLS.items()):
    sb = v[0]
    total_score = int(v[3]) + int(v[5])
    print(f"{sb}: {total_score}")

print(RTN())

header("final score spreads")
for k, v in SUPER_BOWLS.items():
    sb = v[0]
    spread = int(v[3]) - int(v[5])
    print(f"{sb}: {spread}")

print(RTN())

header("upsets")
UPSETS = {v[0]: [v[2], float(v[10])]
          for k, v in SUPER_BOWLS.items()
          if v[9] != "Pick 'em"
          and v[2] != v[9]}

for k, v in sorted(UPSETS.items(), key=lambda x: x[1][1]):
    print(f"Super Bowl {k}, {v[0]}, {v[1]}")

print(RTN())
