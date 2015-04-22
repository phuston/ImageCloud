import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/img.jpg',0)


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
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
maskLPF = np.zeros((rows,cols,2),np.uint8)
maskLPF[crow-50:crow+50, ccol-50:ccol+50] = 1 # LPF - creates box of 1's in center to 'mask' input

# create a mask first, center square is 0, remaining all ones
maskHPF = np.ones((rows,cols,2),np.uint8)
maskHPF[crow-50:crow+50, ccol-50:ccol+50] = 0 # HPF - creates box of 0's in center to 'mask' input



# apply mask and inverse DFT
fshift = dft_shift*maskHPF
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()