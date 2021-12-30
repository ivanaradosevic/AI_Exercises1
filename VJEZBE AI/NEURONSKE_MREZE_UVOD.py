import numpy as np
import os
import  cv2
from skimage.feature import hog
import matplotlib.pyplot as plt
import numpy as np


dataset_path="dataset"
mean_image_width=101
mean_image_height=264
def load_ped_dataset():
    ped_image_dataset= os.path.join(dataset_path, "ped") #cilj funkcije je da vrati pedestrian znacajke, za svaku sliku

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
ped_dataset=load_ped_dataset()

print("done")
