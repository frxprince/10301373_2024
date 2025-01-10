from pylab import *
from PIL import Image
import mahotas

Im= array(Image.open('lena512color.tiff'))
ImGray=    mahotas.colors.rgb2gray(Im)
subplot(1,2,1);imshow(ImGray,cmap='gray',vmin=0,vmax=255)

c=int(input('Input the contrast value -255,255 '))
f=(259*(c+255))/(255*(259-c))
ImAdj= clip(((ImGray-128)*f)+128,0,255)
subplot(1,2,2);imshow(ImAdj,cmap='gray',vmin=0,vmax=255)
show()
