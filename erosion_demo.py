import matplotlib.pyplot as plt
import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


image_path = 'images/mustang.png'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

eroded_image = cv2.erode(image, structuring_element, iterations=1)

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(
    eroded_image, cmap='gray'), plt.title('Eroded Image')
plt.show()
