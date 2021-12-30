from skimage.feature import hog
from sklearn.neural_network import MLPClassifier
from skimage.io import imread, imshow
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os
import glob
import pickle

IMG_SHAPE = (250, 100)

def loadData(dataPath, isPositive = True):
    X = []; labels = []

    files = glob.glob(os.path.join(dataPath, "*.png"))
    for file in files:
        img = imread(file, as_gray=True)
        img = resize(img, IMG_SHAPE)
        feat = hog(img, feature_vector=True)

        X.append(feat)
        labels.append(1 if isPositive else 0)

    return X, labels

def main():
    print("Loading and preparing dataset....")
    posX, posLabels = loadData("dataset/ped/",    True)
    negX, negLabels = loadData("dataset/no_ped/", False)
    X = [*posX, *negX]; labels = [*posLabels, *negLabels]

    xTrain, xTest, yTrain, yTest = train_test_split(X, labels, test_size=0.15, shuffle=True, random_state=0)

    print("Training....")
    model = MLPClassifier(hidden_layer_sizes=(256, 128, 64, 32, 16), batch_size=16)
    model.fit(xTrain, yTrain)

    print("Testing....")
    yPred = model.predict(xTest)
    print(classification_report(yTest, yPred))

    print("Saving model...")
    with open('model.pkl', 'wb') as fid:
        pickle.dump(model, fid)    

if __name__ == "__main__":
    main()
