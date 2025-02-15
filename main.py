from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from plyer import filechooser

Builder.load_file('style.kv') 

class Style(MDAnchorLayout):
    fmn=filechooser

    def handle_selection(self,selection):
        print(selection)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'
        return Style()

MainApp().run()
