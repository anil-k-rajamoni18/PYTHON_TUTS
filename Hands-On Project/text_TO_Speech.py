from gtts import gTTS

file = open('sample.txt')

data = file.read()

language = 'en'

audio = gTTS(text=data)

audio.save('audio.mp3')