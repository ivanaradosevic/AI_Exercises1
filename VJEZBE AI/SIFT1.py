import cv2
import numpy as np

MIN_MATCH_COUNT=5   #KONFIG FAJLOVI KOJI BI TREBALI BITI U POSEBNOM FAJLU, AKO NISU ONDA CAPS LOC

image=cv2.imread("knjiga_naslovnica.png", cv2.IMREAD_GRAYSCALE)
image2=cv2.imread("knjige.png", cv2.IMREAD_GRAYSCALE)

sift=cv2.SIFT_create()  #ako hocu drugu sliku samo 2 stavim, za image2
kp1, desc1=sift.detectAndCompute(image,None)
kp2, desc2=sift.detectAndCompute(image2,None)
image_keypoints=cv2.drawKeypoints(image, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
image_keypoints2=cv2.drawKeypoints(image2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("keypoints", image_keypoints)
cv2.imshow("keypoints2", image_keypoints2)
matcher=cv2.BFMatcher()
matches=matcher.knnMatch(desc1, desc2, k=2)
img_matches=cv2.drawMatchesKnn(image, kp1, image2, kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

#cv2.imshow("matches", img_matches)

good_matches=[]
for m,n in matches:
    if m.distance <0.7* n.distance:   #n nam je drugi najbolji, kao referenca za odbacivanje loših, jer je k=2
        good_matches.append(m)         #m i n su objekti
#img_matches=cv2.drawMatchesKnn(image, kp1, image2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
#cv2.imshow("matches", img_matches)
if len(good_matches)>MIN_MATCH_COUNT:
    src_points=np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    M, _ =cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)
    h,w=image.shape
    pts=np.float32([[0,0],[w-1, 0], [w-1, h-1], [0,h-1]]).reshape(-1,1,2)
    dst=cv2.perspectiveTransform(pts, M)
    img_detection=cv2.polylines(image2, [np.int32(dst)],True, 255,2)
    cv2.imshow("detection", img_detection)

cv2.waitKey()
cv2.destroyAllWindows()




cv2.imshow("image",image)
