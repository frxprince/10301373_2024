from pylab import *
from scipy.fftpack import *

I=array([
[208,	244,	108,	173,	71,	112,	181,	245],
[231,	246,	234,	193,	12,	97,	192,	87],
[32,	40,	202,	189,	25,	195,	70,	149],
[233,	248,	245,	100,	210,	203,	173,	57],
[161,	244,	167,	167,	177,	48,	167,	192],
[25,	124,	9,	44,	81,	125,	41,	65],
[71,	204,	217,	180,	242,	114,	30,	129],
[139,	36,	238,	8,	9,	165,	127,	178]
])

Y=dct(dct(I.T,2,norm='ortho').T,2,norm='ortho')
I2=uint8(idct(idct(Y.T,norm='ortho').T,norm='ortho'))
subplot(1,3,1);imshow(I,cmap='gray')
subplot(1,3,2);imshow(Y,cmap='gray')
subplot(1,3,3);imshow(I2,cmap='gray')
show()
