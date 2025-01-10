from pylab import *
from PIL import Image
import mahotas

Im= array(Image.open('frontier_color57.jpg'))
ImGray=    mahotas.colors.rgb2gray(Im)
h,w=ImGray.shape
width=int((w/4))
x2=int(floor(w/4))
ImGray[:,x2:x2+width]=clip(ImGray[:,x2:x2+width]-50,0,255)
c=-50
f=(259*(c+255))/(255*(259-c))
x3=int(x2+width)
ImGray[:,x3:x3+width]=clip(((ImGray[:,x3:x3+width]-128)*f)+128,0,255)
x4=int(x3+width)
g=2
ImGray[:,x4:w]=((ImGray[:,x4:w]/255)**g)*255
imshow(ImGray,cmap='gray')
show()

  
