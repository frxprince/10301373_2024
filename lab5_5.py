from pylab import *
import mahotas
from PIL import Image
import scipy.signal
Im=mahotas.colors.rgb2gray(array(Image.open('coins.jpg')))
G= ones((9,9),dtype=int)/(9*9)
ImLowpass= scipy.signal.convolve2d(Im,G)
Ims=ImLowpass < 200


#imshow(Ims,cmap='gray')
#show()




patch=3
L,n = mahotas.label(Ims,ones((3,3),dtype=int))
plt,ax=subplots(1,2)
ax[0].imshow(Im,cmap='gray')
for i in range( 1,n+1):
    r,c=where(L==i)
    y1=min(r);y2=max(r);x1=min(c);x2=max(c)
    ov=Rectangle((x1,y1),x2-x1,y2-y1,linewidth=1,
                 edgecolor='r',facecolor='none')
    ax[0].text(x1,y1,str(i),color='g')
    ax[0].add_patch(ov)
    subImg=Im[y1-patch:y2+patch,x1-patch:x2+patch]
    ax[1].imshow(subImg,cmap='gray')
    show(block=False)
    pause(1)
    
   


