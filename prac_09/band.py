"""
CP1404 - prac_09 band
"""


class Band:
    """Represents a music band"""

    def __init__(self, band_name):
        """Initialises band name and empty musicians list"""
        self.band_name = band_name
        self.musicians = []

    def add(self, musician):
        """Adds a musician"""
        self.musicians.append(musician)

    def __str__(self):
        """Returns band details as a string"""
        band = []
        for musician in self.musicians:
            band.append(f"{musician}")
        return f"{self.band_name} ({','.join(band)})"

    def play(self):
        """Calls play() method for each musician object"""
        for musician in self.musicians:
            print(musician.play())
