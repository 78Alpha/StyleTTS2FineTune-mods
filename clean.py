import os
import glob

main_dir = os.getcwd()

trainingData = glob.glob(f"{main_dir}/trainingdata/*.txt")
srt = glob.glob(f"{main_dir}/srt/*.*")
silencedAudio = glob.glob(f"{main_dir}/silencedAudio/*.wav")
segmentedAudio = glob.glob(f"{main_dir}/segmentedAudio/*.wav")
paddedAudio = glob.glob(f"{main_dir}/paddedAudio/*.wav")
badAudio = glob.glob(f"{main_dir}/badAudio/*.wav")

cleanupDir = [trainingData, srt, silencedAudio, segmentedAudio, paddedAudio, badAudio]

for dir in cleanupDir:
    for item in dir:
        os.remove(item)
