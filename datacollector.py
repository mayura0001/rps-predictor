import pandas as pd
from RPS import defaultPlayer
from RPS_game import quincy, mrugesh, kris, abbey, random_player


# Game Logic extended to collect data for training the model

#List
p1_plays = [] #Extend line
p2_plays = [] #Extend line

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        p1_plays.append(p1_prev_play) #Extend line
        p2_plays.append(p2_prev_play) #Extend line

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return (win_rate)



#data collection
print("|Entered Data Collection phase|")

Botnames = ["quincy", "mrugesh", "kris", "abbey", "random_player"]
for bot in Botnames:
    play(defaultPlayer, eval(bot), 1000)
    # Create DataFrame
    df = pd.DataFrame({
        "Player1": p1_plays,
        "Player2": p2_plays
    })
    # Save to CSV
    df.to_csv(f"data{bot.capitalize()}.csv", index=False)