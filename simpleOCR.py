from pylab import *
from PIL import Image
import skimage
import mahotas
from pylab import *
import mahotas
from scipy import ndimage
from PIL import Image
import sys
Im_original=  mahotas.colors.rgb2gray(array(Image.open('ocr_test_image/syn2.bmp'))).astype(float)
Im_template=  mahotas.colors.rgb2gray(array(Image.open('ocr_test_image/syn0.bmp'))).astype(float)
Im_original=Im_original+1
#Im= ndimage.rotate(Im_original,5)
Im=Im_original.copy()
Im[Im==0]=255
Im=Im-1

#--- load template -----
T=[]
ImTemplateB=transpose(Im_template<100)
L, n=mahotas.label(ImTemplateB,ones((3,3),dtype=int))
fig=figure()
fig2=figure()
bx=fig2.subplots(2,2)
bx[0,0].imshow(Im_template,cmap='gray')
for i in range(1,n+1):
    r,c=where(L==i)
    Tc=ImTemplateB[r.min():r.max(), c.min():c.max()]
    bx[0,1].cla()
    bx[0,1].imshow(transpose(Tc),cmap='gray')
    T.append(Tc)
    fig2.show()
    pause(0.00001)
#sys.exit(0)
#---- image alignment -------    
ax=fig.subplots(2,2)
h,w=Im.shape
ImE=Im<200#abs(ndimage.sobel(Im[round(.1*h):round(.9*h),round(.1*w):round(.9*w)]))
ax[0,0].imshow(Im,cmap='gray',vmin=0,vmax=255)
maxBlank=-1;degree=0
for i in range(-10,10):
    ImT=ndimage.rotate(ImE,i,reshape=False)
    h,w=ImT.shape
    Px=sum(ImT,1)
    r=where(Px <10)
    if(r[0].shape[0] > maxBlank):
        maxBlank=r[0].shape[0]
        degree=i
    ax[0,1].cla()    
    ax[0,1].imshow(ImT,cmap='gray',vmin=0,vmax=ImT.max())
    ax[0,1].plot((Px/Px.max())*100,range(0,h))
    fig.show()
    pause(0.0001)
Im=Im+1
Im_aligned= array(Image.fromarray(Im).rotate(degree,resample=Image.BICUBIC ))
Im_aligned[Im_aligned==0]=255
Im_aligned=Im_aligned-1
ImB=Im_aligned <200;
ax[1,0].imshow(ImB,cmap='gray',vmin=0,vmax=1)
fig.show()
#------- line segmentation -------
Px=sum(ImB,1)
h,w=ImB.shape
ax[1,0].plot((Px/Px.max())*100,range(0,h))
fig.show()
Lines=Px >10
L,n=mahotas.label(Lines)
for i in range(1,n+1):
    r=where(L==i)
    y0=min(r[0])-3;y1=max(r[0])+3
    R=Rectangle((1,y0),w-1,y1-y0,edgecolor='red',facecolor='none')
    ax[1,0].add_patch(R)
    ImQ=ImB[y0:y1,1:w-1]
    ax[1,1].cla()
    ax[1,1].imshow(transpose(ImQ),cmap='gray')
    fig.show()
    Lq,nq=mahotas.label(transpose(ImQ),ones((3,3),dtype=int))
    for j in range(1,nq+1):
        #------ charactor segmentation -
        R,C=where(Lq==j)
        minDist=9999
        digit=0;k=0
        R2=Rectangle((C.min(),R.min()),C.max()-C.min(),R.max()-R.min(),edgecolor='red',facecolor='none')
        ax[1,1].add_patch(R2)
        Qcroped=transpose(ImQ)[R.min():R.max(), C.min():C.max()]
        bx[1,0].cla();
        bx[1,0].imshow(transpose(Qcroped),cmap='gray')
        fig.show();fig2.show()
        #------ template matching ------
        if((sum(Qcroped)>10)):
            for t in T:
                k=k+1
                ht,wt=t.shape
                Qs= mahotas.imresize(Qcroped,(ht ,wt))
                hq,wq=Qs.shape
                d=(sum(sqrt((Qs -  t[0:hq,0:wq])**2)))
                if(minDist>d):
                    minDist=d
                    digit=k-1
                bx[1,1].cla()
                bx[1,1].imshow(transpose(t),cmap='gray')
                fig2.show()
                pause(0.000001)
        if(minDist<1500):
            print(digit,minDist)
        else:
            print("?",minDist)

    print("--- end of line---")
    pause(0.00005);
    
                

