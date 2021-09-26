from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_list = {"Harry Howard", "Cody Sullivan", "Cheese Bread"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.name_list:
            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)

DynamicWidgetsApp().run()
