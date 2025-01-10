
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


class TranslationApp(App):
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
        middle_section = ScrollView(size_hint=(1, 0.7))
        scroll_layout = BoxLayout(orientation="vertical", size_hint_y=None, padding=10, spacing=20)
        scroll_layout.bind(minimum_height=scroll_layout.setter("height"))

        for main_id in range(1, 4):
            main_button = Button(
                text=f"Main {main_id}",
                size_hint_y=None,
                height=60,
                background_color=(0.55, 0.8, 1, 1),
                on_press=lambda instance, main_id=main_id: self.handle_main_button_click(main_id),
            )
            scroll_layout.add_widget(main_button)

            # Sub botões
            sub_layout = BoxLayout(orientation="horizontal", spacing=10, padding=(20, 0))
            for sub_id in range(1, 4):
                sub_button = Button(
                    text=f"S{sub_id}",
                    size_hint_y=None,
                    height=40,
                    width=40,
                    size_hint=(None, None),
                    background_color=(1, 0.7, 0.2, 1),
                    on_press=lambda instance, main_id=main_id, sub_id=sub_id: self.handle_sub_button_click(main_id, sub_id),
                )
                sub_layout.add_widget(sub_button)

            scroll_layout.add_widget(sub_layout)

        middle_section.add_widget(scroll_layout)
        root.add_widget(middle_section)

        # Seção inferior
        bottom_section = BoxLayout(orientation="horizontal", size_hint=(1, 0.2), padding=10, spacing=10)
        controls = [("🏠", "home"), ("📖", "book"), ("🔁", "repeat")]
        for icon, action in controls:
            btn = Button(
                text=icon,
                size_hint=(1, 1),
                background_color=(1, 1, 1, 1),
                on_press=lambda instance, action=action: self.handle_control_button_click(action),
            )
            bottom_section.add_widget(btn)

        root.add_widget(bottom_section)

        return root

    # Funções de callback para os botões
    def handle_flag_click(self, language):
        print(f"Selected prefered language: {language}")

    def handle_main_button_click(self, main_id):
        print(f"Main button {main_id} clicked")

    def handle_sub_button_click(self, main_id, sub_id):
        print(f"Sub button {main_id}-{sub_id} clicked")

    def handle_control_button_click(self, action):
        print(f"Control button {action} clicked")


# Executa a aplicação
if __name__ == "__main__":
    TranslationApp().run()
