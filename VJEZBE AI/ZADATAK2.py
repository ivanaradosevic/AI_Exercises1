# 2.Primijetite nedostatke prethodnog zadatka. Teško je detektirati samo linije vozne trake bez
# detekcije i ostalih linija na slici. Metodom maskiranja slike, pokušajte izdvojiti samo linije voznih
# traka.

import cv2
import numpy as np


slika=cv2.imread('kamera3.jpeg')  #originalna slika
gray=cv2.cvtColor(slika,cv2.COLOR_BGR2GRAY)
mask= np.zeros_like(gray)
canny=cv2.Canny(gray,150,300)   #canny varijanta grayscalea
height, width=gray.shape
x1=300
y1=290
x2=630
y2=290
x3=width
y3=height
x4=0
y4=height
roi= np.array([[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]]) 
maska=cv2.fillPoly(mask,roi,(255,255,255))  #napravila masku od prazne matrice i roi
maskirana=cv2.bitwise_and(canny, maska)  #lijepim masku na canny sliku


linije=cv2.HoughLinesP(maskirana,1,np.pi/180,100,minLineLength=60,maxLineGap=200)      #detekcija +(tresh.100)
#print(linije)  #ne tražim linije po cijeloj slici nego po maskiranoj


for line in linije:
    for x1,y1,x2,y2 in line:
        cv2.line(slika,(x1,y1),(x2,y2),(255,0,0),2) #za crtanje linija, boje plave
  

cv2.imshow('maskirana',maskirana)
cv2.imshow('slika',slika)
cv2.imshow("maska", maska)
cv2.imshow("keni", canny)
cv2.waitKey()
cv2.destroyAllWindows()


