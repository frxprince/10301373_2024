from pylab import *
from PIL import Image
import mahotas

Im= array(Image.open("frontier_color57.jpg"))
Im_HSV= matplotlib.colors.rgb_to_hsv(Im/255)
H=Im_HSV[:,:,0]
S=Im_HSV[:,:,1]
V=Im_HSV[:,:,2]
subplot(1,4,1);imshow(Im)
subplot(1,4,2);imshow(H,cmap='gray')
subplot(1,4,3);imshow(S,cmap='gray')
subplot(1,4,4);imshow(V,cmap='gray')

S=clip(S*2,0,1)
Im2= uint8(matplotlib.colors.hsv_to_rgb(dstack((H,S,V)))*255)
figure()
imshow(Im2,vmin=0,vmax=255)




show()
