from pylab import *
from PIL import Image
import mahotas
import easygui as ui
fname=ui.fileopenbox(filetypes=['*.jpg','*.png','*.tiff'],default='*.jpg')
Im=array(Image.open(fname))
ImGray= mahotas.colors.rgb2gray(Im)
subplot(1,2,1);imshow(ImGray,cmap='gray',vmin=0,vmax=255)

ImAvg=floor(mean(ImGray))
bias=ImAvg-127
ImAdj=ImGray-bias

subplot(1,2,2);imshow(ImAdj,cmap='gray',vmin=0,vmax=255)
show()
