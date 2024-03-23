# from pydub import AudioSegment
import moviepy.editor as mp

def extract_audio_from_video(video_path, output_audio_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)

# Пример использования:
video_path = "goblin.mp4"
output_audio_path = "audio_out.wav"

extract_audio_from_video(video_path, output_audio_path)
