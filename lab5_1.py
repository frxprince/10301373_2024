from pylab import *
import mahotas
from PIL import Image

Im= array(Image.open('otsu2.jpg'))
Img= mahotas.colors.rgb2gray(Im)
t=50
t2=200
Img_s= (Img >= t) * (Img < t2)   

subplot(1,2,1);imshow(Img,cmap='gray')
subplot(1,2,2);imshow(Img_s,cmap='gray')

figure(2)
Im_s = Im.copy()
Im_s[:,:,0]=Im_s[:,:,0] * Img_s
Im_s[:,:,1]=Im_s[:,:,1] * Img_s
Im_s[:,:,2]=Im_s[:,:,2] * Img_s
imshow(Im_s)


show()
