import cv2
import numpy as np

capture=cv2.VideoCapture("dashcam_video.mp4")
if not capture.isOpened():
    print("cannot open")
    exit(1)

ret,frame=capture.read()
cv2.imwrite("frame.jpg", frame)

x,y,w,h=390,298,140,128
track_window=(x,y,w,h)
roi=frame[y:y+h,x:x+w,:]
roi_hsv=cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
read_lower=np.array([100,20,20])
read_upper=np.array([130,80,200])
mask=cv2.inRange(roi_hsv, read_lower, read_upper)

roi_hist=cv2.calcHist([roi_hsv], [0], mask, [180], [0,180])


#funkc.vjerojatnosti
roi_hist=cv2.normalize(roi_hist, None, 0, 255, cv2.NORM_MINMAX) #radi vizualizacije, uzet cemo histogram i raditi back projectons
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
    #cv2.imshow("backproj", dst)
    if cv2.waitKey(1)==113:
        break

capture.release()
cv2.destroyAllWindows()




