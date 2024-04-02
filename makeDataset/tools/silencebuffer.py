from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import glob

# input path to segmentedAudio folder here and create the paddedAudio folder and put its path here as well.
source_dir = './audio/'
target_dir = './silencedAudio/'

os.makedirs(target_dir, exist_ok=True)

wav_files = glob.glob(os.path.join(source_dir, '*.wav'))

for wav_file in wav_files:
    audio = AudioSegment.from_wav(wav_file)
    chunks = split_on_silence(audio,
    min_silence_len= 232, # minimum length of silence required for a split in ms
    silence_thresh= -70 # volume threshold below which sound is considered silence
)

    silence_chunk = AudioSegment.silent(duration=740)  # amount of silence you want to add in milliseconds

    new_audio = AudioSegment.empty()
    for chunk in chunks:
        new_audio += chunk + silence_chunk 

    new_file_path = os.path.join(target_dir, f"{os.path.basename(wav_file).split('.wav')[0]}_SAA.wav")
    new_audio.export(new_file_path, format='wav')

print("Processing complete. Modified files are saved in:", target_dir)
