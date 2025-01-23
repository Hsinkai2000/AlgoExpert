from collections import defaultdict


def tournamentWinner(competitions, results):
    map = defaultdict(int)

    for i in range(len(competitions)):
        if results[i] == 1:
            winIndex = 0
        else:
            winIndex = 1

        print(competitions[i][winIndex])
        map[competitions[i][winIndex]] += 3

        print(map)

    return max(map, key=map.get)
