import cv2
import matplotlib.pyplot as plt

# Path to the images
image_filenames = ["./assets/fotosaya_1000px.jpg", "./assets/bocchi_1000px.jpg"]

# Load the images
img1 = cv2.imread(image_filenames[0])
img2 = cv2.imread(image_filenames[1])

# Ensure both images have the same size
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# Perform subtract operation
added_img = cv2.subtract(img1, img2)

# Display image
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(added_img, cv2.COLOR_BGR2RGB))
plt.title('Substract Image')
plt.show()
