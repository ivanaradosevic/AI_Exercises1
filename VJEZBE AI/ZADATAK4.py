#Pomoću Houghove transformacije pokušajte detektirati prometni znak na slici “kamera4.png”

import cv2
import numpy as np



slika=cv2.imread('kamera4.png')  #originalna slika
gray=cv2.cvtColor(slika,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
mask= np.zeros_like(gray)   
height, width=gray.shape
x1=800
y1=0
x2=width
y2=0
x3=width
y3=260
x4=800
y4=260
roi= np.array([[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]]) 
maska=cv2.fillPoly(mask,roi,(255,255,255))  
maskirana=cv2.bitwise_and(gray, maska)  


 
krug=cv2.HoughCircles(maskirana, cv2.HOUGH_GRADIENT,1,10)
print(krug)
krug = np.uint16(np.around(krug))

for i in krug[0,:]:
    cv2.circle(slika,(i[0], i[1]),i[2],(255,0,0),3) #3- mijenjam debljinu boje oko kruga
    cv2.circle(slika,(i[0],i[1]),2,(0,255,0),5)


  

cv2.imshow('maskirana',maskirana)
cv2.imshow('slika',slika)
cv2.imshow("maska", maska)
cv2.waitKey()
cv2.destroyAllWindows()
