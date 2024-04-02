import os
import glob

trainingData = glob.glob("/mnt/q/Utilities/CUDA/StyleTTS2FineTune/trainingdata/*.txt")
srt = glob.glob("/mnt/q/Utilities/CUDA/StyleTTS2FineTune/srt/*.*")
silencedAudio = glob.glob("/mnt/q/Utilities/CUDA/StyleTTS2FineTune/silencedAudio/*.wav")
segmentedAudio = glob.glob("/mnt/q/Utilities/CUDA/StyleTTS2FineTune/segmentedAudio/*.wav")
paddedAudio = glob.glob("/mnt/q/Utilities/CUDA/StyleTTS2FineTune/paddedAudio/*.wav")
badAudio = glob.glob("/mnt/q/Utilities/CUDA/StyleTTS2FineTune/badAudio/*.wav")

cleanupDir = [trainingData, srt, silencedAudio, segmentedAudio, paddedAudio, badAudio]

for dir in cleanupDir:
    for item in dir:
        os.remove(item)