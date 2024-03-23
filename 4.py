# -*- coding: utf-8 -*-
# #!/usr/bin/env python3
#
# from vosk import Model, KaldiRecognizer, SetLogLevel
# import sys
# import os
# import wave
#
# SetLogLevel(0)
#
# if len(sys.argv) == 2:
#     wf = wave.open(sys.argv[1], "rb")
# else:
#     wf = wave.open("audioUP_out.wav", "rb")
#
# if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
#     print ("Audio file must be WAV format mono PCM.")
#     exit (1)
#
# model = Model("vosk-model-small-ru-0.22")
# rec = KaldiRecognizer(model, wf.getframerate())
# rec.SetWords(True)
#
# while True:
#     data = wf.readframes(1000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         print(rec.Result())
#     else:
#         print(rec.PartialResult())
#
# print(rec.FinalResult())
#!/usr/bin/env python3

# from vosk import Model, KaldiRecognizer, SetLogLevel
# import sys
# import os
# import wave
# import json
# import pandas as pd
#
# SetLogLevel(0)
#
# if len(sys.argv) == 2:
#     wf = wave.open(sys.argv[1], "rb")
# else:
#     wf = wave.open("audioUP_out.wav", "rb")
#
# if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
#     print ("Audio file must be WAV format mono PCM.")
#     exit (1)
#
# model = Model("vosk-model-small-ru-0.22")
# rec = KaldiRecognizer(model, wf.getframerate())
# rec.SetWords(True)
#
# # Создайте пустой DataFrame
# df = pd.DataFrame()
#
# while True:
#     data = wf.readframes(1000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         # Преобразуйте данные из формата JSON в словарь Python
#         data_dict = json.loads(rec.Result())
#         # Создайте DataFrame из словаря
#         df_new = pd.DataFrame(data_dict['result'])
#         # Добавьте новый DataFrame в существующий DataFrame
#         df = pd.concat([df, df_new], ignore_index=True)
#
# # Сохраните DataFrame в файл CSV
# df.to_csv('structured_output.csv', index=False)
#
# print("Final result saved to structured_output.csv")

from vosk import Model, KaldiRecognizer
import sys
import os
import time
import wave
import csv
import json

model = Model("vosk-model-small-ru-0.22")

wf = wave.open('audioUP_out.wav', "rb")
rec = KaldiRecognizer(model, 16000)

result = []
last_n = False

while True:
    data = wf.readframes(8000)
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())

        if res['text'] != '':
            result.append(res['text'])
            last_n = False
        elif not last_n:
            result.append('\n')
            last_n = True

res = json.loads(rec.FinalResult())
result.append(res['text'])

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for line in result:
        writer.writerow([line])

print("Data written to output.csv")