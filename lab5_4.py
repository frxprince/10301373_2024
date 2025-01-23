## Demostration of Otsu thresholding algorithm
## Original version
## Writen by Dr.Paween Khoenkaw http://www.drpaween.com
from pylab import *
import mahotas
from PIL import Image
Im=mahotas.colors.rgb2gray(array(Image.open('otsu1.jpg')))
levels=16;
Im=( ceil((Im/255.0)*(levels-1) )).astype(uint8);
F,I=histogram(Im,bins=linspace(0,levels,levels+1))
pixels=sum(F)
wB=0
wF=0
minimal=9999999
threshold=0.0
subplot(2,2,1)
imshow(Im,cmap='gray')
title('Original')
print("Bin\tweightB\tweightF\tmeanB \tmeanF \tvarB \tvarF \twithInVar\tMinimalBin")
for i in range(0,levels):
    wB=wB+F[i]    
    if(wB==0):
        continue
    wF=pixels-wB    
    if(wF==0):
        break
    Bx=F[0:i+1]
    Fx=F[i+1:levels]    
    BgIndex=linspace(0,i,i+1).astype(int)
    FgIndex=linspace(i+1,levels-1,levels-i-1).astype(int)
    weightB=sum(Bx)/pixels
    weightF=sum(Fx)/pixels
    meanB=sum(Bx*BgIndex)/(sum(Bx))  
    meanF=sum(Fx*FgIndex)/(sum(Fx))
    varB=sum(((BgIndex-meanB)**2)*Bx)/sum(Bx)
    varF=sum(((FgIndex-meanF)**2)*Fx)/sum(Fx)
    withInVar=(weightB*varB)+(weightF*varF)
    if(withInVar < minimal):
        threshold=i
        minimal=withInVar
    print("%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t\t%d"%(i,weightB,weightF,meanB,meanF,varB,varF,withInVar,threshold))

    xx=subplot(2,2,2)
    cla()
    bar(BgIndex,Bx,color='blue')
    bar(FgIndex,Fx,color='green')
    text(threshold,mean(F),'X',color='red')
    title('Histogram and algorithm progress')
    show(block=False)
    subplot(2,2,3)
    imshow(Im>i,cmap='gray')
    title('Current threshold')
    subplot(2,2,4)
    imshow(Im>threshold,cmap='gray')
    title('Best threshold discovered so far')
    pause(0.1)


