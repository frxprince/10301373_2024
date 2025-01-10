from PIL import Image
import mahotas
from pylab import *

Im=array(Image.open('lena512color.tiff'))
Im_small= array(Image.open('small.jpg'))
ImGray=mahotas.colors.rgb2gray(Im)
h,w=Im_small.shape

#ImGray[0:h,0:w]=Im_small
#imshow(ImGray,cmap='gray')

Im[0:h,0:w,0]=Im_small;Im[0:h,0:w,1]=Im_small;Im[0:h,0:w,2]=Im_small
imshow(Im)
show()
ImPil=Image.fromarray(Im)
ImPil.save('lab1.jpg')
