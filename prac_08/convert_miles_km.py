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
        try:  # sets output to 0.0 when calc button is pressed and invalid input is entered
            self.output_distance = f"{float(self.root.ids.miles_input.text) * CONV_FACTOR:.2f}"
        except ValueError:
            self.output_distance = "0.0"

    def handle_increment(self, increment):
        try:  # try-except block to handle increments when input is invalid
            if increment == 1:
                if self.root.ids.miles_input.text == "":  # checks TextInput field if empty
                    self.root.ids.miles_input.text = "1"
                else:
                    self.root.ids.miles_input.text = f"{float(self.root.ids.miles_input.text) + 1}"
            else:
                if self.root.ids.miles_input.text == "":
                    self.root.ids.miles_input.text = "-1"
                else:
                    self.root.ids.miles_input.text = f"{float(self.root.ids.miles_input.text) - 1}"
        except ValueError:
            pass


DistanceConverter().run()
