from pylab import *
from PIL import Image
from PIL import ImageOps
import mahotas
import scipy.signal

Im= mahotas.colors.rgb2gray((array(Image.open('Valve_original_.png'))))
Gv=array([[-1, 1],[-1, 1]])
ImEdgeV= scipy.signal.convolve2d(Im,Gv)

subplot(1,4,1);imshow(Im,cmap='gray')
subplot(1,4,2);imshow(ImEdgeV,cmap='gray',vmin=0,vmax=255)

Gh= Gv.T
ImEdgeH= scipy.signal.convolve2d(Im,Gh)
subplot(1,4,3);imshow(ImEdgeH,cmap='gray',vmin=0,vmax=255)
ImEdge=abs(ImEdgeV+ImEdgeH)
subplot(1,4,4);imshow(ImEdge,cmap='gray',vmin=0,vmax=255)
ImEdgeBin=ImEdge>20
figure(2)
imshow(ImEdgeBin,cmap='gray')

show()

