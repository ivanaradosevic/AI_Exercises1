import cv2
import numpy as np

org_slika=cv2.imread("sudoku.jpg")
slika=cv2.cvtColor(org_slika,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(slika,100,200)

lines= cv2.HoughLinesP(canny,1,np.pi/180,200)

print(lines)

#kada dobijem brojeve u terminal, provučem ih kroz for loop, ali ovdje nemam tu sliku sudoku...