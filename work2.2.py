import cv2
import argparse
import numpy as np
import imutils

def task2():
    path = 'C:/Users/Abdul Bari Rasuly/Desktop/Image/'

    def set_image(image):
        return cv2.imread(path + image)
    
    def result_search():
        for i in range(1, 11):
            image = set_image('image.jpg')
            
            fragment = set_image(f'Et_{i}.jpg')
            
            (fragmentHeight, fragmentWidth) = fragment.shape[:2]
            # Search for a fragment in the image
            result = cv2.matchTemplate(image, fragment, cv2.TM_CCOEFF)
            (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
            # Select the desired fragment and separate it from the image
            topLeft = maxLoc
            botRight = (topLeft[0] + fragmentWidth, topLeft[1] + fragmentHeight)
            roi = image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
            # Create a darkened transparent layer 
            mask = np.zeros(image.shape, dtype="uint8")
            image = cv2.addWeighted(image, 0.20, mask, 0.75, 0)
            # Return the desired fragment
            image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
            # Display fragment and image 
            cv2.imshow(f"Image{i}", imutils.resize(image, height=900))
            cv2.imshow(f"Et_{i}", fragment)
            cv2.waitKey(0)

            #path_result = '/result/'
            cv2.imwrite("C:/Users/Abdul Bari Rasuly/Desktop/Image/result/result_search/{i}.jpg", image)
            
    result_search()

task2()