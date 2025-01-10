from pylab import *
from PIL import Image
import mahotas

Im=   array(Image.open('lena512color.tiff'))
ImGray=mahotas.colors.rgb2gray(Im)
F,I= histogram(ImGray,range(0,255))
#F,I= histogram(ImGray,bins=10)
F_cumsum=cumsum(F)
subplot(1,2,1);bar(I[0:len(I)-1],F)
subplot(1,2,2);bar(I[0:len(I)-1],F_cumsum)
show()

