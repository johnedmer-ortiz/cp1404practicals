"""
CP1404 - prac_05 - Wimbledon Games
"""


def main():
    """Main function for printing to display"""
    games = create_games_list()
    champions, countries = create_winners_list(games)
    countries = sorted(countries)
    champion_to_win = count_scores(champions, games)
    print("Wimbledon Champions: ")
    for champion, win in champion_to_win.items():
        print(f"{champion} {win}")
    print("")
    print("These 12 countries have won Wimbledon: ")
    for country in countries:
        if country != countries[-1]:
            print(country, end=", ")
        else:
            print(country)


def create_games_list():
    """Parses CSV file and creates a games list"""
    games = []
    with open("wimbledon.csv", encoding="utf-8-sig") as in_file:
        for game in in_file:
            games.append(game.split(","))
        del games[0]
    return games


def create_winners_list(games):
    """Creates a non-repeating lists of winning champions and countries"""
    countries = []
    champions = []
    for game in games:
        if game[2] not in champions:
            champions.append(game[2])
            if game[1] not in countries:
                countries.append(game[1])
    return champions, countries


def count_scores(champions, games):
    """Counts number of wins of champions"""
    win = [0 for champion in range(len(champions))]
    champion_to_win = dict(zip(champions, win))
    for game in games:
        if game[2] in champions:
            champion_to_win[game[2]] += 1
    return champion_to_win


main()
