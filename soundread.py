import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

class SoundRead():
    def __init__(self,wav_file):
        #read wav file
        self.rate, self.wav = read(wav_file)

        #get image size from first 2 elements, max value from 3rd and scalar from 4th
        self.img_size = self.wav[0:2]
        self.arr_max = self.wav[2:3]
        self.scalar = self.wav[3:4]

        #delete first 4 elements (info elements)
        self.wav = np.delete(self.wav,[0,1,2,3])

        # #for sounds not from images
        # img_size = (int(np.sqrt(len(wav)/2)))
        # arr_max = 600000 #completely arbitrary
        # scalar = 32767
        # wav = np.array(wav[0:(img_size**2*2)])
        # print len(wav)
        # print img_size

    def unscale_and_shape(self):
        #unscale the array
        unscaled_arr = np.array(self.wav/self.scalar)
        self.unscaled_arr = np.array(unscaled_arr*np.abs(self.arr_max))
        #reshape the array
        self.unreshape_arr = np.reshape(self.unscaled_arr,(self.img_size[0],self.img_size[1],2))

    def to_image(self,filename,color=True):
        #convert back into image
        f_ishift = np.fft.ifftshift(self.unreshape_arr)
        img_back = cv2.idft(f_ishift)
        img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

        # plt.subplot(121),plt.imshow(img_back, cmap = 'gray')
        # plt.title('Image'), plt.xticks([]), plt.yticks([])
        # plt.show()

        #save images with pyplot
        if color:
            plt.imsave(filename + "_color.png", img_back)
        plt.imsave(filename + "_gray.png",img_back,cmap='gray')