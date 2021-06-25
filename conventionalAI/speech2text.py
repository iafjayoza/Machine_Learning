# import library
import speech_recognition as sr
import time
from record import *
from main import getReply

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

while True:
    record()
    with sr.AudioFile('audio/sample5.wav') as source:
        audio_text = r.listen(source)

        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print('      ')
            print('User> ', text)
            print('Bot> ', getReply(text))
            print('      ')
            if text in ('exit', 'quit', 'bye'):
                break
            time.sleep(5)
        except:
            print('Sorry.. run again...')
            break