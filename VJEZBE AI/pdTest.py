from skimage.feature import hog
from skimage.transform import pyramid_gaussian
from skimage.io import imread, imshow
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage.draw import rectangle_perimeter
import numpy as np
from matplotlib import pyplot as plt
import pickle
from pdTrain import IMG_SHAPE
from nms import clusterDetections

def drawDetection(img, detection, color, thickness = 1):
    for t in range(0, thickness):
        x, y, w, h, _ = detection
        rr, cc = rectangle_perimeter((y-t, x-t), extent=(h+2*t, w+2*t), shape=img.shape)
        img[rr, cc, :] = color


def slidingWindowDetection(model, img):
    stepSize = 5
    downscale = 1.5

    scale = 0
    detections = []

    print("Sliding window detection...")
    for imgResized in pyramid_gaussian(img, downscale=downscale):
        print(f"\t Checking im of {imgResized.shape[::-1]}...")

        for r in range(0, imgResized.shape[0], stepSize):
            for c in range(0, imgResized.shape[1], stepSize):

                 patch = imgResized[r:r+IMG_SHAPE[0], c:c+IMG_SHAPE[1]]
                 if patch.shape[0] != IMG_SHAPE[0] or patch.shape[1] != IMG_SHAPE[1]:
                    continue

                 feat = hog(patch, feature_vector=True)
                 probs = model.predict_proba([feat]).squeeze()
                 if np.argmax(probs) != 1: 
                     continue

                 mulF = downscale ** scale
                 d = [int(c * mulF), int(r * mulF), int(IMG_SHAPE[1] * mulF), int(IMG_SHAPE[0] * mulF), probs[1]] #x, y, w, h, prob
                 detections.append(d)
                 
        scale += 1
    
    return detections


def main():
    with open('model.pkl', 'rb') as fid:
        model = pickle.load(fid)

    img = imread("dataset/test_img.png")
    detections = slidingWindowDetection(model, rgb2gray(img)) 
    for d in detections:
        drawDetection(img, d, (255, 255, 0))

    rDetections = clusterDetections(detections, 30)
    for rd in rDetections:
        drawDetection(img, rd, (255, 0, 0), 5)

    imshow(img)
    plt.show()
    print("done")


if __name__ == "__main__":
    main()
