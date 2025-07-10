import pyttsx3


def play_voice_assistant_speech(text_to_speech):
    ttsEngine=pyttsx3.init()
    voices = ttsEngine.getProperty("voices")
    ttsEngine.setProperty("voice", 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()
