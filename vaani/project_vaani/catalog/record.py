from venv.Lib import librosa 
import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas as pd
from scipy import spatial

def cancel_noise(y):
  x=[]
  j=0
  notestart=[]
  for i in range(0,len(y)):
    if y[i]>0.05:
        notestart.append(i)
        x.append(y[i])
    else:
        x.append(0)
  x=np.array(x)
  return x

def plot_pitch_contour(pitch,pl,time,y):
  c = []
  sum = 0
  sr = 16000
  for i in range(pl):
    if sum <= int(len(y)/sr)+1:
      c.append(sum)
      sum += time
  #c=np.arange(0,len(pitch),1)
  plt.figure(figsize = (70,15))
  plt.scatter(c,pitch)
  plt.title('F0 vs time')
  plt.xlabel('time (seconds)')
  plt.ylabel('F0 (Hz)')
  plt.xticks(c)


def audio_to_pitch(file_name,windtime):
  y, sr = librosa.load(file_name, offset = 0.0,sr=16000)
  time=len(y)/sr
  windsamples=int(windtime*sr)
  #windows=len(y)//windsamples 
  #x = cancel_noise(y)
  f0,voiceflag,voiceprob = librosa.pyin(y,fmin=20,fmax=2000,frame_length=1600,hop_length=windsamples)
  mfcc=librosa.feature.mfcc(y=y, sr=16000)
  rmse = librosa.feature.rms(y,center=True)
  plot_pitch_contour(f0,len(f0),windtime,y)
  return list(f0)

def padding(lst,p):
  print(len(lst),len(p))
  n=len(lst)-len(p)
  print(n)
  if n<0:
    lst=lst.extend([0]*abs(n))
  else:
    p=p.extend([0]*n)
  print(lst,p)



  