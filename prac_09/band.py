"""
CP1404 - prac_09 band
"""


class Band():

    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        band = []
        for musician in self.musicians:
            band.append(f"{musician}")
        return f"{self.band_name} ({','.join(band)})"

    def play(self):
        for musician in self.musicians:
            print(musician.play())