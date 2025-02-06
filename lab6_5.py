from pylab import *
from PIL import Image
import mahotas
import scipy.signal
from skimage import *
Im= array(Image.open("frontier_color57.jpg"))
r,c,d=Im.shape
YCbCr= color.rgb2ycbcr(Im)
fY=1
fC=0.2
Y= YCbCr[:,:,0];Cb=YCbCr[:,:,1];Cr=YCbCr[:,:,2]
subplot(2,4,1);imshow(Im)
subplot(2,4,2);imshow(Y,cmap='gray');subplot(2,4,3);imshow(Cb,cmap='gray')
subplot(2,4,4);imshow(Cr,cmap='gray')
Y2=transform.resize(Y,(r*fY,c*fY));Cb2=transform.resize(Cb,(r*fC,c*fC));
Cr2=transform.resize(Cr,(r*fC,c*fC))

Y3=transform.resize(Y2,(r,c));Cr3=transform.resize(Cr2,(r,c));Cb3=transform.resize(Cb2,(r,c))
subplot(2,4,6);imshow(Y3,cmap='gray');subplot(2,4,7);imshow(Cb3,cmap='gray')
subplot(2,4,8);imshow(Cr3,cmap='gray')
YCbCr2=dstack((Y3,Cb3,Cr))
Im2= color.ycbcr2rgb(YCbCr2)
figure()
subplot(1,2,1);imshow(Im)
subplot(1,2,2);imshow(Im2)

show()
