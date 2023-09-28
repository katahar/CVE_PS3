
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
import numpy as np
import argparse
# import matplotlib.pyplot as plt
