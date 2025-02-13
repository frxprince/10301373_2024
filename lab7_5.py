from pylab import *
from scipy.fftpack import *
from lab7fx import *
from PIL import Image
import zlib
import struct
def dct2(Im):
    return dct(dct(Im.T,2,norm='ortho').T,2,norm='ortho')

def idct2(Cm):
    return uint8(idct(idct(Cm.T,norm='ortho').T,norm='ortho'))

Q=array([
[1,	1,	1,	1,	1,	1,	1,	1],
[1,	1,	1,	1,	1,	1,	1,	2],
[1,	1,	1,	1,	1,	2,	2,	2],
[2,	2,	3,	3,	3,	3,	3,	3],
[3,	3,	3,	4,	4,	4,	3,	3],
[4,	3,	3,	3,	4,	5,	4,	4],
[5,	5,	5,	5,	5,	3,	4,	5],
[6,	5,	5,	6,	4,	5,	5,	5]]).astype(float)
Im = int32(array(Image.open('ladybug.bmp')))
h,w=Im.shape
Coded=[]
fig,ax=subplots(1)
ax.imshow(Im,cmap='gray')
block=8
for i in range(0,h,block):
    for j in range(0,w,block):
#        rect=Rectangle((j,i),block,block,linewidth=1,edgecolor='r',facecolor='none')
#        ax.add_patch(rect)
         ImB=Im[i:i+block,j:j+block] -127
         Y=dct2(ImB)
         Yq=(Y/Q).astype(int16)
         Yqz=fzigzag(Yq).astype(int16)
         Coded.extend(Yqz)
bCoded=array(Coded,dtype=int16).tobytes()
jpegdata=zlib.compress(bCoded)
print("original %d x %d = %d compressed to %d , ratio = %f"
      %(w,h,w*h,len(jpegdata),len(jpegdata)/(w*h)))
show()
