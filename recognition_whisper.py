# -*- coding: utf-8 -*-
import whisper
from moviepy.editor import VideoFileClip

# Загружаем модель для русского языка
model = whisper.load_model("medium")

# Путь к видеофайлу
video_file = "goblin.mp4"

# Извлекаем аудио из видеофайла
video_clip = VideoFileClip(video_file)
audio = video_clip.audio

# Сохраняем аудио во временный файл
temp_audio_file = "audio111.mp3"
audio.write_audiofile(temp_audio_file)

# Загружаем аудиофайл и дополняем или обрезаем его для подгонки под 30 секунд
audio = whisper.load_audio(temp_audio_file)
audio = whisper.pad_or_trim(audio)

# Создаем логарифмическую мел-спектрограмму и переносим ее на тот же устройство, что и модель
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# Декодируем аудио
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# Сохраняем распознанный текст в файл
output_file = "output_ru.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result.text)

print("Распознанный текст сохранен в файл", output_file)
