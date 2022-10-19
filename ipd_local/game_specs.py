# simulation specs
NOISE = False # whether or not this tournament has noise
NOISE_LEVEL = 0.1 # percentage noise; only used if NOISE is set to True
ROUNDS = 80 # number of rounds each strategy plays against each other strategy

# scores distribution, assuming symmetry
POINTS_BOTH_RAT = 1
POINTS_DIFFERENT_WINNER = 10
POINTS_DIFFERENT_LOSER = 0
POINTS_BOTH_COOPERATE = 5

# blacklist?
RELOAD_BLACKLIST = True

# run with default functions or no
INCLUDE_DEFAULTS = True