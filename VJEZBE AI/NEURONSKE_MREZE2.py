import numpy as np
import os
import  cv2
from skimage.feature import hog
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

#istrenirani klasifikator i sada cemo ga iskoristiti za detekciju pjesaka metodom kliznog prozora
#krecemo od lijevog kuta, izrezat, pmaknut za 5 pik. u desno, pamtiti vjerojatnosti i tocke, top left...




dataset_path="dataset"
mean_image_width=101
mean_image_height=264
def load_ped_dataset(images_folder):

    ped_image_dataset= os.path.join(dataset_path, images_folder) #cilj funkcije je da vrati pedestrian znacajke, za svaku sliku

    pedestrian_hog_list=[]
    for file in os.listdir(ped_image_dataset):
        if file.endswith('.png'):

            image_name=os.path.join(ped_image_dataset,file)   #/pad/ime slike
            image_ped=cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
            image_ped=cv2.resize(image_ped,(mean_image_width, mean_image_height))

            HOG_desc,hog_image= hog(image_ped,visualize=True)
            #fig,axes=plt.subplots(1,2)
            #axes[0].imshow(image_ped,cmap="gray")
            #axes[1].imshow(hog_image,cmap="gray")
            #plt.show()

            pedestrian_hog_list.append(HOG_desc)

    pedestrian_hog_list=np.array(pedestrian_hog_list)
    return pedestrian_hog_list

ped_dataset=load_ped_dataset('ped')
no_ped_dataset=load_ped_dataset('no_ped')

pedestrian_labels= np.ones(ped_dataset.shape[0])
no_pedestrian_labels=np.zeros(no_ped_dataset.shape[0])

X= np.concatenate((ped_dataset, no_ped_dataset))
y= np.concatenate((pedestrian_labels, no_pedestrian_labels))

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2)
classifier=MLPClassifier(random_state=1)
classifier.fit(X_train, y_train)
#score=classifier.score(X_test, y_test)
#print(score)

test_image= cv2.imread("dataset/test_img.png",cv2.IMREAD_GRAYSCALE)
image_height=test_image.shape[0]
image_width=test_image.shape[1]

max_pedestrian_probability=0
final_top_left_bb=(0,0)
final_bottom_right=(0,0)
for i in range(0, image_height-mean_image_height-1, 10):
    for j in range(0, image_width-mean_image_width-1,10):
        roi= test_image[i: i + mean_image_height, j: j + mean_image_width]
        HOG_desc, HOG_image=hog(roi, visualize=True)
        HOG_desc=HOG_desc.reshape((1, -1))
        roi_probabilities=classifier.predict_proba(HOG_desc)
        pedestrian_probability=roi_probabilities[0,1]#pedestrian smo oznacili kao 1, non pedestrian kao 0
        if pedestrian_probability>max_pedestrian_probability:
            max_pedestrian_probability=pedestrian_probability
            final_top_left_bb=(j,i)
            final_bottom_right=(j+mean_image_width, i + mean_image_height)
detection_image=cv2.rectangle(test_image, final_top_left_bb, final_bottom_right,255, thickness=3)
cv2.imshow("detection", detection_image)
cv2.waitKey()
cv2.destroyAllWindows()







print("done")
