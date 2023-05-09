from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (1, 0, 0, 1)


class DynamicWidget(App):
    def __init__(self, **kwargs):
        """initiate the App object"""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_label.kv')
        self.create_name_widgets()
        return self.root

    def create_name_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicWidget().run()
