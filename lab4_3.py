from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas
import scipy.signal

Im= mahotas.colors.rgb2gray((array(Image.open('lena512color.tiff'))))
#G= [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
a=0.8
G = [[0,1,0],[1,-4,1],[0,1,0]]
Im2= scipy.signal.convolve2d(Im,G,mode='valid')
subplot(1,3,1);imshow(Im,cmap='gray')
subplot(1,3,2);imshow(Im2,cmap='gray',vmin=0,vmax=255)
h,w= Im.shape
Im3= (abs(Im2)*a)+Im[0:h-2,0:w-2]
subplot(1,3,3);imshow(Im3,cmap='gray',vmin=0,vmax=255)



show()

