import speech_recognition as sr
import requests
import random
import json
from playsound import playsound
 
r = sr.Recognizer()
 
with sr.AudioFile("sangetsuki.wav") as source:
    audio = r.record(source)
 
text = r.recognize_google(audio, language='ja-JP')

# 音素データ生成
response = requests.post('http://127.0.0.1:50021/audio_query', params = {'text': text, 'speaker': 14})

# 音声合成
wav = requests.post('http://127.0.0.1:50021/synthesis', params = {'speaker': 1}, data=json.dumps(response.json()))
filename = ""
if wav.status_code == 200:
    filename = "sangetsuki-" + str(random.randint(111, 999)) + ".wav"
    with open(filename, "wb") as fp:
        fp.write(wav.content)

    # 再生
    playsound(filename)