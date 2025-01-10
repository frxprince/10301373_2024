from pylab import *
from PIL import Image
import mahotas

Im= array(Image.open('lena512color.tiff'))
ImGray=    mahotas.colors.rgb2gray(Im)
subplot(1,2,1);imshow(ImGray,cmap='gray',vmin=0,vmax=255)

ImAdj=(clip(ImGray-50,0,255)).astype('uint8')

subplot(1,2,2);imshow(ImAdj,cmap='gray',vmin=0,vmax=255)
show()
