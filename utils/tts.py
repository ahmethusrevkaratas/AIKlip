from gtts import gTTS
import os

def text_to_speech(text, lang='tr', filename="output.mp3"):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename

