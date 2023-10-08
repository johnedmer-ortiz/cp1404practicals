games = []
champions = []

with open("wimbledon.csv", encoding="utf-8-sig") as in_file:
    for game in in_file:
        games.append(game.split(","))
    del games[0]

    for game in games:
        if game[2] not in champions:
            champions.append(game[2])

    win = [0 for champion in range(len(champions))]
    champion_to_win= dict(zip(champions, win))
    for game in games:
        if game[2] in champions:
            champion_to_win[game[2]] += 1

