import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Set the input and output file paths
input_file = 'input.mp4'
output_file = 'output.mp3'

# Load the video file
video = VideoFileClip(input_file)

# Extract the audio from the video
audio = video.audio

# Write the audio to a temporary WAV file
temp_wav_file = 'temp.wav'
audio.write_audiofile(temp_wav_file)

# Load the audio file
sound = AudioSegment.from_file("temp.wav", "wav")

# Specify the ffmpeg executable path (if necessary)
AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"  # Replace with the actual path to ffmpeg.exe

# Export the audio to MP3
output_file = "output.mp3"
sound.export(output_file, format="mp3")

# Remove the temporary WAV file
os.remove(temp_wav_file)

print(f"Audio extracted and saved to {output_file}")