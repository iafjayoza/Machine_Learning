import sounddevice as sd
import soundfile as sf

samplerate = 16000
duration = 7 # seconds
filename = 'audio/sample5.wav'

def record():
    print("start")
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
        channels=1, blocking=True)
    print("end")
    sd.wait()
    sf.write(filename, mydata, samplerate)