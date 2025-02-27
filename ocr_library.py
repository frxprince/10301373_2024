from PIL import Image
import pytesseract
from pylab import *
Im=array(Image.open('ocr_test_image/syn2.bmp'))
texts=pytesseract.image_to_string(Im,lang='tha+eng')
print(texts)

boxes=pytesseract.image_to_boxes(Im,lang='tha+eng')
fig=figure()
ax=fig.subplots()
h,w,d=Im.shape

imshow(Im);
for box in boxes.splitlines():
    p=box.split(' ')
    print(box)
    if(len(p)>3):
        a=p[0]
        if(a != '~'):
            x=int(p[1]);y=int(p[2]);w1=int(p[3])-x;h1=int(p[4])-y
            rec=Rectangle((x,h-y-h1),w1,h1,facecolor='none',edgecolor='red')
            text(x,h-y-h1,a,color='green',fontsize=20)
            print(a)
            ax.add_patch(rec)

show()
