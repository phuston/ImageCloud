import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import write

class Im2Audio():
    def __init__(self, img_file):
        self.img = cv2.imread(img_file,0)

        # Convert image to np array, shift DC to center of image
        dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT) 
        self.dft_shift = np.fft.fftshift(dft)

        self.rows, self.cols = self.img.shape
        self.img_size = np.array([rows,cols])
        self.crow,self.ccol = self.rows/2 , self.cols/2
        # apply mask and inverse DFT
        self.fshift = self.dft_shift

    def plot_mag(self):
        magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

        # Displays frequency domain view of image - DC centered
        plt.subplot(121),plt.imshow(img, cmap = 'gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()

    def lowpass(self):
        # create a mask first, center square is 1, remaining all zeros
        maskLPF = np.zeros((self.rows,self.cols,2),np.uint8)
        maskLPF[self.crow-50:self.crow+50, self.ccol-50:self.ccol+50] = 1 # LPF - creates box of 1's in center to 'mask' input
        # apply mask and inverse DFT
        self.fshift = self.dft_shift * maskLPF

    def highpass(self):
        # create a mask first, center square is 0, remaining all ones
        maskHPF = np.ones((self.rows,self.cols,2),np.uint8)
        maskHPF[self.crow-50:self.crow+50, self.ccol-50:self.ccol+50] = 0 # HPF - creates box of 0's in center to 'mask' input
        # apply mask and inverse DFT
        self.fshift = self.dft_shift * maskHPF

    def shape_and_scale(self):
        # Reshapes 2D array into 1D array
        # Generate audio from frequency domain rather than original image
        reshape_arr = np.reshape(self.fshift, np.product(self.fshift.shape))
        self.arr_max = np.max(self.reshape_arr)
        self.scalar = 32767
        scaled_arr = np.array(reshape_arr/np.abs(self.arr_max) * self.scalar)

        self.full_sample = np.concatenate([self.img_size, np.array([self.arr_max,self.scalar]), scaled_arr])

    def write(self, filename):
        write(filename + '.wav', 44100, self.full_sample)