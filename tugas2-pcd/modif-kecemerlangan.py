

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Unggah gambar
#image_filename = input("Masukkan nama file gambar: ")
image_filename = "./assets/fotosaya_1000px.jpg"

# Baca gambar yang diunggah
img = cv2.imread(image_filename)

# Tentukan nilai kecerahan yang ingin ditambahkan
brightness_value = 50

# Tambahkan nilai kecerahan ke setiap piksel dalam citra
brightened_img = np.clip(img.astype(int) + brightness_value, 0, 255).astype(np.uint8)

# Menampilkan gambar asli dan hasil kecerahan
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(brightened_img, cv2.COLOR_BGR2RGB))
plt.title('Brightened Image')

plt.show()
