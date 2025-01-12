# Atividade_Extensionista_II_Vini-Tasso
Atividade desenvolvida como trabalho para conclusão do curso de análise e desenvolvimento de sistemas pela UNINTER.

# Help Language
Aplicação desenvolvida pensando em auxiliar funcionários da segurança pública, como bombeiros, em situações de atendimento à pessoas extrangeiras.

# Dependencias

É necessário Instalar a biblioteca Google Texto To Speech
pip install gtts playsound

Caso o formato não seja reconhecido, é necessário obter um reprodutor de mídia compatível.

pip install pygame

After import pygame appeard the error SDL downgrade.

https://github.com/pygame/pygame/issues/3992
In this website we shoud enconter the awnser for this problem following this step:
Solution = don't import pygame after importing kivy, kivymd and other modules/libraries just import the pygame at the start of the code and then the error should resolve.
