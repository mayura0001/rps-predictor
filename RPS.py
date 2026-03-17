# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def defaultPlayer(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess


#This is Mayura Jayasinghe's Implementation for better ML based RPS player

'''

import tensorflow as tf
import numpy as np

print("Loading model...")

'''