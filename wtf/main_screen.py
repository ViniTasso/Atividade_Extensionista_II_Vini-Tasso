
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from src.textToSpeech_openai import textToSpeech_openai as speech
from src.studing import Chating

class TranslationApp(App):

    global data_base 
    data_base = {"perguntas": ["Para as perguntas a seguir, apenas responda yes ou no.",
            "Você estava amamentando o bebê quando ele se engasgou?",
            "Você deu algum alimento para o bebê que não seja liquido?",
            "A criança tem menos de 3 meses? "],
            "Dicas": [
            "É importante que você não amamente a criança quando estiver deitada! Para evitar sufocar o bebê!",
            "Quando deixar a criança no berço, retire os objetos soltos, os cobertores, para evitar sufocar o bebê.",
            "Após amamentar o bebê, aguarde 15 minutos antes de deita-lo na cama."]
        
    }
    def build(self):
        # Layout principal
        root = BoxLayout(orientation="vertical")

        # Seção superior
        top_section = BoxLayout(orientation="horizontal", size_hint=(1, 0.1), padding=10, spacing=10)
        top_section.add_widget(Label(text="Choose Language:", size_hint=(0.4, 1)))

        languages = {"🇺🇸": "en", "🇧🇷": "pt", "🇪🇸": "es"}
        for emoji, lang in languages.items():
            btn = Button(text=emoji, size_hint=(0.3, 1), on_press=lambda instance, lang=lang: self.handle_flag_click(lang))
            top_section.add_widget(btn)

        root.add_widget(top_section)

        # Seção do meio (rolável)
        middle_section = ScrollView(size_hint=(1, 1))
        scroll_layout = BoxLayout(orientation="vertical", size_hint_y=None, padding=10, spacing=20)
        scroll_layout.bind(minimum_height=scroll_layout.setter("height"))

        #scroll_layout = TranslationApp.create_buttom_test(scroll_layout)
        scroll_layout = TranslationApp.create_buttom_database(scroll_layout)

        middle_section.add_widget(scroll_layout)
        root.add_widget(middle_section)

        # Seção inferior
        bottom_section = BoxLayout(orientation="horizontal", size_hint=(1, 0.2), padding=10, spacing=10)
        controls = [("🏠", "home"), ("📖", "book"), ("🔁", "repeat")]
        for icon, action in controls:
            btn = Button(
                text=action,
                size_hint=(1, 1),
                background_color=(1, 1, 1, 1),
                on_press=lambda instance, action=action: self.handle_control_button_click(action),
            )
            bottom_section.add_widget(btn)

        root.add_widget(bottom_section)

        return root
    
    def create_buttom_database(scroll_layout: BoxLayout):
        for data in data_base:
            main_button = Button(
                text=f"Main {data}",
                size_hint_y=None,
                height=60,
                background_color=(0.55, 0.8, 1, 1),
                on_press=lambda instance, main_id=data: TranslationApp.handle_main_button_click(super, data),
            )
            scroll_layout.add_widget(main_button)

            # Sub botões
            sub_layout = BoxLayout(orientation="vertical", size_hint=(1,1), spacing=10, padding=(20, 0))
            for subitem in data_base[data]:
                sub_button = Button(
                    text=f"S{subitem}",
                    size_hint_y=None,
                    height=40,
                    #width=40,
                    size_hint=(1, None),
                    background_color=(1, 0.7, 0.2, 1),
                    on_press=lambda instance, main_id=data, sub_id=subitem.index: TranslationApp.handle_sub_button_click(super, data, subitem),
                )
                sub_layout.add_widget(sub_button)

            scroll_layout.add_widget(sub_layout)
        return scroll_layout

    # Funções de callback para os botões
    def handle_flag_click(self, language):
        print(f"Selected prefered language: {language}")

    def handle_main_button_click(self, main_id):
        print(f"Main button {main_id} clicked")

    def handle_sub_button_click(self, main_id, text):
        print(f"Sub button {main_id}-{text} clicked")
        speech.text_to_speech(text, "pt")

    def handle_control_button_click(self, action):
        print(f"Control button {action} clicked")
        if action == "book":
            chat = Chating()
            resposta = chat.unica_pergunta("Você pode conversar comigo?")
            print("A resposta foi: "+resposta )
    
    """
    # Executa a aplicação
    if __name__ == "__main__":
        TranslationApp().run()
    """