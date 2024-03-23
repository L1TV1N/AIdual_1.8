from pydub import AudioSegment
from pydub.generators import WhiteNoise

# Загрузка аудиофайла
audio = AudioSegment.from_file("audioUP_out.wav")

# Применение фильтра
filtered_audio = audio.low_pass_filter(9000)

# Сохранение результата
filtered_audio.export("filt_audio.wav", format="wav")
