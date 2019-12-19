from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import matplotlib
matplotlib.use('TkAgg')
import os
import pydub
from winapp2 import Main
##############################################
data_dir = "./set_a"
audio_files = glob(data_dir + "/*.wav")
def wr_in_file():
    for file in range(0, len(audio_files), 1):
        fs_rate, sig = wavfile.read(audio_files[file])
        l_audio = len(sig.shape)
        if l_audio == 2:
            sig = sig.sum(axis=1) / 2
        N = sig.shape[0]
        secs = N / float(fs_rate)
        Ts = 1.0 / fs_rate  # сепл интервал во времени
        t = scipy.arange(0, secs, Ts)  # рассчет времении вектора field / numpy.ndarray
        FFT = abs(scipy.fft(sig))
        FFT_side = FFT[range(N // 2)]  # бпф
        freqs = scipy.fftpack.fftfreq(sig.size, t[1] - t[0])
        fft_freqs = np.array(freqs)
        freqs_side = freqs[range(N // 2)]  # частота
        fft_freqs_side = np.array(freqs_side)
        file_name = r'FFT_side/file{}.txt'.format(file)
        with open(file_name, 'wb') as f:
            f.write(FFT_side)
        file_name = r'freqs_side/file{}.txt'.format(file)
        with open(file_name, 'wb') as f:
            f.write(freqs_side)
def display_plot_file(filename):
                ####### var #######
    fs_rate, sig = wavfile.read(filename)
    l_audio = len(sig.shape)
    # Wav files could headers or have riffd parts,
    if l_audio == 2:
        sig = sig.sum(axis=1) / 2
    N = sig.shape[0]
    secs = N / float(fs_rate)
    Ts = 1.0 / fs_rate  # сепл интервал во времени
    t = scipy.arange(0, secs, Ts)  # рассчет времении вектора field / numpy.ndarray
    FFT = abs(scipy.fft(sig))
    FFT_side = FFT[range(N // 2)]  # бпф
    freqs = scipy.fftpack.fftfreq(sig.size, t[1] - t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(N // 2)]  # частота
    fft_freqs_side = np.array(freqs_side)
                ####### var #######
    plt.subplot(311)
    p1 = plt.plot(t, sig, "g")  # ресуем первоначальный фид
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.subplot(312)
    p2 = plt.plot(freqs, FFT, "r")  # не посредственно бпф
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count dbl-sided')
    plt.subplot(313)
    p3 = plt.plot(freqs_side, abs(FFT_side), "b")  # положительный бпф
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count single-sided')
    plt.show()
def convertor() :
    wav_file = glob("set_b/*.mp3")
    for wav_file in wav_file:
        mp3_file = os.path.splitext(wav_file)[0] + ".wav"
        sound = pydub.AudioSegment.from_mp3(wav_file)
        sound.export(mp3_file , format = "wav")
        os.remove(wav_file)