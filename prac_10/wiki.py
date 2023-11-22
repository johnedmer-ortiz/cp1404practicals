"""
CP1404 - prac_10 - wiki
"""

import wikipedia


def main():
    query = None
    query = input("Enter search string: ")
    while query != "":
        try:
            suggestion = wikipedia.suggest(query)
            print(wikipedia.summary(suggestion))
        except ValueError:
            print("Wikipedia suggestion returned 'None'. Try a different search query.")
        except wikipedia.DisambiguationError:
            print("Cannot find page. Try again.")
        query = input("Enter search string: ")
main()
