import imageio as iio
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

image = 'animal.jpg'

# Part A
img0 = iio.imread(image)
img0 = np.mean(img0, axis=-1)

# Part B
fig = plt.figure()

sx = ndimage.sobel(img0)
plt.subplot(2,2,2)
plt.imshow(sx, cmap=plt.cm.gray)
sy = ndimage.sobel(img0, axis=1)
plt.subplot(2,2,3)
plt.imshow(sy, cmap=plt.cm.gray)



