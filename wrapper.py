"""
ImageCloud Wrapper
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read, write

from imagecompress import Im2Audio
from soundread import SoundRead


if __name__ == '__main__':
    imgname = 'img/stripesHorizontal.png'
    wavname = 'out/flower.wav'

    im = Im2Audio(imgname)
    im.plot_mag()
    im.highpass()
    im.shape_and_scale()
    im.write(wavname)

    wv = SoundRead(wavname)
    wv.unscale_and_shape()
    wv.to_image('out/flowerout', color=True)