from pydub import AudioSegment

input_file = "audio_out.wav"
output_file = "audioUP_out.wav"

def convert_to_mono_8k(input_file, output_file):
    sound = AudioSegment.from_file(input_file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound.export(output_file, format="wav")



convert_to_mono_8k(input_file, output_file)
