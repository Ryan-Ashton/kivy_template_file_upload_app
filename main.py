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

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

import pandas as pd



class OutputPage(Screen):
    pass




class InputPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=[".csv", ".xlsx"]
        )

    def file_manager_open(self):
        self.file_manager.show(r'C:\Users')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        df = pd.read_excel(path)
        df.to_csv("test_output.csv")

        self.exit_manager()
        toast(path)

        # Once a file has been loaded by a user, go to a new page
        sm.current = "output" 

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = True
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


class WindowManager(ScreenManager):
    pass



sm = WindowManager()


class MainApp(MDApp):

    def build(self):
        screens = [InputPage(name='main'), OutputPage(name='output')]

        for screen in screens:
            sm.add_widget(screen)

        sm.current = "main"

        return sm



if __name__ == "__main__":
    MainApp().run()

