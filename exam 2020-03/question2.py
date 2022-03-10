import numpy as np
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt

fn = 'violin.wav'


def pitch(frequency):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    f_c0 = 440 * 2**(-4.75)
    h = 12 * np.log2(frequency/f_c0)
    h_bracket = round(h)
    o = h_bracket // 12
    n = h_bracket % 12

    return f'{notes[n]}{o}'


def read_soundfile(filename):
    samplerate, data = scipy.io.wavfile.read(filename, mmap=False)
    length = data.shape[0] / samplerate
    time = np.linspace(0, length, data.shape[0])
    plt.plot(time, data)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude [arb. units]")
    plt.title('Amplitude as a function of time over the violin.wav file')
    plt.show()


def dominating_freq(filename):
    samplerate, data = scipy.io.wavfile.read(filename, mmap=False)
    fourier = np.abs(np.fft.fft(data))

    freq = np.fft.fftfreq(len(fourier), d=1./samplerate)

    midx = np.argmax(fourier)
    base_frequency = np.abs(freq[midx])
    note = pitch(base_frequency)
    print('The frequency of the violin sound is', base_frequency, 'which correspond to the note', note)
    plt.plot(freq, fourier)
    plt.xlim([0, 3000])
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.title('Amplitude as a function of frequency over the violin.wav file')
    plt.show()








dominating_freq(fn)