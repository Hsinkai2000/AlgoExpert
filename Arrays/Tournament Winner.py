from collections import defaultdict


def tournamentWinner(competitions, results):
    map = defaultdict(int)  # Initialize a default dictionary to keep scores

    # Iterate through the competitions and results
    for i in range(len(competitions)):
        # Determine the winner index based on the result
        if results[i] == 1:
            winIndex = 0
        else:
            winIndex = 1

        # Update the score of the winning team
        map[competitions[i][winIndex]] += 3

    # Return the team with the maximum score
    return max(map, key=map.get)
