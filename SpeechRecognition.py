import os
import json
import wave
from vosk import Model, KaldiRecognizer
from Models import MODELS
from Helper import format_timestamp


def transcribe(audio_path, lang):
    if not os.path.exists('vosk/' + MODELS[lang]):
        return

    model = Model('vosk/' + MODELS[lang])
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    rec.SetWords(True)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))

    srt_output = []
    counter = 1

    for res in results:
        if 'result' not in res or not res['result']:
            continue

        words = res['result']

        start = format_timestamp(words[0]['start'])
        end = format_timestamp(words[-1]['end'])
        text = res.get('text', '')

        srt_output.append(f"{counter}")
        srt_output.append(f"{start} --> {end}")
        srt_output.append(f"{text}\n")
        counter += 1

    return "\n".join(srt_output)