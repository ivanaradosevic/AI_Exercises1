import cv2
import numpy as np

capture=cv2.VideoCapture("car_meanshift.mp4")
if not capture.isOpened():
    print("cannot open")
    exit(1)

ret,frame=capture.read()

x,y,w,h=223,202,34,20
track_window=(x,y,w,h)
roi=frame[y:y+h,x:x+w,:]
roi_hsv=cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
read_lower=np.array([170,50,50])
read_upper=np.array([180, 255,255])
mask=cv2.inRange(roi_hsv, read_lower, read_upper)
def new_func(roi_hsv, mask):
    roi_hist=cv2.calcHist([roi_hsv], [0], mask, [180], [0,180])  # prva vrijednost koliko binova, druga range od 0,180
    return roi_hist  # ako stavim 10 onda u debageru vidim manji histogram boja

roi_hist = new_func(roi_hsv, mask)
#funkc.vjerojatnosti
cv2.normalize(roi_hist, None, 0, 255, cv2.NORM_MINMAX) #radi vizualizacije, uzet cemo histogram i raditi back projectons
criteria=(cv2.TermCriteria_EPS | cv2.TERM_CRITERIA_COUNT,10,1)
while True:
    ret, frame=capture.read()  #čitanje slike po slike

    if frame is  None:
        break

    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dst=cv2.calcBackProject([hsv_frame],[0], roi_hist, [0,180], 1)
    _, track_window=cv2.meanShift(dst,track_window,criteria)
    x,y,w,h=track_window
    tracking_img=cv2.rectangle(frame, (x,y), (x+w,y+h),[255,0,0])
    cv2.imshow("tracking", tracking_img)
    cv2.imshow("backproj", dst)
    if cv2.waitKey(1)==113:
        break





capture.release()
cv2.destroyAllWindows()


#backSub= cv2.createBackgroundSubtractorMOG2()




# while True:
#     ret, frame=capture.read()  #čitanje slike po slike
#     binarna=backSub.apply(frame)
#     bez_suma=cv2.morphologyEx(binarna, cv2.MORPH_OPEN,(5,5))  #erozija i dilatacija
#     kernel=np.ones((5,5),np.uint8)
#     if frame is  None:
#         break
    # cv2.imshow("frame", frame)
    # cv2.imshow("binarna", binarna)
    # cv2.imshow("bez suma",bez_suma)
    # if cv2.waitKey(1)==113: #koliko brzo želimo brzo da učita video i 113 za slovo q po ascii da izađemo iz petlje
    #     break 
#capture.release()
cv2.destroyAllWindows()
