"""
CP1404 - prac_08 - miles to kilometres converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONV_FACTOR = 1.6


class DistanceConverter(App):
    output_distance = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        self.output_distance = f"{float(self.root.ids.miles_input.text) * CONV_FACTOR:.2f}"

    def handle_increment(self, increment):
        if increment == 1:
            self.root.ids.miles_input.text = f"{float(self.root.ids.miles_input.text) + 1}"
        else:
            self.root.ids.miles_input.text = f"{float(self.root.ids.miles_input.text) - 1}"


DistanceConverter().run()
