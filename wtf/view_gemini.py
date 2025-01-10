
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class LevelButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.round = True
        self.next_level = None

     
    def on_press(self):
        
        if self.next_level:
            #Fazer um teste para não duplicar o botão no grid caso ele já exista.
            self.parent.add_widget(self.next_level)

class LevelGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 10


class TraducaoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        root = LevelGrid()
        start_button = LevelButton(text="Start")
        root.add_widget(start_button)
        TraducaoApp.create_level_tree(start_button)

        # Parte 1: Seleção de idioma
        top_section = BoxLayout(size_hint_y=None, height=100, orientation='horizontal')
        # ... Adicione seus widgets aqui ...
        home_button = Button(text="Bandeira", size_hint_x=None, width=100)
        top_section.add_widget(home_button)

        # Parte 2: Opções e subopções
        options_section = ScrollView()
        #options_container = BoxLayout(orientation='vertical', width=100)

        # ... Adicione seus botões aqui ...
            # Dentro da parte 2:
        """
        for i in range(2):  # Exemplo de 10 opções principais
            main_button = Button(text=f"Opção {i}", size_hint_y=None, height=50)
            sub_options = BoxLayout(orientation='horizontal', height=50)
            for j in range(3):  # Exemplo de 5 subopções
                sub_button = Button(text=f"Subopção {j}", size_hint_x=None, width=50)
                sub_options.add_widget(sub_button)
            options_container.add_widget(main_button)
            options_container.add_widget(sub_options)
        """
        options_section.add_widget(root)

        # Parte 3: Botões de ação
        bottom_section = BoxLayout(size_hint_y=None, height=100)
        # ... Adicione seus botões aqui ...
        home_button = Button(text="Home", size_hint_x=None, width=100)
        bottom_section.add_widget(home_button)

        layout.add_widget(top_section)
        layout.add_widget(options_section)
        layout.add_widget(bottom_section)

        return layout

    def create_level_tree(button, depth=0):
        if depth == 2:  # Limita a profundidade da árvore (ajuste conforme necessário)
            return

        for i in range(3):  # Cria 3 botões filhos
            new_button = LevelButton(text=f"Level {depth+1}-{i}")
            button.next_level = new_button
            #button.parent.add_widget(new_button, index=button.parent.children.index(button)+1)
           
            TraducaoApp.create_level_tree(new_button, depth+1)
        
    



#Primeira pergunta 
app_traducao = TraducaoApp()
if __name__ == '__main__':
    app_traducao.run()
