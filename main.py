from kivy.app import App
from kivy.uix.button import Button

class UIApp(App):
	def build(self):
		return Button(text="AIS - IQ",color="#00FC00")
UIApp().run()