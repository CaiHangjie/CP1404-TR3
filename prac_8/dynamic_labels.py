from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Cai Hangjie", "Zhang Zhang", "Yi Yi", "Ni Ni", "Lala"]
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add labels dynamically based on the names list."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()