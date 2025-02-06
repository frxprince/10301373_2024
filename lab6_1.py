from pylab import *
from PIL import Image

Im= array(Image.open("frontier_color57.jpg"))
R=Im[:,:,0]
G=Im[:,:,1]
B=Im[:,:,2]

R2 =clip( 0.393*R + 0.769*G + 0.189*B,0,255)
G2 =clip( 0.349*R + 0.686*G + 0.168*B,0,255)
B2 =clip( 0.272*R + 0.534*G + 0.131*B,0,255)
#Im2=Im.copy()
#Im2[:,:,0]=clip(R2,0,255)
#Im2[:,:,1]=clip(G2,0,255)
#Im2[:,:,2]=clip(B2,0,255)
Im2=uint8(dstack((R2,G2,B2)))
subplot(1,2,1);imshow(Im)
subplot(1,2,2);imshow(Im2)
show()
