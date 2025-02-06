from pylab import *
from PIL import Image
import mahotas
import scipy.signal
from skimage import *
Im= array(Image.open("cameraman.tif"))
subplot(1,2,1);imshow(Im,cmap='gray')
subplot(1,2,2);imshow(Im,cmap='pink')

C= plt.cm.pink
Im2 = C(Im)

figure()
imshow(Im2)
show()
