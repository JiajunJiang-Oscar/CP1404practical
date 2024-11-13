from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMiles(App):
    def build(self):
        Window.size = (400, 250)
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

ConvertMiles().run()