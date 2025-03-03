# simulation specs
NOISE = True # whether or not this tournament has noise
NOISE_LEVEL = 0.1 # percentage noise; only used if NOISE is set to True
ROUNDS = 59 # number of rounds each strategy plays against each other strategy
NOISE_GAMES_TILL_AVG = 50 # number of games to play until averaging (if noise is true)

# scores distribution, assuming symmetry
POINTS_BOTH_RAT = 1             # score for both players if they both rat
POINTS_DIFFERENT_WINNER = 9     # score for for ratting if opponent stays silent
POINTS_DIFFERENT_LOSER = 0      # score for staying silent if opponent rats
POINTS_BOTH_COOPERATE = 5       # score for both players when they cooperate

# run with default functions (always rat, always silent, tit for tat, etc).
# all default functions can be found in defaul_functions.py
INCLUDE_DEFAULTS = True

# whether or not to reload blacklisted functions
# not reloading speeds up simulation.
# however, it will cause problems if functions that are supposed to be blacklisted are not.
# thus, only set this variable to false if you are confident there has been no changes made to the submission sheet
RELOAD_BLACKLIST = True

# the columns of the spreadsheet that correspond to the
# student name, regular strategies, and noise strategies
SHEET_NAME = "IPD Player Strategies"
TAB_NAME = "Form Responses 1"
STUDENT_NAME_COL = 1
REGULAR_STRAT_COL = 2
NOISE_STRAT_COL = 3

DEBUG_MODE = True # Set this to False.
