from kivy.config import Config
Config.read('kivy.config.ini')

from kivy.app import App
from includes.main import Password
from kivy.core.clipboard import Clipboard
from kivy.uix.gridlayout import GridLayout

class PgenGridLayout(GridLayout):
    clipboard = Clipboard

    def generate(self, opts={}):
        return Password().generate(opts)

class PgenApp(App):
    icon = 'icons/lock.png'

    def build(self):
        return PgenGridLayout()

if __name__== '__main__':
    PgenApp().run()