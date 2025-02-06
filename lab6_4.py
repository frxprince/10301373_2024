from pylab import *
from PIL import Image
import mahotas
import scipy.signal
Im= array(Image.open("led.jpg"))
Im_HSV= matplotlib.colors.rgb_to_hsv(Im/255)
H=Im_HSV[:,:,0]
S=Im_HSV[:,:,1]
V=Im_HSV[:,:,2]
subplot(2,4,1);imshow(Im)
subplot(2,4,2);imshow(H,cmap='gray')
subplot(2,4,3);imshow(S,cmap='gray')
subplot(2,4,4);imshow(V,cmap='gray')

H2 = H > 0
subplot(2,4,6);imshow(H2,cmap='gray')
S2 = S  <0.1
subplot(2,4,7);imshow(S2,cmap='gray')
V2 = V  > 0.9
subplot(2,4,8);imshow(V2,cmap='gray')
ROI = H2 * V2 * S2
subplot(2,4,5);imshow(ROI,cmap='gray')

G= ones((5,5),dtype=double)/(5*5)
ROI2= scipy.signal.convolve2d(ROI,G, 'same') > 0



Im2=Im.copy()
Im2[:,:,0]= Im2[:,:,0] * ROI2
Im2[:,:,1]= Im2[:,:,1] * ROI2
Im2[:,:,2]= Im2[:,:,2] * ROI2
figure()
imshow(Im2)
show()
