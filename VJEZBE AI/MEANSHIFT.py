import cv2
import numpy as np

capture=cv2.VideoCapture("car_meanshift.mp4")
if not capture.isOpened():
    print("cannot open")
    exit(1)

backSub= cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame=capture.read()  #čitanje slike po slike
    binarna=backSub.apply(frame)
    bez_suma=cv2.morphologyEx(binarna, cv2.MORPH_OPEN,(5,5))  #erozija i dilatacija
    kernel=np.ones((5,5),np.uint8)
    if frame is  None:
        break
    cv2.imshow("frame", frame)
    cv2.imshow("binarna", binarna)
    cv2.imshow("bez suma",bez_suma)
    if cv2.waitKey(1)==113: #koliko brzo želimo brzo da učita video i 113 za slovo q po ascii da izađemo iz petlje
        break 
capture.release()
cv2.destroyAllWindows()



