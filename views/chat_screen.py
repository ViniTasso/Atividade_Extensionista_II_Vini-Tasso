
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from src.Chating_IA import Chating_IA

Builder.load_file('views/chat_screen.kv')
class chat_screen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        
    def send_message(self):
        # Obtém o texto do campo de entrada
        message = self.ids.message_input.text
        if message.strip():
            # Adiciona a mensagem enviada ao layout
            self.ids.chat_box.add_widget(
                self.create_message(message, "right")
            )
            chat = Chating_IA()
            texto = chat.unica_pergunta(text=message)
            self.aswer_IA(texto)
            # Limpa o campo de entrada
            self.ids.message_input.text = ""

    def aswer_IA(self, text):
        # Adiciona mensagem no scroow
        self.ids.chat_box.add_widget(
            self.create_message(text, "left")
        )
    def create_message(self, text, alignment):
        from kivy.uix.label import Label
        from kivy.uix.boxlayout import BoxLayout

        # Define o layout do lado certo
        message_box = BoxLayout(
            size_hint_y=None,
            height=50,
            padding=10,
            spacing=10,
            orientation="horizontal",
        )
        if alignment == "right":
            message_box.add_widget(Label())
        message_box.add_widget(Label(
            text=text,
            size_hint_x=None,
            width=200,
            text_size=(200, None),
            valign="middle",
            halign="left" if alignment == "left" else "right",
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=40,
        ))
        if alignment == "left":
            message_box.add_widget(Label())
        return message_box
    
    def handle_back_action(self, button_id):
        self.manager.current = "main_screen"