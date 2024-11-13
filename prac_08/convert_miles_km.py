from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
MILES_TO_KM = 1.60934

class ConvertMilesApp(App):
    """ConvertMilesApp is a kivy app for convert miles to kilograms"""
    km_result = StringProperty()

    def build(self):
        """Build the app from the kv file"""

        # default window size (learn from Square Number App)
        Window.size = (400, 250)
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file("convert_miles_km.kv")

        # default display message
        self.km_result = "54.71756"
        return self.root

    def get_valid_miles(self):
        """Get input miles from kv file, do error check, return float message"""
        try:
            miles_value = float(self.root.ids.input_number.text)
            return miles_value
        except ValueError:
            return 0

    def handle_calculate(self):
        """Handle calculation (call by button press), output result to output label"""
        try:
            output_result = self.get_valid_miles() * MILES_TO_KM
            self.root.ids.km_result.text = str(output_result)
        except ValueError:

            # error check, if input have value error, result equal to 0
            self.km_result = "0.0"

    def handle_increment(self, change):
        """Handle increment (+1 or -1) (call by button press), then update input label and calculate result"""
        input_result = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(input_result)
        self.handle_calculate()

ConvertMilesApp().run()
