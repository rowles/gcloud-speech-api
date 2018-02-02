import base64
import json
import os
import requests

G_KEY = os.environ['G_KEY']
SPEECH_URI = 'https://speech.googleapis.com/v1/speech:recognize?key=%s' % G_KEY


def transcribe(fname: str) -> dict:
    with open(fname, 'rb') as audio_file:
        audio_b64 = base64.encode(audio_file.read())

        payload = {
                'config': {
                    'encoding': 'LINEAR16',
                    'sampleRateHertz': 44100,
                    'languageCode': 'en-US'
                    },
                'audio': {
                    'content': audio_b64.decode('ascii')
                    }
                }

        r = requests.post(SPEECH_URI, json=payload)
        return r.json()


if __name__ == '__main__':
    resp = transcribe('test.wav')
    print(resp)
