import operator

def header(title):
    """ print header """
    print(title.upper())


def count(lst_, dct_):
    """ tally wins or losses """
    for sb_team in lst_:
        dct_[sb_team] = lst_.count(sb_team)


def print_totals(category):
    """ print total wins or losses """
    sorted_totals = sorted(category.items(), key=operator.itemgetter(0))
    for unit, total in sorted(sorted_totals, key=operator.itemgetter(1),
                              reverse=True):
        print(unit, total)


def score_math(final_score):
    """ run calculations on score """
    for sb_number, total_or_diff in sorted(final_score.items(),
                                           key=lambda x: x[1], reverse=True):
        print(f"Super Bowl {sb_number}: {total_or_diff}")


def tally_and_print(category_header, b_, c_, d_):
    """ print header, calculate totals and print them """
    header(category_header)
    count(b_, c_)
    print_totals(d_)
    print("\n")
