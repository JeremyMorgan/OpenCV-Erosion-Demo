import cv2  # Import the OpenCV library
import numpy as np  # Import the NumPy library
import matplotlib  # Import the Matplotlib library
matplotlib.use('TkAgg')  # Set the backend for Matplotlib to 'TkAgg'
import matplotlib.pyplot as plt  # Import the Pyplot module from Matplotlib

# Define the path to the image
image_path = 'images/balloon.png'

# Read the image from the given path, and convert it to grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the structuring element as an ellipse with a 3x3 size
structuring_element_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# Perform erosion on the grayscale image using the ellipse-shaped structuring element
eroded_image_ellipse = cv2.erode(image, structuring_element_ellipse, iterations=1)

# Create a new figure with a specified size
plt.figure(figsize=(12, 6))

# Create the first subplot, showing the original grayscale image
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')

# Create the second subplot, showing the eroded image
plt.subplot(122), plt.imshow(eroded_image_ellipse, cmap='gray'), plt.title('Eroded Image with Ellipse')

# Display the subplots
plt.show()
