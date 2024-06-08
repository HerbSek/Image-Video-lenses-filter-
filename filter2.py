import cv2
import numpy as np

img = cv2.imread('Selection_096.png')
height, width = img.shape[:2]
img = cv2.resize(img,(int(width/3), int(height/3)), interpolation=cv2.INTER_AREA)


enhance_array = [
             [-1,-1, -1,-1,-1],
             [-1, 2,  2, 2,-1],
             [-1, 2,  10, 2,-1],
             [-1, 2,  2, 2,-1],
             [-1,-1, -1,-1,-1] 
]  
img_array = np.array(enhance_array) / 9
img_enhance = cv2.filter2D(img, -1 ,img_array)

cv2.imshow('Input', img)
cv2.imshow('Output', img_enhance)
cv2.waitKey()