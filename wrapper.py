"""
ImageCloud Wrapper
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read, write

from imagecompress import Im2Audio
from soundread import SoundRead
from cloudwrapper import CloudClient


if __name__ == '__main__':
    imgname = 'img/img.jpg'
    wavname = 'out/byronpat.wav'

    im = Im2Audio(imgname)
    im.plot_mag()
    im.highpass()
    im.shape_and_scale()
    im.write(wavname)

    sc = CloudClient()
    sc.post_track(wavname)

    wv = SoundRead(wavname)
    wv.unscale_and_shape()
    wv.to_image('out/flowerout', color=True)