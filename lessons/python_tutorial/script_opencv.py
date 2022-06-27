import cv2
import matplotlib.pyplot as plt



img_grayscale = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)



print(type(img_grayscale))
print(img_grayscale.shape)



THRESH = 127
img_binary_data = cv2.threshold(img_grayscale, THRESH, 255, cv2.THRESH_BINARY)
img_binary = img_binary_data[1]
cv2.imshow("binary", img_binary)
cv2.waitKey(0)

#plt.hist(img_binary.ravel(), bins=20)
#plt.show()
