"""
CP1404 - prac_10 - wiki
"""

import wikipedia


def main():
    query = None
    while query != "":
        query = input("Enter search string: ")
        suggestion = wikipedia.suggest(query)
        print(wikipedia.summary(suggestion))

main()
