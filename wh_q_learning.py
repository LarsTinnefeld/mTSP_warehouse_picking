# This is a digital playground to develop an algorithm that
# finds the best pick path in a warehouse based on Q-Learning

# Importing libraries
import numpy as np

# Defining the environment
# The warehouse environment is represented by a grid 15 x 15 units (225 states)
wh_rows = 15
wh_cols = 15

wh_states = np.zeros((wh_rows, wh_cols))
