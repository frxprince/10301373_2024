from PIL import Image
from pylab import *
import mahotas
#from scipy.misc import imresize

im=Image.open('lena512color.tiff')
Im= array(im)
#imshow(Im);show()
(h,w,d)=Im.shape
print("width=%d height=%d color depth=%d"%(w,h,d))
Im_R= Im[:,:,0]
Im_G= Im[:,:,1]
Im_B= Im[:,:,2]
ImTmp=zeros((h,w,d),dtype=uint8)
Im_R2=ImTmp.copy(); Im_R2[:,:,0]=Im_R
Im_G2=ImTmp.copy(); Im_G2[:,:,1]=Im_G
Im_B2=ImTmp.copy(); Im_B2[:,:,2]=Im_B
#subplot(1,4,1);imshow(Im)
#subplot(1,4,2);imshow(Im_R2)
#subplot(1,4,3);imshow(Im_G2)
#subplot(1,4,4);imshow(Im_B2)
#imshow(Im_R,cmap='gray')
#figure()
#imshow(Im_G,cmap='gray')
#figure()
#imshow(Im_B,cmap='gray')
#
#ImGray=zeros((h,w),dtype=uint8)
#for r in range(0,h):
#    for c in range(0,w):
#       ImGray[r,c]=(Im[r,c,0]* 0.299)+(Im[r,c,1]*0.587)+(Im[r,c,2]*0.114)
def rgb2gray(RGB):
    return dot(RGB[...,:3],[0.299 ,0.587, 0.114])


#ImGray=rgb2gray(Im)
#ImGray= mahotas.colors.rgb2gray(Im)
    #   0.299R+0.587G+0.114B
#imshow(ImGray,cmap='gray')
Im_small=array(im.resize((round(0.5*h),round(0.5*w))))
subplot(1,2,1);imshow(Im);subplot(1,2,2);imshow(Im_small)

show()


