import os
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

KV ='''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Send Audio"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "send"

            OneLineListItem:
                text: "Know Your Rights"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "rights"

            OneLineListItem:
                text: "Vision"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "vision"

            OneLineListItem:
                text: "About Us"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "about"

Screen:

    MDToolbar:
        
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "App"
        color: 0, 0, 0, 0
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "send"

                MDLabel:
                    text: "Send Audio"
                    halign: "center"

            Screen:
                name: "rights"

                MDLabel:
                    text: "Know Your Rights"
                    halign: "center"

            Screen:
                name: "vision"

                MDLabel:
                    text: "Vision"
                    halign: "center"

            Screen:
                name: "about"

                MDLabel:
                    text: "About Us"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Menu(MDApp):
    def build(self):
        self.theme_cls.primary_palette='LightBlue'
        self.theme_cls.primary_hue = 'A100'
        return Builder.load_string(KV)

Menu().run()
