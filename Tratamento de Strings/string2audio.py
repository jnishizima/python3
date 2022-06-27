# Necessario a instalar esse dois
# pip install gtts
# pip install playsound

from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text='meu primero audio, sou python',
    lang=language
)

sp.save(audio)
playsound(audio)