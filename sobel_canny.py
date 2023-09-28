'''
In this problem, you will detect edges in an image by two methods:
(1) Write your own Sobel filtering code in Python to detect edges, and
(2) Use the Canny edge detector in OpenCV to detect edges.

Either way, take as input the color images, “cheerios,” “professor,” “gear,” and “circuit,” shown in Figure 2,
and convert them to binary images showing edges in black on a white background.

The inner workings of the Canny edge detector are explained in the 9/22 lecture. They are also explained
in the appendix placed at the end of this document.

Since the Canny results change significantly depending on specified parameters (threshold1, threshold2,
apertureSize, and L2gradient), use some GUIs such as slider bars and radio buttons to allow a user to
iteratively change and apply a different combination of parameters and see the result on the screen. Use
your program to find the best combination of parameters for each of the four images.

For each image, compare and discuss the results of the Sobel filtering and the Canny edge detection.

'''

import cv2
import os
import numpy as np


sobel_h_kern = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_v_kern = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

def sobel(img):
    graysc =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_h = cv2.filter2D(graysc, -1, sobel_h_kern)
    sobel_v = cv2.filter2D(graysc, -1, sobel_v_kern)
    img_out = sobel_h + sobel_v
    return img_out


# get file input
print("Greetings! What photo would you like to edit? Your options are: ")
for file_names in os.listdir():
    if file_names.endswith(".png") or file_names.endswith(".jpg"):
        print("\t" + file_names)
input_file = input("\n input file: ")
img = cv2.imread(input_file)

# extracting extension and file base name
extension = input_file[-4:]
input_file = input_file[:-4]


# sobel filter
sobel_img = sobel(img)


cv2.namedWindow("input", cv2.WINDOW_NORMAL )
cv2.namedWindow("sobel", cv2.WINDOW_NORMAL )
# cv2.namedWindow("canny", cv2.WINDOW_NORMAL )

cv2.imshow("input", img)
cv2.imshow("sobel", sobel_img)
# cv2.imshow("canny", canny_img)


# cv2.imwrite(input_file+"-sobel"+extension, sobel_img)
# cv2.imwrite(input_file+"-canny"+extension, canny_img)

cv2.waitKey(0)
cv2.destroyAllWindows()