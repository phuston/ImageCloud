import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

rate, wav = read('test.wav')
print wav
img_size = wav[0:2]
arr_max = wav[2:3]
scalar = wav[3:4]
# print img_size
print arr_max
print scalar
wav = np.delete(wav,[0,1,2])
# unscaled_arr = np.array(wav * scalar)
# print unscaled_arr
# reshape_arr = np.reshape(unscaled_arr,img_size)
# print reshape_arr