"""
CP1404 - prac_10 - wiki
"""

import wikipedia


def main():
    query = input("Enter search string: ")
    while query != "":
        try:
            suggestion = wikipedia.suggest(query)
            page = wikipedia.page(suggestion)
            print(f"Title: {page.title}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
        except ValueError:
            print("Wikipedia suggestion returned 'None'. Try a different search query.")
        except wikipedia.DisambiguationError:
            print("Cannot find page. Try again.")
        query = input("Enter search string: ")


main()
