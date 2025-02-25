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

#Q=array([
#[1,	1,	10,	16,	24,	40,	51,	61],
#[1,	1,	14,	19,	26,	58,	60,	55],
#[14,	13,	16,	24,	40,	57,	69,	56],
#[14,	17,	22,	29,	51,	87,	80,	62],
#[18,	22,	37,	56,	68,	109,	103,	77],
#[24,	36,	55,	64,	81,	104,	113,	92],
#[49,	64,	78,	87,	103,	121,	120,	101],
#[72,	92,	95,	98,	112,	100,	103,	99]
#    ]).astype(float)

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

#decode
bCoded2=zlib.decompress(jpegdata)
intData2=[]
for i in range(0,len(bCoded2),2):
    intData2.extend(struct.unpack('h',bCoded2[i:i+2]))
Coded2=array(intData2)    
offset=0
Im2=zeros((h,w))
for i in range(0,h,block):
    for j in range(0,w,block):
        Yqz2=Coded2[offset:offset+(block*block)]
        Yq2=array(izigzag(Yqz2,block,block)).astype(int16)
        Y2=Yq2*Q
        Imb2=clip(idct2(Y2)+127,0,255)
        Im2[i:i+block,j:j+block]=Imb2.astype(uint8)
        offset=offset+(block*block)
figure(2)
subplot(1,3,1);imshow(Im,cmap='gray')
subplot(1,3,2);imshow(Im2,cmap='gray')
subplot(1,3,3);imshow(abs(Im-Im2).astype(uint8)*10,cmap='gray')


show()
