import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

rate, wav = read('test.wav')

img_size = wav[0:2]
scalar = wav[2:3]
# print img_size
# print scalar
wav = np.delete(wav,[0,1,2])
unscaled_arr = np.array(wav * scalar)