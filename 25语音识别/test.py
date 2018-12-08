#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 12:09:49
import wave,requests
from pyaudio import PyAudio, paInt16
import time



framerate = 16000  # 采样率
NUM_SAMPLES = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
TIME = 4 #秒，2000x4=8000
FILENAME='speech.wav'


def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def my_record():
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=channels,
                     rate=framerate, input=True, frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    t=time.time()
    print('正在录音...')
    # while count < TIME * 14:
    while time.time()<t+10: #10秒
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
    save_wave_file(FILENAME, my_buf)
    stream.close()


def play(file):
    wf = wave.open(file, 'rb')
    pa = PyAudio()
    stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
    while True:
        data=wf.readframes(1024)
        if data=='':
            break
        stream.write(data)
    stream.close()
    pa.terminate()

if __name__=='__main__':
    my_record()
    play(FILENAME)