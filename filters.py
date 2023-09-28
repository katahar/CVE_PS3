
'''

As discussed in class, the quality of an image can be improved by two types of area-to-pixel filters: (1)
smoothing filters, and (2) sharpening filters. The former will reduce noise in an image, and the latter will
make an image sharper.

In this problem, you are asked to find a smoothing filter, a sharpening filter, or a combination of them that
improves the quality of each of the noisy and/or blurry images shown in Figure 1. Noisy/blurry image are
shown on the left-hand side, and part of their ground truth images are shown on the right-hand side.

Your task is to find a good combination of smoothing and sharpening filters and the order of applying them
to improve each image and make it as close as possible to the ground truth.
You do not need to write your own filters for this problem. Instead, use any OpenCV smoothing functions,
including cv2.blur(), cv2.boxFilter(), cv2.GaussianBlur(), cv2.medianBlur(), cv2.bilateralFilter(). For
sharpening, you may use cv2.filter2D() with a sharpening kernel that you define. You may also create an
“unsharp masking” effect by combining a Gaussian-smoothed image and the original image by using
cv2.addWeighted().

Note to self: be sure to run "conda activate cve" before running this file

'''
import cv2
import os
import numpy as np

def sharpen(img, kernel, k):
    img_out = cv2.filter2D(img, -1, kernel*k )

    return img_out

def sharpen3o(img, k):
    tmp_ortho = sharpen3x3ortho
    tmp_ortho[1][1] = 4
    tmp_ortho = tmp_ortho * k
    tmp_ortho[1][1] = tmp_ortho[1][1]+5
    tmp_ortho = tmp_ortho /5
    img_out = cv2.filter2D(img, -1, tmp_ortho )

    return img_out

def sharpen3a(img, k):
    tmp_ortho = sharpen3x3all
    tmp_ortho[1][1] = 8
    tmp_ortho = tmp_ortho * k
    tmp_ortho[1][1] = tmp_ortho[1][1]+9
    tmp_ortho = tmp_ortho /9
    img_out = cv2.filter2D(img, -1, tmp_ortho )

    return img_out



sharpen3x3ortho = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpen3x3all = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpen5x5 = np.array([[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, 25, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]])
# sharpen5x5a = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])


    

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

# # circuit modifications
new_img = img
finalized_img_blurred = cv2.medianBlur(img,3)
finalized_img = finalized_img_blurred
finalized_img_sharpened = sharpen3o(finalized_img_blurred,5)
finalized_img = finalized_img_sharpened
finalized_img  = cv2.addWeighted(finalized_img_blurred, 0.75, finalized_img_sharpened, 0.25, 0)

# # golf modifications
# new_img = img
# finalized_img_blurred = cv2.medianBlur(cv2.medianBlur(img,3),5)
# finalized_img = finalized_img_blurred
# finalized_img_sharpened = sharpen3o(finalized_img_blurred,5)
# finalized_img = finalized_img_sharpened
# finalized_img = cv2.addWeighted(finalized_img_blurred, 0.75, finalized_img_sharpened, 0.25, 0)


# # pots modifications
# new_img = img
# finalized_img = img
# finalized_img_sharp = sharpen3o(finalized_img,22)

# rainbow modifications
# new_img = img
# finalized_img = img
# finalized_img = cv2.bilateralFilter(img, 20,30,120)


# ------------------
# test_img  = cv2.medianBlur(cv2.medianBlur(img,3),5)
# test_img2 = cv2.medianBlur(img,5)
# test_img3 = cv2.medianBlur(cv2.medianBlur(img,5),3)


# test_img  = cv2.bilateralFilter(img, 20,30,120)
# test_img2 = cv2.bilateralFilter(img, 40,30,120)
# test_img3 = cv2.bilateralFilter(img, 60,30,120)

# test_img  = sharpen3o(finalized_img,1)
# test_img2 = sharpen3o(finalized_img,3)
# test_img3 = sharpen3o(finalized_img,5)

# test_img  = sharpen3a(finalized_img,15)
# test_img2 = sharpen3a(finalized_img,22)
# test_img3 = sharpen3a(finalized_img,30)

# test_img  = sharpen(finalized_img,sharpen3x3ortho,1)
# test_img2 = sharpen(finalized_img,sharpen3x3all,1)
# test_img3 = sharpen3o(finalized_img,2)

# test_img  = sharpen(finalized_img,sharpen3x3ortho,1)
# test_img2 = sharpen(finalized_img,sharpen3x3ortho,1.5)
# test_img3 = sharpen(finalized_img,sharpen5x5,1)

# test_img  = cv2.addWeighted(finalized_img_blurred, 0.75, finalized_img_sharpened, 0.25, 0)
# test_img2 = cv2.addWeighted(finalized_img_blurred, 0.6, finalized_img_sharpened, 0.4, 0)
# test_img3 = cv2.addWeighted(finalized_img_blurred, 0.9, finalized_img_sharpened, 0.1, 0)

cv2.imwrite(input_file+"-improved"+extension, finalized_img)

# creating empty named windows for later population
cv2.namedWindow("input", cv2.WINDOW_NORMAL )
cv2.namedWindow("corrected", cv2.WINDOW_NORMAL )
# cv2.namedWindow("corrected2", cv2.WINDOW_NORMAL )
# cv2.namedWindow("corrected3", cv2.WINDOW_NORMAL )



cv2.imshow("input", img)
# cv2.imshow("input", finalized_img)
cv2.imshow("corrected", finalized_img)
# cv2.imshow("corrected", test_img)
# cv2.imshow("corrected2", test_img2)
# cv2.imshow("corrected3", test_img3)



cv2.waitKey(0)
cv2.destroyAllWindows()