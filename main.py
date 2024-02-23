"""
Calculates statistics like most wins by a franchise, most wins by a coach, most
mvps by player based on Super Bowl data.
"""

import csv
from collections import Counter
from collections import namedtuple


def open_csv_and_populate_dct():
    dct = {}

    with open("super_bowls.csv") as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        assembled_tuple = namedtuple("assembled_tuple", headings)
        for detail in f_csv:
            row = assembled_tuple(*detail)
            dct[row.date] = row.super_bowl, row.site, row.city, \
                            row.visiting_team, row.visiting_team_score, \
                            row.home_team, row.home_team_score, \
                            row.mvp, row.winningcoach, row.losingcoach, \
                            row.favorite, row.line

    return dct


def build_dct_of_franchises():
    dct = {}

    with open("franchises.csv") as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        assembled_tuple = namedtuple("assembled_tuple", headings)
        for detail in f_csv:
            row = assembled_tuple(*detail)
            dct[row.team] = [row.alternate_names]

    return dct


def build_dictionary_of_teams_and_wins_or_losses(dct2):
    dct1 = {}
    for team, number_of_wins in dct2:
        dct1.setdefault(team, number_of_wins)

    return dct1


def build_dictionary_of_upsets():
    dct = {}
    for super_bowl_name, details in winning_teams_favorites_and_lines.items():
        winning_team = details[0]
        winning_team_score = int(details[1])
        losing_team = details[2]
        losing_team_score = int(details[3])
        favorite = details[4]
        if details[5] == "Pick \'em":
            line = details[5]
        else:
            line = float(details[5])
            if winning_team != favorite and line != "Pick 'em":
                dct[super_bowl_name] = [winning_team, winning_team_score,
                                        losing_team, losing_team_score, 
                                        favorite, line]

    return dct


def build_list_of_host_cities():
    lst = []
    for details in super_bowls.values():
        host_city = details[2]
        lst.append(host_city)

    return lst


def build_list_of_match_ups():
    lst = []
    for details in super_bowls.values():
        teams = details[3], details[5]
        lst.append(sorted(teams))

    return lst


def build_list_of_match_ups_sorted():
    lst = []
    for match_up in match_ups:
        teams = f"{match_up[0]} vs {match_up[1]}"
        lst.append(teams)

    return lst


def build_list_of_mvps():
    lst = []
    for details in super_bowls.values():
        mvp = details[7]
        lst.append(mvp)

    return lst


def build_lists_of_winning_and_losing_coaches():
    lst1 = []
    lst2 = []
    for details in super_bowls.values():
        winning_coach = details[8]
        losing_coach = details[9]
        lst1.append(winning_coach)
        lst2.append(losing_coach)

    return lst1, lst2


def build_list_of_unique_values(lst):
    return list(set(lst))


def build_lists_and_dictionary_of_winning_and_losing_teams():
    lst1 = []
    lst2 = []
    dct = {}
    for details in super_bowls.values():
        super_bowl_name = details[0]
        visiting_team = details[3]
        visiting_team_score = int(details[4])
        home_team = details[5]
        home_team_score = int(details[6])
        mvp = details[7]
        favorite = details[10]
        line = details[11]
        if home_team_score > visiting_team_score:
            lst1.append(home_team)
            lst2.append(visiting_team)
            dct[super_bowl_name] = [home_team, home_team_score, visiting_team,
                                    visiting_team_score, favorite, line]
        else:
            lst1.append(visiting_team)
            lst2.append(home_team)
            dct[super_bowl_name] = [visiting_team, visiting_team_score,
                                    home_team, home_team_score, favorite, line]

    return lst1, lst2, dct


def build_list_of_won_and_lost(lst2, lst3):
    lst1 = []
    for i in lst2:
        if i in lst3:
            lst1.append(i)

    return lst1


def calculate_combined_scores_and_score_differential_for_each_game():
    dct1 = {}
    dct2 = {}
    for details in super_bowls.values():
        super_bowl_name = details[0]
        visiting_team_score = int(details[4])
        home_team_score = int(details[6])
        total_score = visiting_team_score + home_team_score
        if visiting_team_score > home_team_score:
            difference = visiting_team_score - home_team_score
        else:
            difference = home_team_score - visiting_team_score
        dct1[super_bowl_name] = total_score
        dct2[super_bowl_name] = difference

    return dct1, dct2


def count_wins_or_losses(lst2):
    lst1 = Counter(lst2)

    return lst1.most_common()


def open_csv_and_populate_list():
    lst = []

    with open("current_teams.csv") as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        assembled_tuple = namedtuple("assembled_tuple", headings)
        for detail in f_csv:
            row = assembled_tuple(*detail)
            lst.append(row.team)

    return lst


def count_mvps():
    mvps = build_list_of_mvps()
    mvp_counts = Counter(mvps)

    return mvp_counts.most_common()


def count_games_by_host_city():
    host_cities = build_list_of_host_cities()
    city_counts = Counter(host_cities)
    
    return city_counts.most_common()


def build_list_of_elements_in_other_list(lst1, lst2):
    return [i for i in lst1 if i in lst2]


def build_list_of_elements_not_in_other_list(lst1, lst2):
    return [i for i in lst1 if i not in lst2]


super_bowls = open_csv_and_populate_dct()
current_teams = open_csv_and_populate_list()
legacy_franchises = {
    "Indianapolis Colts": ["Baltimore Colts"],
    "Los Angeles Chargers": ["San Diego Chargers"],
    "Las Vegas Raiders": ["Los Angeles Raiders", "Oakland Raiders"],
    "Los Angeles Rams": ["St. Louis Rams"],
    "Washington Commanders": ["Washington Redskins"],
}

print("\nsuper bowl results")
for super_bowl in super_bowls.values():
    super_bowl_name = super_bowl[0]
    visiting_team = super_bowl[3]
    visiting_team_score = int(super_bowl[4])
    home_team = super_bowl[5]
    home_team_score = int(super_bowl[6])
    mvp = super_bowl[7]
    print(f"\n{super_bowl_name}: {visiting_team} {visiting_team_score} - "
          f"{home_team} {home_team_score}")
    print(f"mvp: {mvp}")

winning_teams, losing_teams, winning_teams_favorites_and_lines = \
build_lists_and_dictionary_of_winning_and_losing_teams()

franchises_that_have_won = build_list_of_unique_values(winning_teams)
print("\nfranchises that have won")
for franchise in sorted(franchises_that_have_won):
    print(franchise)

franchises_that_have_lost = build_list_of_unique_values(losing_teams)
print("\nfranchises that have lost")
for franchise in sorted(franchises_that_have_lost):
    print(franchise)

all_appearances = winning_teams + losing_teams
franchises_that_have_appeared = set(all_appearances)
print("\nfranchises that have appeared")
for franchise in sorted(franchises_that_have_appeared):
    print(franchise)

franchises_that_have_won_and_lost = \
build_list_of_won_and_lost(franchises_that_have_won, franchises_that_have_lost)
print("\nfranchises that have both won and lost")
for franchise in sorted(franchises_that_have_won_and_lost):
    print(franchise)

winning_teams_number_of_wins = count_wins_or_losses(winning_teams)
team_number_of_wins = \
build_dictionary_of_teams_and_wins_or_losses(winning_teams_number_of_wins)
print("\nmost wins by a franchise")
for franchise, number_of_wins in sorted(team_number_of_wins.items(), \
                                        key=lambda x: x[1], reverse=True):
    print(franchise, number_of_wins)

losing_teams_number_of_losses = count_wins_or_losses(losing_teams)
team_number_of_losses = \
build_dictionary_of_teams_and_wins_or_losses(losing_teams_number_of_losses)
print("\nmost losses by a franchise")
for franchise, losses in sorted(team_number_of_losses.items(), \
                                key=lambda x: x[1], reverse=True):
    print(franchise, losses)

print("\ncurrent franchises that have not won")
for franchise in sorted(current_teams):
    if franchise not in franchises_that_have_won and franchise not in \
    list(legacy_franchises.keys()):
        print(franchise)

no_appearances = \
    build_list_of_elements_not_in_other_list(current_teams, all_appearances)
legacy_appearances = \
    build_list_of_elements_in_other_list(no_appearances, legacy_franchises)
no_appearances_reconciled = \
    build_list_of_elements_not_in_other_list(no_appearances, legacy_appearances)

print("\ncurrent franchises that have not appeared")
for franchise in sorted(no_appearances_reconciled):
    print(franchise)

combined_scores, score_differentials = \
calculate_combined_scores_and_score_differential_for_each_game()

print("\ncombined scores descending")
for super_bowl, combined_score in sorted(combined_scores.items(), \
                                         key=lambda x: x[1], reverse=True):
    print(super_bowl, combined_score)

print("\ncombined scores ascending")
for super_bowl,combined_score in sorted(combined_scores.items(), \
                                        key=lambda x: x[1]):
    print(super_bowl, combined_score)

print("\nscore differential")
for super_bowl, score_differential in sorted(score_differentials.items(), \
                                             key=lambda x: x[1], reverse=True):
    print(super_bowl, score_differential)

cities_counts = count_games_by_host_city()
print("\nmost common host city")
for city_count in cities_counts:
    city = city_count[0]
    number_of_super_bowls_hosted = city_count[1]
    print(f'{city}, {number_of_super_bowls_hosted}')

mvps = count_mvps()
print("\nmvps")
for mvp in mvps:
    player = mvp[0]
    number_of_wins = mvp[1]
    print(f'{player}, {number_of_wins}')

match_ups = build_list_of_match_ups()
match_ups_sorted = build_list_of_match_ups_sorted()
match_ups_count = count_wins_or_losses(match_ups_sorted)
print("\nmost common match ups")
for match_ups_count in match_ups_count:
    match_up = match_ups_count[0]
    count = match_ups_count[1]
    if count > 1:
        print(match_up, count)

winning_coaches, losing_coaches = build_lists_of_winning_and_losing_coaches()

coaches_who_have_won = build_list_of_unique_values(winning_coaches)
print("\ncoaches who have won")
for coach in sorted(coaches_who_have_won):
    print(coach)

coaches_who_have_lost = build_list_of_unique_values(losing_coaches)
print("\ncoaches who have lost")
for coach in sorted(coaches_who_have_lost):
    print(coach)

coaches_who_have_won_and_lost = \
build_list_of_won_and_lost(coaches_who_have_won, coaches_who_have_lost)
print("\ncoaches who have won and lost")
for coach in sorted(coaches_who_have_won_and_lost):
    print(coach)

wins_by_coach = count_wins_or_losses(winning_coaches)
print("\nwins by coach")
for coach_results in wins_by_coach:
    coach = coach_results[0]
    result = coach_results[1]
    print(coach, result)

losses_by_coach = count_wins_or_losses(losing_coaches)
print("\nlosses by coach")
for coach_results in losses_by_coach:
    coach = coach_results[0]
    result = coach_results[1]
    print(coach, result)

upsets = build_dictionary_of_upsets()
print("\nupsets")
for super_bowl_name, details in sorted(upsets.items(), key=lambda x: x[1][5]):
    winning_team = details[0]
    winning_team_score = details[1]
    losing_team = details[2]
    losing_team_score = details[3]
    line = details[5]
    print(f"Super Bowl {super_bowl_name}"),
    print(winning_team, winning_team_score, losing_team, losing_team_score)
    print(f"line: {line}\n")
