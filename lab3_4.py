from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas

Im=   array(Image.open('Unequalized_Hawkes_Bay_NZ.jpg'))
ImGray=uint8(mahotas.colors.rgb2gray(Im))
h,index= histogram(ImGray,range(0,255))
cdf = cumsum(h)
sk= uint8((cdf/max(cdf))*255)
m,n=ImGray.shape
Y = zeros_like(ImGray)
for i in range(0,m):
    for j in range(0,n):
        Y[i,j]= sk[ImGray[i,j]]
        
subplot(3,3,1);imshow(ImGray,cmap='gray',vmin=0,vmax=255)
subplot(3,3,2);bar(index[0:len(index)-1],h)
subplot(3,3,3);bar(index[0:len(index)-1],cdf)
subplot(3,3,4);imshow(Y,cmap='gray',vmin=0,vmax=255)
h2,index= histogram(Y,range(0,255))
cdf2 = cumsum(h2)
subplot(3,3,5);bar(index[0:len(index)-1],h2)
subplot(3,3,6);bar(index[0:len(index)-1],cdf2)

ImGrayPIL= Image.fromarray(ImGray)
Y2= ImageOps.equalize(ImGrayPIL)
subplot(3,3,7);imshow(Y2,cmap='gray',vmin=0,vmax=255)

h2,index= histogram(Y2,range(0,255))
cdf2 = cumsum(h2)
subplot(3,3,8);bar(index[0:len(index)-1],h2)
subplot(3,3,9);bar(index[0:len(index)-1],cdf2)

show()

