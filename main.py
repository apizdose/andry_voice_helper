import queue
import sys
import sounddevice as sd
import voice
import gptAI
from vosk import Model, KaldiRecognizer
import os.path

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

try:
  
    device_info = sd.query_devices(None, "input")
    samplerate = int(device_info["default_samplerate"])
    if os.path.exists("model-ru"):
        model = Model("model-ru")
    else:
        model = Model(lang="ru")
    dump_fn = None

    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=None,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                text=rec.Result()[14:-3]
                print(text)
                keywords=["андрюша","андрюшей","андрей","андроид"]
                for i in keywords:
                    if i in text:
                        ans=gptAI.botreq(text)
                        voice.play_voice_assistant_speech(ans)
            else:
                pass
                #print(rec.PartialResult())


except KeyboardInterrupt:
    print("\nDone")
    exit(0)
except Exception as e:
    exit(type(e).__name__ + ": " + str(e))

