# from vosk import Model, KaldiRecognizer
# import os
# import pyaudio
#
# # Укажите путь к модели
# model_path = "vosk-model-small-ru-0.22"
# model = Model(model_path)
#
# rec = KaldiRecognizer(model, 16000)
#
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
# stream.start_stream()
#
# while True:
#     data = stream.read(4000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         print(rec.Result())
#     else:
#         print(rec.PartialResult())
from vosk import Model, KaldiRecognizer
import os
import pyaudio

# Укажите путь к модели
model_path = "vosk-model-small-ru-0.22"
model = Model(model_path)

rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Откройте файл для записи
with open('output.txt', 'w') as f:
    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # Запишите результат в файл
            f.write(rec.Result())
            f.write('\n')
        else:
            # Запишите частичный результат в файл
            f.write(rec.PartialResult())
            f.write('\n')
