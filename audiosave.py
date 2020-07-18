#Test running
import kivy
kivy.require ("1.11.1")
from kivy.app import App
from kivy.uix.button import Button
from plyer import audio
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.lang import Builder
print(audio.file_path)


Builder.load_string("""
<RecordScreen>:
    FloatLayout:
        Button:
            background_color: 0,1,0,1
            text_size: self.size
            halign: 'center'
            valign: 'center'
            text: 'Start'
            pos_hint: {"x":0.1,"y":0.5}
            size_hint: 0.15, 0.15
            on_press:
                root.start()
        
        Button:
            background_color: 1,0,0,1
            text_size: self.size
            halign: 'center'
            valign: 'center'
            text: 'Stop'
            pos_hint: {"x":0.45, "y":0.5}
            size_hint: 0.15, 0.15
            on_press:
                root.stop()
        
        Button:
            background_color: 0,0,1,1
            text_size: self.size
            halign: 'center'
            valign: 'center'
            text: 'Play'
            pos_hint: {"x":0.8, "y":0.5}
            size_hint: 0.15, 0.15
            on_press:
                root.play()


""")

class RecordScreen(Screen):

    def start(self):
        try:
            audio.start()
        except:
            print("Not implemented")
    def stop(self):
        try:
            print(audio.file_path)
            audio.stop()
        except:
            print("Not implemented")

        

    def play(self):
        try:
            audio.play()
        except:
            print("Not implemented")

sm=ScreenManager()
sm.add_widget(RecordScreen(name='record'))
sm.current= 'record'

class Main(App):
    def build(self):
        self.title="911-4-911"

        return sm

if __name__== '__main__':
    app= Main()
    app.run()