# 1.Pomoću Houghove transformacije detektirajte i nacrtajte pravce na slici “kamera3.jpeg”. Među
# detektiranim pravcima moraju biti detektirane i linije voznih traka.

import cv2
import numpy as np


import cv2
import numpy as np


slika=cv2.imread('kamera3.jpeg')
gray=cv2.cvtColor(slika,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(7,7),1)
canny=cv2.Canny(gray,150,200)
linije=cv2.HoughLinesP(canny,1,np.pi/180,180,minLineLength=60,maxLineGap=40)      #detekcija
print(linije)


for line in linije:
    for x1,y1,x2,y2 in line:
        cv2.line(slika,(x1,y1),(x2,y2),(255,0,0),2)
#cv2.line(slika,pt1,pt2,color,thickness=5)

cv2.imshow('keni',canny)
cv2.imshow('slika',slika)
cv2.waitKey()
cv2.destroyAllWindows()


