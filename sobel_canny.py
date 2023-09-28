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

thresh1 = 50
thresh2 = 200
aperture_sz = 3
l2_grad = 0


# get file input
print("Greetings! What photo would you like to edit? Your options are: ")
for file_names in os.listdir():
    if file_names.endswith(".png") or file_names.endswith(".jpg"):
        print("\t" + file_names)
input_file = input("\n input file: ")
img = cv2.imread(input_file)

# creating windows
cv2.namedWindow("input", cv2.WINDOW_NORMAL )
cv2.namedWindow("sobel", cv2.WINDOW_NORMAL )
cv2.namedWindow("canny", cv2.WINDOW_NORMAL )

# extracting extension and file base name
extension = input_file[-4:]
input_file = input_file[:-4]



def sobel(img):
    graysc =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_h = cv2.filter2D(graysc, -1, sobel_h_kern)
    sobel_v = cv2.filter2D(graysc, -1, sobel_v_kern)
    img_out = sobel_h + sobel_v
    return img_out

# sobel filter
sobel_img = sobel(img)
canny_img = img

def fake_cb(val):
    pass


# canny
cv2.createTrackbar('Threshold 1', 'canny', 0, 255, fake_cb )
cv2.createTrackbar('Threshold 2', 'canny', 0, 255, fake_cb )
cv2.createTrackbar('Aperture Size', 'canny', 3, 8, fake_cb )
cv2.createTrackbar('L2 Gradient', 'canny', 0, 1, fake_cb )

cv2.setTrackbarPos('Threshold 1', 'canny', thresh1)
cv2.setTrackbarPos('Threshold 2', 'canny', thresh2)
cv2.setTrackbarPos('Aperture Size', 'canny', aperture_sz)
cv2.setTrackbarPos('L2 Gradient', 'canny', l2_grad)

cv2.imshow("input", img)
cv2.imshow("sobel", sobel_img)

while(True):

    cv2.imshow("canny", canny_img)

    key = cv2.waitKey(1)
    if key == 27: #escape key
        break
    
    thresh1 = min(cv2.getTrackbarPos('Threshold 1', 'canny'), thresh2)
    cv2.setTrackbarPos('Threshold 1', 'canny', thresh1)


    thresh2 = max(cv2.getTrackbarPos('Threshold 2', 'canny'), thresh1)
    cv2.setTrackbarPos('Threshold 2', 'canny', thresh2)

    aperture_sz = cv2.getTrackbarPos('Aperture Size', 'canny')
    if( (aperture_sz%2)==0) :
        aperture_sz = aperture_sz + 1
    if(aperture_sz > 7):
        aperture_sz = 7
    if(aperture_sz < 3):
        aperture_sz = 3
    cv2.setTrackbarPos('Aperture Size', 'canny', aperture_sz)


    l2_grad = cv2.getTrackbarPos('L2 Gradient', 'canny')

    canny_img = cv2.Canny(img,thresh1,thresh2,apertureSize=aperture_sz, L2gradient=l2_grad)



print("Canny settings: ")
print("\t threshold 1: " + str(thresh1))
print("\t threshold 2: " + str(thresh2))
print("\t Aperture: " + str(aperture_sz))
print("\t L2: " + str(l2_grad))

cv2.imwrite(input_file+"-sobel"+extension, sobel_img)
cv2.imwrite(input_file+"-canny"+extension, canny_img)

# cv2.waitKey(0)
cv2.destroyAllWindows()