import cv2
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

img_color = cv2.imread('flower.jpg', cv2.IMREAD_COLOR)
img_grayscale = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)

print(type(img_grayscale))
print(img_grayscale.shape)

THRESH = 127
img_binary_data = cv2.threshold(img_grayscale, THRESH, 255, cv2.THRESH_BINARY)
img_binary = img_binary_data[1]

print(type(img_binary))

# plt.imshow(img_grayscale)
# plt.show()
# cv2.imshow("binary", img_binary)
# cv2.waitKey(0)

# plt.hist(img_binary.ravel(), bins=20)
# plt.show()

# Initial Array

# x = np.array([1, 2, 3, -1, 5])

# indexes = np.where(img_binary==0)
# img_grayscale(indexes)=0
#
#
# mx = ma.masked_array(img_grayscale, mask=img_binary)
# print(type(mx))
# cv2.imshow("mx", mx)
# cv2.waitKey(0)
# cv2.imshow("img_binary", img_binary)
# cv2.waitKey(0)


mask = np.array([[1, 0, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 0, 1],
                 [1, 1, 1, 1]])

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("Initial Array: ")
print(arr)

backgrounIndexes = np.where(img_binary == 0)
imgBlue = img_color[:, :, 0]
imgGreen = img_color[:, :, 1]
imgRed = img_color[:, :, 2]

imgBlue[backgrounIndexes] = 0
imgGreen[backgrounIndexes] = 0
imgRed[backgrounIndexes] = 0

img_color_masked = img_color.copy()
img_color_masked[:, :, 0] = imgBlue
img_color_masked[:, :, 1] = imgGreen
img_color_masked[:, :, 2] = imgRed

cv2.imshow("img_color_masked", img_color_masked)
cv2.waitKey(0)

# print()
# print("result[0]: ")
# print(result[0])
#
# print()
# print("result[1]: ")
# print(result[1])
#
# print()
# print("result: ")
# print(result)
