"""
Calculates statistics like most wins by a franchise, most wins by a coach, most
mvps by player based on Super Bowl data.
"""

import csv
from collections import Counter
from collections import namedtuple

legacy_franchises = {
    "Indianapolis Colts": "Baltimore Colts",
    "Los Angeles Chargers": "San Diego Chargers",
    "Las Vegas Raiders": ["Los Angeles Raiders", "Oakland Raiders"],
    "Los Angeles Rams": "St. Louis Rams",
    "Washington Football Team": "Washington Redskins",
}


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
                                   losing_team, losing_team_score, favorite,
                                   line]

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
    print("\nsuper bowl results")
    for details in super_bowls.values():
        super_bowl_name = details[0]
        visiting_team = details[3]
        visiting_team_score = int(details[4])
        home_team = details[5]
        home_team_score = int(details[6])
        mvp = details[7]
        favorite = details[10]
        line = details[11]
        print(f"Super Bowl {super_bowl_name}")
        print(f"{visiting_team} {visiting_team_score} vs {home_team} "
              f"{home_team_score}")
        if home_team_score > visiting_team_score:
            print(f"winning team: {home_team}")
            print(f"losing team: {visiting_team}")
            print(f"mvp: {mvp}\n")
            lst1.append(home_team)
            lst2.append(visiting_team)
            dct[super_bowl_name] = [home_team, home_team_score, visiting_team,
                                    visiting_team_score, favorite, line]
        else:
            print(f"winning team: {visiting_team}")
            print(f"losing team: {home_team}")
            print(f"mvp: {mvp}\n")
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


def output_dictionary_sorted_by_values_ascending(header, dct):
    print(header)
    for k, v in sorted(dct.items(), key=lambda x: x[1]):
        print(k, v)


def output_dictionary_sorted_by_values_descending(header, dct):
    print(header)
    for k, v in sorted(dct.items(), key=lambda x: x[1], reverse=True):
        print(k, v)


def output_franchises_that_have_appeared():
    print("\nteams that have appeared")
    for team in sorted(franchises_that_have_appeared):
        print(team)


def output_mvps_and_number_of_wins():
    mvps = build_list_of_mvps()
    mvp_counts = Counter(mvps)
    mvps_counts = mvp_counts.most_common()

    print("\nmvps")
    for mvp in mvps_counts:
        player = mvp[0]
        number_of_wins = mvp[1]
        print(f'{player}, {number_of_wins}')


def output_list(header, lst):
    print(header)
    for i in sorted(lst):
        print(i)


def output_host_cities():
    host_cities = build_list_of_host_cities()
    city_counts = Counter(host_cities)
    cities_counts = city_counts.most_common()

    print("\nmost common host city")
    for city_count in cities_counts:
        city = city_count[0]
        number_of_super_bowls_hosted = city_count[1]
        print(f'{city}, {number_of_super_bowls_hosted}')


def output_most_common_match_ups(lst):
    print("\nmost common match ups")
    for match_ups_count in lst:
        print(*match_ups_count, sep=", ")


def output_teams_that_have_not_won_or_appeared(header, lst):
    print(header)
    for team in sorted(current_teams):
        if team not in franchises_that_have_won and team not in \
        list(legacy_franchises.keys()):
            print(team)


def output_upsets():
    print("\nupsets")
    for super_bowl_name, details in sorted(upsets.items(),
                                           key=lambda x: x[1][5]):
        winning_team = details[0]
        winning_team_score = details[1]
        losing_team = details[2]
        losing_team_score = details[3]
        line = details[5]
        print(f"Super Bowl {super_bowl_name}"),
        print(winning_team, winning_team_score, losing_team, losing_team_score)
        print(f"line: {line}\n")


def output_wins_or_losses_by_coach(header, lst):
    print(header)
    for coach_results in lst:
        coach = coach_results[0]
        result = coach_results[1]
        print(coach, result)


super_bowls = open_csv_and_populate_dct()

winning_teams, losing_teams, winning_teams_favorites_and_lines = \
build_lists_and_dictionary_of_winning_and_losing_teams()

franchises_that_have_won = build_list_of_unique_values(winning_teams)
output_list("franchises that have won", franchises_that_have_won)

franchises_that_have_lost = build_list_of_unique_values(losing_teams)
output_list("\nfranchises that have lost", franchises_that_have_lost)

all_appearances = build_list_of_won_and_lost(franchises_that_have_won,
                                             franchises_that_have_lost)
franchises_that_have_appeared = build_list_of_unique_values(all_appearances)
output_list("\nfranchises that have appeared", franchises_that_have_appeared)

franchises_that_have_won_and_lost = \
build_list_of_won_and_lost(franchises_that_have_won, franchises_that_have_lost)

output_list("\nfranchises that have both won and lost",
            franchises_that_have_won_and_lost)

winning_teams_number_of_wins = \
count_wins_or_losses(winning_teams)

team_number_of_wins = \
build_dictionary_of_teams_and_wins_or_losses(winning_teams_number_of_wins)
output_dictionary_sorted_by_values_descending(
"\nmost wins by a franchise", team_number_of_wins)

losing_teams_number_of_losses = \
count_wins_or_losses(losing_teams)

team_number_of_losses = \
build_dictionary_of_teams_and_wins_or_losses(losing_teams_number_of_losses)
output_dictionary_sorted_by_values_descending(
"\nmost losses by a franchise", team_number_of_losses)

current_teams = open_csv_and_populate_list()

output_teams_that_have_not_won_or_appeared(
"\ncurrent teams that have not won", franchises_that_have_won)

output_teams_that_have_not_won_or_appeared(
"\ncurrent teams that have not appeared", franchises_that_have_appeared)

combined_scores, score_differentials = \
calculate_combined_scores_and_score_differential_for_each_game()
output_dictionary_sorted_by_values_descending("\ncombined scores descending",
                                              combined_scores)
output_dictionary_sorted_by_values_ascending("\ncombined scores ascending",
                                              combined_scores)
output_dictionary_sorted_by_values_descending("\nscore differential",
                                              score_differentials)

output_host_cities()
output_mvps_and_number_of_wins()

match_ups = build_list_of_match_ups()
match_ups_sorted = build_list_of_match_ups_sorted()
match_ups_count = count_wins_or_losses(match_ups_sorted)
output_most_common_match_ups(match_ups_count)

winning_coaches, losing_coaches = build_lists_of_winning_and_losing_coaches()

coaches_who_have_won = build_list_of_unique_values(winning_coaches)
output_list("\ncoaches who have won", coaches_who_have_won)

coaches_who_have_lost = build_list_of_unique_values(losing_coaches)
output_list("\ncoaches who have lost", coaches_who_have_lost)

coaches_who_have_won_and_lost = \
build_list_of_won_and_lost(coaches_who_have_won, coaches_who_have_lost)
output_list("\ncoaches who have won and lost", coaches_who_have_won_and_lost)

wins_by_coach = count_wins_or_losses(winning_coaches)
output_wins_or_losses_by_coach("\nwins by coach", wins_by_coach)

losses_by_coach = count_wins_or_losses(losing_coaches)
output_wins_or_losses_by_coach("\nlosses by coach", losses_by_coach)

upsets = build_dictionary_of_upsets()
output_upsets()
