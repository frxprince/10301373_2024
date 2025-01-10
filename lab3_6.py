from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas

ImGray1=   array(Image.open('match2_1.tiff'))
ImGray2=   array(Image.open('match2_2.tiff'))

subplot(1,3,1);imshow(ImGray1,cmap='gray')
subplot(1,3,2);imshow(ImGray1,cmap='gray')

ImDiff=  abs(double(ImGray1) - double(ImGray2))
subplot(1,3,3);imshow(ImDiff,cmap='gray',vmin=100,vmax=255)
print( "The SAD ="+ str( sum(ImDiff)  ))
show()

