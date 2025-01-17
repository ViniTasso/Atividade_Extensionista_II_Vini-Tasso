    
import os
import textwrap
import json
from src import util
import google.generativeai as genai
import google.ai.generativelanguage as glm
from googletrans import Translator as translator    

class Chating_IA:

    """ Os Modelos disponíveis podem ser:
    models/gemini-1.0-pro
    models/gemini-1.0-pro-001
    models/gemini-1.0-pro-latest       
    models/gemini-1.0-pro-vision-latest
    models/gemini-1.5-pro-latest       
    models/gemini-pro
    models/gemini-pro-vision
    """
    
    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
        
    model = genai.GenerativeModel("models/gemini-1.0-pro")

    chat = model.start_chat()
    idioma = "Ingles"

    def texto_padrao_dicas(texto, idioma="inglês"):
        """
        Descrição:
            Esta função gera um texto padrão para solicitar ao modelo de geração de texto que 
            forneça três opções de resposta para uma determinada frase em um idioma específico. 
            O texto também inclui um exemplo de como o resultado deve ser apresentado, com as 
            respostas e suas traduções correspondentes.

        Parâmetros:
            - `texto`: A frase para a qual se deseja gerar opções de resposta.
            - `idioma`: O idioma em que a resposta deve ser gerada (padrão é "inglês").

        Retorno:
            - Uma string contendo o texto padrão com as instruções para gerar opções de resposta.
        """
        return f"""
    Me de 3 opções de resposta para responder a seguinte frase: \n
    {texto} \n
    A resposta escreva em {idioma} e a tradução em português.
    Siga o exemplo de resultado que eu espero: 
    Resposta 1: texto; 
    Traducao 1: texto; 
    Resposta 2: texto; 
    Traducao 2: texto;
    Resposta 3: texto;
    Traducao 3: texto; 
    Substitua a palavra texto pelo resultado obtido. Mostre também um tópico de "Dicas:"
    """

    def possiveis_respostas(texto):
        """
        Descrição:
        E   sta função utiliza o modelo de geração de texto para gerar opções de resposta, 
        traduções e dicas com base em um texto padrão.

        Parâmetros:
            - `texto`: A frase para a qual se deseja gerar opções de resposta.

        Retorno:
            - Um dicionário contendo as opções de resposta, traduções e dicas.

        Frase utilizada no google,
        Exemplo de entrada e saída:

            Como eu posso responder a seguinte frase em francês "Bonjour!", me de 3 opções de 
            resposta e siga o exemplo de resultado
            Resposta 1: texto;
            Traducao 1: texto;

            Resposta 2: texto;
            Traducao 2: texto;

            Resposta 3: texto;
            Traducao 3: texto;

            Substitua a palavra texto pelo resultado obtido.

            Mostre também um tópico de "Dicas:"

        RESPOSTA DO GOOGLE

            Resposta 1: Bonjour!
            Tradução 1: Olá!
            Resposta 2: Salut!
            Tradução 2: Oi!
            Resposta 3: Coucou!
            Tradução 3: Alô!
            Dicas:
            "Bonjour!" é a forma mais comum e educada de dizer "olá" em francês.
            "Salut!" é uma forma mais informal e é usada entre amigos ou familiares.
            "Coucou!" é uma forma ainda mais informal e é usada entre pessoas muito próximas.

        """
        modelAI = Chating_IA.model
        resposta = modelAI.generate_content(Chating_IA.texto_padrao_dicas(texto=texto, idioma=Chating_IA.idioma))
        #print("O primeiro retorno foi:\n"+resposta.text)

        resposta = modelAI.generate_content(textwrap.dedent(
            Chating_IA.texto_padrao_JSON_dicas(resposta.text)
        ))
        #print(json.dumps(json.loads(resposta.text), indent=3))

        return json.loads(resposta.text)

    def texto_padrao_JSON_dicas(texto):
        """
        Descrição:
            Esta função gera um texto padrão com instruções para retornar um JSON descrevendo as 
            respostas de frases, as traduções e as dicas com base em um texto fornecido.

        Parâmetros:
            - `texto`: O texto a ser incluído nas instruções.

        Retorno:
            - Uma string contendo o texto padrão com as instruções para retornar um JSON.

        """
        return """\
    Por favor retorne JSON descrevendo as respostas de frases, as traduções e as dicas desse texto usando o seguinte schema: 

    {"frase": list[FRASE], "traducao":list[TRADUCAO], "dicas":list[DICAS}

    FRASE = {"numero": int, "descricao": str}
    TRADUCAO = {"numero": int, " descricao ": str}
    DICA = {"numero": int, descricao ": str}

    Todos os campos são necessários

    Importante: Só retorne um único texto valido de JSON.

    Aqui está o conteúdo:\n

    """ + texto
        """_summary_
            Cria modelo que permite ser usado como tool no generate e os resultados 
            já são inseridos conforme solicitado.        
        """


    def traduzir_texto(texto):
        traducao = translator.translate(texto, dest=Chating_IA.idioma)
        return traducao

    def unica_pergunta(self, text):
        """
        Descrição:
            Esta função utiliza o modelo de geração de texto para fazer uma pergunta com base no texto fornecido.

        Parâmetros:
            - `text`: O texto da pergunta a ser gerada.

        Retorno:
            - Uma string contendo a pergunta gerada pelo modelo.

        """
        modelAI = Chating_IA.model
        resposta = modelAI.generate_content(text)
        return resposta.text

    def validaConversa(texto):
        """
        Descrição:
            Esta função faz uma pergunta ao usuário para validar se um determinado texto está no idioma especificado.

        Parâmetros:
            - `texto`: O texto a ser validado.

        Retorno:
            - Um valor booleano indicando se o texto está no idioma especificado (True) ou não (False).
        """
        resposta = Chating_IA.unica_pergunta(f"O texto {texto}, está no idioma {Chating_IA.idioma}? \nResponda apenas sim ou não.")
        if "sim" in str.lower(resposta):
            return True
        else:
            return False
        
    def inicia_chat_principal(self, idioma="ingles", tema="Acidente de transito", assunto="dizer que o carro tem multa", nivel="basico"):
        """
        Função responsável por iniciar o módulo de conversação.

        Esta função inicia uma conversa interativa em um idioma escolhido pelo usuário, permitindo 
        a prática de conversação sobre um determinado assunto. Durante a conversa, o usuário pode 
        solicitar dicas sobre o que responder, obter traduções de frases e encerrar a conversação.

        Returns:
            None
        """
        
        #ainda não esta funcionando
        
        self.chat = Chating_IA.model.start_chat(history=[]) #passa uma lista vazia
        if assunto != "":
            assunto = ", com frase principal, " + assunto

        primeira_mensagem = f"""Você é um professor de {idioma} e quer me ensinar o idioma. 
         Você sabe que o meu nível é {nivel} e quer me ensinar por meio de um assunto que uso no meu trabalho,
         o tema é: {tema}{assunto}. 
         Inicie uma conversa comigo, limite sua mensagem para 60 palavras, primeiro envie a 
         estrutura do conteúdo, depois converse sobre cada tópico comigo, limitando 60 palavras 
         por mensagem. Ao invés de mandar todo conteúdo, quero que você evolua nossa conversa 
         gradualmente a medida que você confirmar que eu entendi o conteúdo. 
        Me traga exemplos e dicas e o que for necessario para melhor compreenssão. 
        Inicie a conversa com "Olá querido aluno!" 
        Sua resposta tem que ser o inicio de uma conversa!"""

        response = self.chat.send_message(primeira_mensagem)

        return self.chat.history[-1].parts[0].text
    
    def iteracao_IA(self, mensagem, idioma="ingles"):

        response = self.chat.send_message(mensagem, stream=True)
        
        for chunk in response:
            print(chunk.text)
        
        return self.chat.history[-1].parts[0].text
            