import cv2
import numpy as np
import matplotlib.pyplot as plt

# Unggah gambar
#image_filename = input("Masukkan nama file gambar: ")
image_filename = "./assets/fotosaya_1000px.jpg"

# Baca gambar yang diunggah
img = cv2.imread(image_filename)

#menerapkan rumus negasi: Po(x,y) = 225 - Pi(x,y)
negated_img = 255 - img

# Menampilkan gambar asli dan hasil negasi
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(negated_img, cmap='gray')
plt.title('Negated Image')

plt.show()
