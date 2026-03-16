from kivy.config import Config
Config.read('kivy.config.ini')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from includes.main import Password

class PgenGridLayout(GridLayout, Password):
	password = Password()

	def generate(self, opts={}):
		return self.password.generate(opts)

class PgenApp(App):
    icon = 'icons/lock.png'

    def build(self):
        return PgenGridLayout()

if __name__== '__main__':
    PgenApp().run()