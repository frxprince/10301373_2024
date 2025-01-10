from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas
import scipy.signal

Im= (array(Image.open('noise1.bmp')))
#G= [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
w=6
G = ones((w,w))/(w*w)
Im2= scipy.signal.convolve2d(Im,G,mode='same',boundary='symm')
subplot(1,2,1);imshow(Im,cmap='gray')
subplot(1,2,2);imshow(Im2,cmap='gray')
show()

