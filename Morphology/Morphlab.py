import cv2
import numpy as np

# Görüntüyü gri tonlamalı (0 ile) olarak okuma
frame = cv2.imread('AiProjects/Resim2.png', 0)

# Orijinal görüntünün bir kopyasını alma
frame2 = frame.copy()

# 5x5 boyutunda kernel matrisi tanımlama(beyaz dikdörtgen üzerinde)
kernel = np.ones((5, 5), np.uint8)

# Aşındırma (erode) işlemi: nesneleri küçültme, kenarları siyah yapma
result1 = cv2.erode(frame, kernel, iterations=1)

# Genişletme (dilate) işlemi: nesneleri büyütme,kenarları beyaz yapma
result2 = cv2.dilate(frame, kernel, iterations=1)

# Açma (opening) işlemi: önce erode sonra dilate ->gürültü temizleme
result3 = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

# Görüntüleri ekranda gösterme
cv2.imshow("Orijinal Resim", frame2)
cv2.imshow("Erozyon", result1)
cv2.imshow("Dilate", result2)
cv2.imshow("Opening", result3)
# Görüntüleri Kaydetme
cv2.imwrite("AiProjects/Erozonimg.jpg",result1)
cv2.imwrite("AiProjects/Dilate.jpg",result2)
cv2.imwrite("AiProjects/Opening.jpg",result3)

# Bir tuşa basılana kadar bekle ve tüm pencereleri kapat
cv2.waitKey(0)
cv2.destroyAllWindows()

