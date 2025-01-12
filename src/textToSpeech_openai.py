import pygame
from gtts import gTTS
import os
import playsound
import time

from pydub import AudioSegment
from pydub.playback import play

class textToSpeech_openai:

    def text_to_speech(text, lang="en"):
        """
        Converte texto em áudio e reproduz.
        
        Parâmetros:
        - text (str): Frase a ser convertida.
        - lang (str): Código do idioma (ex.: 'en' para inglês, 'pt' para português, 'es' para espanhol).
        """
        try:
            # Converte o texto para áudio usando gTTS
            tts = gTTS(text=text, lang=lang)
            
            # Salva o arquivo de áudio temporariamente
            audio_file = "temp_audio.mp3"
            tts.save(audio_file)
            
            
            # Remove o arquivo após a reprodução
            # Aguarda o arquivo ser salvo
            timeout = 5  # Tempo máximo de espera em segundos
            start_time = time.time()
            while not os.path.exists(audio_file):
                if time.time() - start_time > timeout:
                    raise TimeoutError("O arquivo de áudio não foi criado a tempo.")
                time.sleep(0.1)

            # Reproduz o áudio
            textToSpeech_openai.playPyGame(audio_file)
            
            
            os.remove(audio_file)

        except PermissionError as e:
            print(f"Erro na permissão do arquivo: {e}")
        except Exception as e:
            print(f"Erro ao converter texto em fala: {e}")
        
        
    def playPyGame(audio_file):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Aguarda a reprodução terminar
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

    def playPyDub(audio_file):
        # Carrega e reproduz o áudio diretamente da memória
        audio = AudioSegment.from_mp3(audio_file)
        play(audio)

    def playSystem(audio_file):
        playsound.playsound(audio_file)
    """
    # Exemplo de uso
    if __name__ == "__main__":
        frases = {
            "en": "Hello, how are you?",
            "pt": "Olá, como você está?",
            "es": "Hola, ¿cómo estás?"
        }
        
        print("Selecione o idioma:")
        print("1. Inglês")
        print("2. Português")
        print("3. Espanhol")
        
        opcao = input("Digite o número da sua escolha: ")
        idioma = {"1": "en", "2": "pt", "3": "es"}.get(opcao, "en")
        
        frase = frases.get(idioma, "Hello, how are you?")
        print(f"Reproduzindo a frase: {frase}")
        text_to_speech(frase, lang=idioma)
    """