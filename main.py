
import pygame #apenas para evitar erro de compatibilidade com a biblioteca 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


#BIBLIOTECAS PESSOAIS
from wtf.main_screen import TranslationApp
from src.Chating_IA import Chating_IA
from views.main_screen import main_screen
from views.chat_screen import chat_screen

class main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(main_screen(name="main_screen"))
        sm.add_widget(chat_screen(name="chat_screen"))
        return sm
    def handle_flag_click(self, language):
        print(f"Selected prefered language: {language}")
if __name__ == "__main__":
    main().run()
        
    #TranslationApp().run()



#ler o o arquivo /data/profile.csv
#colocar os dados do usuário nas variáveis globais.

#fornecer as opções para o usuário escolher

#conversar com a Dona Gemini
#chamar funções talking

#revisão de coisas estudadas
#chamar flashcard

#aprender palavras em contexto
#chamar função guide