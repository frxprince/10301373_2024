from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas

h_bin=10
fdataset=range(1,31)
def getRGBHistogram(IM):
    HR,i=histogram(IM[:,:,0],bins=h_bin)
    HG,i=histogram(IM[:,:,1],bins=h_bin)
    HB,i=histogram(IM[:,:,2],bins=h_bin)
    return(HR/max(HR),HG/max(HG),HB/max(HB)) 

ImT= array(Image.open('./image_dataset1/25.jpg'))
TR,TG,TB=getRGBHistogram(ImT)
D=[]
for fid in fdataset:
    Im= array(Image.open('./image_dataset1/%d.jpg'%fid))
    R,G,B=getRGBHistogram(Im)
    d=  sum(((TR-R)**2 + (TG-G)**2 + (TB-B)**2)**0.5)
    D.append(('./image_dataset1/%d.jpg'%fid, d))
Result= sorted(D,key=lambda tup:(tup[1],tup[0]))    
subplot(3,3,1);imshow(ImT)
for i in range(0,8):
    ImX= array(Image.open(Result[i][0]))
    subplot(3,3,i+2);imshow(ImX)
show()

