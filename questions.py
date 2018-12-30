import random

# 1 - build a list of answers and associated questions
# 2 - generate a list of random numbers within the range of the number of questions
# 3 - ask the user a question associated with one of the numbers
# 4 - remove that number from the list of random numbers
# 5 - if the user answers correctly, go to te next random number in the list of random numbers and 
# ask the user another question
# if the user answers incorrectly, the game is over
# 6 - calculate the user's score
# 7 - write the score to a database

questions = {
    a: "team_most_wins",
    b: "team_most_losses",
    c: "coach_most_wins", # raw_input("Number of coaches have won and lost. Name them.\n"),
    d: "coach_most_losses", # raw_input("Which Super Bowl saw the most total points scored?\n"),
    e: "coaches_won_lost", # raw_input("Which?\n"),
    f: "highest_score",
    g: "lowest_score".
}
