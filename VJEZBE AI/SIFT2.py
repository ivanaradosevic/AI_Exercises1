import cv2
import numpy as np

capture=cv2.VideoCapture("dashcam_video.mp4")
if not capture.isOpened():
    print("cannot open")
    exit(1)

ret,frame=capture.read()

MIN_MATCH_COUNT=5
image=cv2.imread("car.png", cv2.IMREAD_GRAYSCALE)
image2=cv2.imread("frame.jpg", cv2.IMREAD_GRAYSCALE)
sift=cv2.SIFT_create()  #ako hocu drugu sliku samo 2 stavim, za image2
kp1, desc1=sift.detectAndCompute(image,None)

kp2, desc2=sift.detectAndCompute(image2,None)

matcher=cv2.BFMatcher()
matches=matcher.knnMatch(desc1, desc2, k=2)
img_matches=cv2.drawMatchesKnn(image, kp1, image2, kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

good_matches=[]
for m,n in matches:
    if m.distance <0.7* n.distance:   #n nam je drugi najbolji, kao referenca za odbacivanje loših, jer je k=2
        good_matches.append(m)

if len(good_matches)>MIN_MATCH_COUNT:
    src_points=np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    M, _ =cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)
h,w=image.shape
pts=np.float32([[0,0],[w-1, 0], [w-1, h-1], [0,h-1]]).reshape(-1,1,2)
dst=cv2.perspectiveTransform(pts, M)
print(dst)
img_detection=cv2.polylines(image2, [np.int32(dst)],True, 255,2)
cv2.imshow("detection", img_detection)



capture.release()

cv2.waitKey()
cv2.destroyAllWindows()



