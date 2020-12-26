from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from includes.main import Password

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '160')
Config.write()

class PgenGridLayout(GridLayout, Password):
	password = Password()

	def passgen(self, opts={}):
		return self.password.generate(opts)

class PgenApp(App):
    icon = 'icons/lock.png'

    def build(self):
        return PgenGridLayout()
        
if __name__== '__main__':
    PgenApp().run()