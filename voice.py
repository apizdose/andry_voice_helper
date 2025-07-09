import pyttsx3

ttsEngine=pyttsx3.init()
voices = ttsEngine.getProperty("voices")
ttsEngine.setProperty("voice", voices[2].id)
print(voices)

def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()
