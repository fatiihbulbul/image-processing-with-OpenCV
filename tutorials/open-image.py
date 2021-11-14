import cv2
import numpy as np

image= cv2.imread("images/nature.jpeg")
cv2.imshow("Nature Photo",image)
"""
print(image) #matrix state
print(image.size) #total size
print(image.dtype) #data type
print(image.shape) #rows (height), columns (width), and channels (bgr)
print(image[(240,20)]) #pixel's bgr values (blue, green, red)
"""
print("The size of the picture: "+str(image.size))
print("Data type of image: "+str(image.dtype))
print("Features of the picture: "+str(image.shape))

cv2.waitKey(0)
cv2.destroyAllWindows() 