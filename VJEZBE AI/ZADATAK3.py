# 3.Pomoću Houghove transformacije detektirajte i nacrtajte pravce na slici “puna_linija_desno.jpg”.
# Među detektiranim pravcima mora biti samo desna puna linija.
# Izmijenite kôd tako da se među detektiranim linijama također nalaze i isprekidane linije
# autoceste.

import cv2
import numpy as np


slika=cv2.imread('puna_linija_desno.jpg')  #originalna slika
gray=cv2.cvtColor(slika,cv2.COLOR_BGR2GRAY)
#gray= cv2.GaussianBlur(gray,(5,5),1)
mask= np.zeros_like(gray)
canny=cv2.Canny(gray,150,300)   
height, width=gray.shape
x1=0
y1=330
x2=550
y2=330
x3=width
y3=height
x4=0
y4=height
roi= np.array([[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]]) 
maska=cv2.fillPoly(mask,roi,(255,255,255))  
maskirana=cv2.bitwise_and(canny, maska)  


linije=cv2.HoughLinesP(maskirana,1,np.pi/180,50,minLineLength=60,maxLineGap=200)      


for line in linije:
    for x1,y1,x2,y2 in line:
        cv2.line(slika,(x1,y1),(x2,y2),(255,0,0),2) #za crtanje linija, boje plave
  

cv2.imshow('maskirana',maskirana)
cv2.imshow('slika',slika)
cv2.imshow("maska", maska)
cv2.imshow("keni", canny)
cv2.waitKey()
cv2.destroyAllWindows()
