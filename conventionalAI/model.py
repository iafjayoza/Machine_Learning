# This is a sample Python script.

from deepspeech import Model
import numpy as np
import os
import wave
from IPython.display import Audio

model_file_path = 'deepspeech-0.9.3-models.pbmm'
lm_file_path = 'deepspeech-0.9.3-models.scorer'
beam_width = 500
lm_alpha = 0.93
lm_beta = 1.18

model = Model(model_file_path)
model.enableExternalScorer(lm_file_path)

model.setScorerAlphaBeta(lm_alpha, lm_beta)
model.setBeamWidth(beam_width)

# Returning Buffer and Rate for given audio file
def read_wave_file(audio_file):
    with wave.open(audio_file, 'rb') as file:
        rate = file.getframerate()
        frames = file.getnframes()
        buffer = file.readframes(frames)
        print("rate is:", rate)
        print("frame is:", frames)

        return buffer, rate

# Creating Voice to Text from DeepSpeech Model
def transcribe(audio_sample):
    buffer, rate = read_wave_file(audio_sample)
    mydata = np.frombuffer(buffer, dtype=np.int16)
    return model.stt(mydata)

# calling transcribe

print("Text:", transcribe('boeing.wav'))




