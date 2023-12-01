import numpy as np
import imageio.v2 as imageio
import scipy.ndimage 
import cv2

# Input image file name
img = "Test Images/img2.jpg"

# Function to convert an RGB image to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

# Function to create a dodge effect for image sketching, performs a pixel-wise calculation to achieve the dodge effect.
def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')

# Read the input image using imageio
ss = imageio.imread(img)

# Convert the image to grayscale
gray = rgb2gray(ss)

# Invert the grayscale image to create a negative
i = 255 - gray

# Apply Gaussian blur to the inverted image & Sigma controls the intensity of blurriness
blur = scipy.ndimage.gaussian_filter(i, sigma=27)

# Create the final sketch by applying dodge effect
r = dodge(blur, gray)

# Save the final sketch as an image file
cv2.imwrite('final_sketch.png', r)
