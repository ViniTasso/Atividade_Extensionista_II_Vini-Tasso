
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import Builder
from views.main_screen import main_screen


kv = """
<subitens_view>:
    BoxLayout:
        id:box_body
        orientation: "vertical"

        BoxLayout:
            orientation: "horizontal"
            size_hint: 1, 0.1
            Button:
                text: "Voltar"
                on_press: root.handle_voltar()
        ScreenManager:
            id: scmanager
"""
Builder.load_string(kv)

class subitens_view(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        self.instancia_subitens()

    def instancia_subitens(self):
        #main_screen.data_base
        
        for category in main_screen.data_base:

            sc = Screen(name=category)
        
            box = BoxLayout(orientation="Vertical")
            for iten in self.data_base[category]:
                box.add_widget(Button(text=iten))
            sc.add_widget(box)
            self.ids.scmanager.add_widget(sc)
            

    def handle_voltar(self):
        self.manager.current = "main_view"
