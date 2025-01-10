from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas

ImGray=uint8(mahotas.colors.rgb2gray(array(Image.open('frontier_color57.jpg '))))
h,i= histogram(ImGray,bins=10)
subplot(1,2,1);bar(i[0:len(i)-1],h)
h_norm= h/max(h)
#imshow(ImGray)
subplot(1,2,2);bar(i[0:len(i)-1],h_norm,color='red')
show()

