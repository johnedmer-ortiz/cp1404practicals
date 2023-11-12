"""
CP1404 - prac_08 - dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    def __init__(self, **kwargs):
        """Initialises a list of names"""
        super().__init__(**kwargs)
        self.names = ["Michael", "Mia", "Amelia", "Ethan", "Alexander"]

    def build(self):
        """Dynamically builds label widgets base on name list"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries.add_widget(temp_label)
        return self.root


DynamicLabels().run()
