
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
#from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import sp
from kivy.app import App
from wtf.button_sized import Button
from kivy.uix.scrollview import ScrollView
from src.textToSpeech_openai import textToSpeech_openai as speech



Builder.load_file('views/main_screen.kv')

class main_screen(Screen):

    languages = {"🇺🇸": "en", "🇧🇷": "pt", "🇪🇸": "es"}

    data_base = {"Perguntas": ["Para as perguntas a seguir, apenas responda yes ou no.",
            "Você estava amamentando o bebê quando ele se engasgou?",
            "Você deu algum alimento para o bebê que não seja liquido?",
            "A criança tem menos de 3 meses? "],
            "Dicas": [
            "É importante que você não amamente a criança quando estiver deitada! Para evitar sufocar o bebê!",
            "Quando deixar a criança no berço, retire os objetos soltos, os cobertores, para evitar sufocar o bebê.",
            "Após amamentar o bebê, aguarde 15 minutos antes de deita-lo na cama."]}
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
        for key, itens in self.data_base.items():
            self.ids.middle_section.add_widget(self.instancia_botao_categoria(key))
        #self.instanciar_conjunto_categorias()

        #instancia Screens dos SubItens
        for key, itens in self.data_base.items():
            newsc = Screen(name=key)
            box = BoxLayout(orientation="vertical")
            box_top = BoxLayout(orientation="horizontal")
            box_top.add_widget(Button(text="Voltar", on_press=lambda instance: self.handle_button_main_category()))
            box.add_widget(box_top)
            for iten in itens:
                box.add_widget(self.instancia_botao_subcategoria(iten))
            scrol = ScrollView()
            scrol.add_widget(box)
            newsc.add_widget(scrol)
            self.ids.submanager.add_widget(newsc)
        self.ids.submanager.current = "subscreen_1"
    #função geral de organização
    def instanciar_conjunto_categorias(self):
        #instancia todo conjunto de database
        
        for key, itens in self.data_base.items():
            #box pra categoria
            self.box_categoria = BoxLayout(
                orientation="horizontal",
                size_hint=(1,1),
                padding=10, spacing=2
            )
            #box pro botao categoria
            self.box_botao_categoria = BoxLayout(
                orientation="horizontal",
                size_hint=(1,0.3),
                padding=10, spacing=2
            )
            #box pro sub item categoria
            self.box_item_categoria = BoxLayout(
                orientation="vertical",
                size_hint=(1,0.7),
                padding=10, spacing=2
            )
            #registrar os box no IDS para poder ser instanciado em outro lugar do código, como também manipular
            #as configurações em todos os arquivos com o mesmo ids
            self.ids["box_categoria"] = self.box_categoria
            self.ids["box_botao_categoria"] = self.box_categoria
            self.ids["box_item_categoria"] = self.box_categoria

           
            #instanciar o botão categoria
            self.box_botao_categoria.add_widget(self.instancia_botao_categoria(key))
            
            #for iten in itens:
            #    self.box_item_categoria.add_widget(self.instancia_botao_subcategoria(iten))
                
            #organizar estrutura dos box
            self.box_categoria.add_widget(self.box_botao_categoria)
            #self.box_categoria.add_widget(self.box_item_categoria)
            self.ids.middle_section.add_widget(self.box_categoria)
        pass


    #função de execução

    def instancia_botao_categoria(self, text):
        return Button(text=text, size_hint=(1,1), on_press=lambda instance: self.handle_subscreen_switch(text))

    def instancia_botao_subcategoria(self, text):
        return Button(text=text, size_hint=(1,1), on_press=lambda instance, action=text: self.handle_item_action_subcategory(text) )
    
    def cria_itens_subcategoria(self):
        for key, item in self.data_base:
            pass
    # Funções de callback para os botões
    def handle_flag_click(self, language):
        print(f"Selected prefered language: {language}")
        
        if 'middle_section' in self.ids:
            btn = Button(text="en", width="50")
            self.ids.middle_section.add_widget(btn)
            
        else:
            print("Erro: O id 'middle' não foi encontrado.")

    def handle_control_button_click(self, main_id):
        print(f"Main button {main_id} clicked")

    def handle_button_main_category(self):
        #box pro sub item categoria
        self.ids.submanager.current = "subscreen_1"

    def handle_item_action_subcategory(self, text):
        #irá abrir um novo box que tem o botão de play
        #quando clicar ele automaticamente já inicia o play
        #quando o botão muda o desenho para stop, se clicar em stop para a execução e muda o desenho para play
        speech.text_to_speech(text, "pt")
        pass

    def handle_control_button_click(self, main_id):
        self.manager.current = "chat_screen"

    def handle_subscreen_switch(self, name):
        self.ids.submanager.current = name
        pass