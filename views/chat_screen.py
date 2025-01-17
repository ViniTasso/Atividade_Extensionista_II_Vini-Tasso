
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from src.Chating_IA import Chating_IA

Builder.load_file('views/chat_screen.kv')
class chat_screen(Screen):
    teste = """
    Explicação do Código:
Gerenciador de Telas (MyScreenManager):

MyScreenManager gerencia as telas e alterna entre elas usando o atributo current.
Nomeando as Telas (name):

Cada tela (FirstScreen e SecondScreen) possui um atributo name. É importante para referenciá-las no ScreenManager.
Botões de Navegação:

O botão em cada tela usa on_press para alterar a tela exibida.
app.root.current é o caminho para o ScreenManager. O valor atribuído a ele deve ser o nome da tela para onde você deseja navegar ("first" ou "second").
Resultado Esperado:
Ao executar o app, a primeira tela será exibida.
Clicar no botão "Ir para a Segunda Tela" muda para a segunda tela.
Na segunda tela, clicar no botão "Voltar para a Primeira Tela" retorna à primeira tela.
Se precisar de ajuda para integrar isso ao seu código atual, me avise! 😊






You said:
Como fazer essa manipulação no código em python?
ChatGPT said:
ChatGPT
Se você deseja manipular as transições entre telas exclusivamente no código Python, sem utilizar KV, aqui está um exemplo completo para implementar o ScreenManager e alternar entre telas ao clicar em botões.


    """

    #chat = Chating_IA()
    def __init__(self, **kw):
        super().__init__(**kw)
        #self.aswer_IA(self.chat.inicia_chat_principal("Frances", "Engasgamento", "A criança está bem, mas ainda precisamos ir ao hospital"))
       
    def send_message(self):
        # Obtém o texto do campo de entrada
        message = self.ids.message_input.text
        if message.strip():
            # Adiciona a mensagem enviada ao layout
            self.ids.chat_box.add_widget(
                self.create_message(message, "right")
            )
            
            #texto = self.chat.iteracao_IA(text=message, idioma="Frances")
            self.aswer_IA(self.teste)
            # Limpa o campo de entrada
            self.ids.message_input.text = ""
        
            dicas = "Dica: This is another teste to see | Esse é mais um teste"#self.chat.possiveis_respostas(texto=texto)
        try:
            self.ids.message_input.hint_text = "Dica: {} | {}..."#.format(dicas["frase"][-1], dicas["traducao"][-1])
        except:
            self.ids.message_input.hint_text = "Digite sua mensagem..."

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
            padding=10,
            spacing=10,
            orientation="horizontal",
            background_color=(0.1, 0.2, 0.5, 1)
        )
        message_box.bind(minimum_height=message_box.setter("height"))

        if alignment == "right":
            message_box.add_widget(Label())
        message_box.add_widget(Label(
            text=text,
            size_hint_x=None,
            width=200,
            #background_color=[0,0,0,0],
            text_size=(200, None),
            valign="middle",
            halign="left" if alignment == "left" else "right",
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=self.get_label_height(text)
        ))
        if alignment == "left":
            message_box.add_widget(Label())
        return message_box
    
    def get_label_height(self, text):
        # Simula o cálculo do tamanho do texto para ajustar a altura do Label
        from kivy.uix.label import Label
        temp_label = Label(text=text, size_hint_y=None,text_size=(200, None))
        temp_label.texture_update()  # Garante que o tamanho do texto foi calculado
        return temp_label.texture_size[1] + 10  # Adiciona margem
    
    def handle_back_action(self, button_id):
        self.manager.current = "main_screen"