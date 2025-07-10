import pyttsx3

def play_voice_assistant_speech(text_to_speech):
    ttsEngine=pyttsx3.init()
    voices = ttsEngine.getProperty("voices")
    ttsEngine.setProperty("voice", voices[2].id)
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()
