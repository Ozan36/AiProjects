import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
color_image = cv2.imread('PythonGoruntuisleme\Resim4.jpg', cv2.IMREAD_COLOR)

# convert to grayscale image
grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Manual thresholding
threshold_value = 128  # Example manual threshold value
_, binary_image = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(color_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Grayscale Image')
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title(f'Global Thresholding (T={threshold_value})')
plt.imshow(binary_image, cmap='gray')
plt.savefig("AiProjects/Thresimage.jpg")
plt.axis('off')
plt.show()


