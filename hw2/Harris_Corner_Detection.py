import matplotlib.pyplot as plt
import numpy as np
import cv2
# %matplotlib inline

from scipy import ndimage

def gaussian_smooth(size, sigma=1):
    ########################################################################
    # TODO:                                                                #
    #   Perform the Gaussian Smoothing                                     #
    #   Input: window size, sigma                                          #
    #   Output: smoothing image                                            #
    ########################################################################
    ax = np.arange(-(size // 2), size // 2 + 1)
    xx, yy = np.meshgrid(ax, ax) #平面上每個點的座標
    
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)  # normalization
    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return kernel

from scipy.ndimage import convolve
# img_filtered_K5 = convolve(img_Gray, gaussian_smooth(size=5,sigma=5))
# img_filtered_K10 = convolve(img_Gray, gaussian_smooth(size=10,sigma=5))

def sobel_edge_detection(im, sigma=1):
    ########################################################################
    # TODO:                                                                #
    #   Perform the sobel edge detection                                   #
    #   Input: image after smoothing                                       #
    #   Output: the magnitude and direction of gradient                    #
    ########################################################################
    # Sobel kernels
    Kx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    
    Ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])

    Ix = convolve(im, Kx)
    Iy = convolve(im, Ky)

    gradient_magnitude = np.sqrt(Ix**2 + Iy**2)
    gradient_direction = np.arctan2(Iy, Ix)
    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return  (gradient_magnitude, gradient_direction)


def structure_tensor(gradient_magnitude, gradient_direction, k, sigma=1):
    ########################################################################
    # TODO:                                                                #
    #   Perform the cornermess response                                    #
    #   Input: gradient_magnitude, gradient_direction                      #
    #   Output: second-moment matrix of Structure Tensor                   #
    ########################################################################
    # 還原 Ix, Iy
    Ix = gradient_magnitude * np.cos(gradient_direction)
    Iy = gradient_magnitude * np.sin(gradient_direction)

    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    # Gaussian window
    window = gaussian_smooth(size=3, sigma=sigma)

    Sxx = convolve(Ixx, window)
    Syy = convolve(Iyy, window)
    Sxy = convolve(Ixy, window)

    # Harris response
    det = (Sxx * Syy) - (Sxy ** 2)
    trace = Sxx + Syy
    R = det - k * (trace ** 2)
    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return R

def NMS(harrisim,window_size=3,threshold=0.1): #window_size=3 or 30
    ########################################################################
    # TODO:                                                                #
    #   Perform the Non-Maximum Suppression                                #
    #   Input: Structure Tensor, window size, threshold                    #
    #   Output: filtered coordinators                                      #
    ########################################################################
    coords = []
    
    harrisim = harrisim / np.max(harrisim)  # normalize

    offset = window_size // 2
    H, W = harrisim.shape

    for i in range(offset, H - offset):
        for j in range(offset, W - offset):

            window = harrisim[i-offset:i+offset+1, j-offset:j+offset+1]
            if harrisim[i, j] >= np.max(window) and harrisim[i, j] > threshold:
                coords.append((i, j))
    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return coords

def plot_harris_points(image,filtered_coords):
    plt.figure()
    plt.gray()
    plt.figure(figsize=(20,10))
    plt.imshow(image)
    plt.plot([p[1] for p in filtered_coords],[p[0]for p in filtered_coords],'+')
    plt.axis('off')
    plt.show()
    
def rotate(image, angle, center = None, scale = 1.0):

    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated