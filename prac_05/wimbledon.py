def main():
    games = create_games_list()
    champions, countries = create_winners_list(games)
    champion_to_win = count_scores(champions, games)


def create_games_list():
    games = []
    with open("wimbledon.csv", encoding="utf-8-sig") as in_file:
        for game in in_file:
            games.append(game.split(","))
        del games[0]
    return games


def create_winners_list(games):
    countries = []
    champions = []
    for game in games:
        if game[2] not in champions:
            champions.append(game[2])
            if game[1] not in countries:
                countries.append(game[1])
    return champions, countries


def count_scores(champions, games):
    champion_to_win = {}
    win = [0 for champion in range(len(champions))]
    champion_to_win = dict(zip(champions, win))
    for game in games:
        if game[2] in champions:
            champion_to_win[game[2]] += 1
    return champion_to_win


main()
