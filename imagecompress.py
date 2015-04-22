import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import write

img = cv2.imread('img/sheetmusic.jpg',0)


# Convert image to np array, shift DC to center of image
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


# Displays frequency domain view of image - DC centered
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

rows, cols = img.shape
img_size = np.array([rows,cols])
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
maskLPF = np.zeros((rows,cols,2),np.uint8)
maskLPF[crow-50:crow+50, ccol-50:ccol+50] = 1 # LPF - creates box of 1's in center to 'mask' input

# create a mask first, center square is 0, remaining all ones
maskHPF = np.ones((rows,cols,2),np.uint8)
maskHPF[crow-50:crow+50, ccol-50:ccol+50] = 0 # HPF - creates box of 0's in center to 'mask' input



# apply mask and inverse DFT
fshift = dft_shift*maskLPF
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


# Reshapes 2D array into 1D array
reshape_arr = np.reshape(img_back, np.product(img_back.shape))
arr_max = np.max(reshape_arr)
scalar = 32767
scaled_arr = np.int16(reshape_arr/np.max(reshape_arr) * 32767)

full_sample = np.concatenate([img_size, np.array([arr_max,scalar]), scaled_arr])
print full_sample


write('test.wav', 44100, full_sample)


# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

# TODO: Implement soundcloud API, but also figure out how to go from wav file back to 2d numpy array representing image
# Because we have to store image as 1D array, we need to add data to np array representing info about the size of the image 