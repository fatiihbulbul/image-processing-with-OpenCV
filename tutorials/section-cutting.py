import cv2
import numpy as np

image= cv2.imread("images/scooby.jpg")

cut= image[50:150,100:200] #spacing for cutting ,(y-axis, x-axis)
image[0:100,0:100]= cut

cv2.imshow("Scooby Doo",image)
cv2.imshow("Scooby Cut",cut)



cv2.waitKey(0)
cv2.destroyAllWindows() 