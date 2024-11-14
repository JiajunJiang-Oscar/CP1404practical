from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabels(App):
    """Dynamic Labels is a kivy app for show the names by name list"""

    def __init__(self, **kwargs):
        """Construct name list."""
        super().__init__(**kwargs)
        self.name_list = ["Oscar", "Brain", "James", "Leo"]

    def build(self):
        """Build the Kivy app interface."""
        self.title = "Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_list:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabels().run()
