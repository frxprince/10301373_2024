from pylab import *
from PIL import Image
import mahotas

Im= array(Image.open('lena512color.tiff'))
ImGray=    mahotas.colors.rgb2gray(Im)
ImAvg=floor(mean(ImGray))
print('The pixel average value is ',ImAvg)

  
