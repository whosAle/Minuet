#soundwave.py
#Alejandro Belgrave
#November 7, 2013

import audio
import math

class Soundwave :
    def __init__(self, halftones = 0, duration = 0, amp = 1.0, samplerate = 44100):
        if isinstance(halftones, str):
            self.samples = audio.read_file(halftones)
            self.samplerate = samplerate
            self.length = len(self.samples)/samplerate
            self.maxvol = 1.0
        else:
            self.length = duration
            self.maxvol = amp
            self.samplerate = samplerate
            self.samples = []
            freq = 440*(2**((halftones+3)/12))
            for t in range(int(duration*samplerate//1)):
                y = amp*math.sin(2*math.pi*freq*t/samplerate)
                self.samples.append(y)
       
    def play(self):
        audio.play(self.samples)
   
    def concat(self, s2):
        self.length = self.length + s2.length
        if self.maxvol > s2.maxvol:
            self.maxvol = s2.maxvol
        self.samples.extend(s2.samples)
    
    def plus(self, s2):
        if self.length < s2.length:
            s3 = s2.copy()
            superpos = len(self.samples)
        s3 = self.copy()
        superpos = len(s2.samples)
        
        for i in range(int(superpos)):
            s3.samples[i] = self.samples[i] + s2.samples[i]
        return s3
    
    def copy(self):
        copy = Soundwave(0,0, self.maxvol,self.samplerate)
        copy.samples = [] + self.samples
        copy.length = self.length
        return copy