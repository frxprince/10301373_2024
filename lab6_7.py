from pylab import *
from PIL import Image
import mahotas
import scipy.signal
from skimage import *
Im= mahotas.colors.rgb2gray(array(Image.open("solarwind.bmp")))
subplot(1,2,1);imshow(Im,cmap='gray')
subplot(1,2,2);imshow(Im/3,cmap='hot')

C= plt.cm.hot
Im2 = C(uint8(Im/3))

Im3 = Image.fromarray(    uint8((Im2 / Im2.max())*255)        )
Im3.save('output.png')
figure()
imshow(Im2)
show()
