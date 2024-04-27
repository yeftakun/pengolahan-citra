import cv2
import numpy as np
import matplotlib.pyplot as plt

# Unggah gambar
#image_filename = input("Masukkan nama file gambar: ")
image_filename = "./assets/fotosaya_1000px.jpg"

# Baca gambar yang diunggah
img = cv2.imread(image_filename)

# hitung citra grayscale dengan rumus Po = (R + G + B) / 3
gray_img = (img[:, :, 0].astype(int) + img[:, :, 1]. astype(int) + img[:, :, 2].astype(int)) // 3

# Menampilkan gambar asli dan hasil grayscale
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Gayscale Image')

plt.show()
