import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

#read wav file
rate, wav = read('test.wav')

#get image size from first 2 elements, max value from 3rd and scalar from 4th
img_size = wav[0:2]
arr_max = wav[2:3]
scalar = wav[3:4]

# #for sounds not from images
# img_size = (int(np.sqrt(len(wav)/2)))
# arr_max = 600000 #completely arbitrary
# scalar = 32767
# wav = np.array(wav[0:(img_size**2*2)])
# print len(wav)
# print img_size

#delete first 4 elements (info elements)
wav = np.delete(wav,[0,1,2,3])

#unscale the array
unscaled_arr = np.array(wav/scalar)
unscaled_arr = np.array(unscaled_arr*np.abs(arr_max))

#reshape the array
unreshape_arr = np.reshape(unscaled_arr,(img_size[0],img_size[1],2))

#convert back into image
f_ishift = np.fft.ifftshift(unreshape_arr)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


# plt.subplot(121),plt.imshow(img_back, cmap = 'gray')
# plt.title('Image'), plt.xticks([]), plt.yticks([])
# plt.show()

#save images with pyplot
plt.imsave("img_back.png", img_back)
plt.imsave("img_back_gray.png",img_back,cmap='gray')