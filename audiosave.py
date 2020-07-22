#Test running
import kivy
kivy.require ("1.11.1")
from kivy.app import App
from kivy.uix.button import Button
from plyer import audio
from plyer import stt
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
        Button:
            background_color: 0,1,0,1
            text_size: self.size
            halign: 'center'
            valign: 'center'
            text: 'Listen'
            pos_hint: {"x":0.1,"y":0.25}
            size_hint: 0.15, 0.15
            on_press:
                root.listen()
        
        Button:
            background_color: 1,0,0,1
            text_size: self.size
            halign: 'center'
            valign: 'center'
            text: 'End'
            pos_hint: {"x":0.45, "y":0.25}
            size_hint: 0.15, 0.15
            on_press:
                root.end_listen()
        
        Button:
            background_color: 0,0,1,1
            text_size: self.size
            halign: 'center'
            valign: 'center'
            text: 'Results'
            pos_hint: {"x":0.8, "y":0.25}
            size_hint: 0.15, 0.15
            on_press:
                root.see_results()


""")

class RecordScreen(Screen):

    def start(self):
        audio.start()
        """
        try:
            audio.start()
        except:
            print("Not implemented")
        """

    def stop(self):
        print(audio.file_path)
        audio.stop()
        """
        try:
            print(audio.file_path)
            audio.stop()
        except:
            print("Not implemented")
        """


    def play(self):
        #doesn't save?
        audio.play()
        """
        try:
            audio.play()
        except:
            print("Not implemented")
        """
    
    def listen(self):
        #doesn't run long enough. Should run longer
        for i in range(30):
            stt.start()
            assert stt.listening
            print(stt.partial_results)
            if "hello" in stt.partial_results:
                print("YESSSIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")

            """
            try:
                stt.start()
                assert stt.listening
                print(stt.partial_results)
                if "hello" in stt.partial_results:
                    print("YESSSIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
            except:
                print("Not implemented")
            """

    def end_listen(self):
        stt.stop()
        """
        try:
            stt.stop()
        except:
            print("Not implemented")
        """

    def see_results(self):
        print(stt.results)
        if "police" in stt.results:
                print("YESSSIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR: BUT FOR POLICE")
        """
        try:
            print(stt.results)
            if "police" in stt.results:
                print("YESSSIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR: BUT FOR POLICE")
        except:
            print("Not implemented")
        """
        

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