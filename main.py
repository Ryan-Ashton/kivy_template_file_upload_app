import kivy
kivy.require('2.0.0')

from kivy.core.window import Window
Window.size = (1000, 800)

from kivy.clock import Clock
Clock.max_iteration = 20

from kivy.lang import Builder
from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class InputPage(Screen):
    pass

class OutputPage(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputPage(name='main'))
        sm.add_widget(OutputPage(name='output'))
        return sm
 
file_manager = MainApp()
 
file_manager.run()