"""
CP1404 - prac_08 - miles to kilometres converter
"""

from kivy.app import App
from kivy.lang import Builder

class DistanceConverter(App):
    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

DistanceConverter().run()