import cv2
import time
from pylab import *
print(cv2.getBuildInformation())


cap= cv2.VideoCapture(0)#("rtsp://admin:csmju123456@172.17.23.73:554/cam/realmonitor?channel=1&subtype=0")
#time.sleep(1)
while(True):
    ret,img=cap.read()
    if(ret==True):
        break
    
while(True):
    ret,img = cap.read()
    #cv2.imshow('hello opencv',img)
    #img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #cla()
    #imshow(img_rgb)
    #show(block=False)
    #pause(1/24)
    cv2.imshow('ip camera',img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cap.release()

