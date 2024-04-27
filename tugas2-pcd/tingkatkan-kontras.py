
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Unggah gambar
#image_filename = input("Masukkan nama file gambar: ")
image_filename = "./assets/fotosaya_1000px.jpg"

# Baca gambar yang diunggah
img = cv2.imread(image_filename)

# tentukan ambang batas (threshold) dan gain
TK = 100
G = 1.5

# rumus peningkatan kontras: Po G * (Pi - TK) + TK
constrasted_img = np.clip(G * (img.astype(int) - TK) + TK, 0, 255).astype(np.uint8)

# Menampilkan gambar asli dan hasil grayscale
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(constrasted_img, cv2.COLOR_BGR2RGB))
plt.title('Contrasted Image')

plt.show()
