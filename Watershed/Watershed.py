#Gerekli kütüphanelerin oluşturulması ve eklenmesi
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from skimage import io, color, filters

# Resmi yükleme ve gri tonlamaya çevirme
image = io.imread("AiProjects/Resim8.webp")
gray = color.rgb2gray(image)

# Thresholding ile binary(ikili) maske oluşturma
thresh = filters.threshold_otsu(gray)
binary = gray > thresh

# Küçük gürültüleri temizleme
binary_cleaned = ndi.binary_opening(binary, structure=np.ones((3, 3)))

# Mesafe dönüşümünü hesapla (her pikselin en yakın arka plan pikseline olan uzaklığı)
distance = ndi.distance_transform_edt(binary_cleaned)
# Mesafe haritasındaki yerel maksimum noktalarını bul (nesnelerin merkezleri olarak kullanılacak)
# footprint=np.ones((3,3)): 3x3'lük komşuluk alanında maksimum ara
# labels=binary_cleaned: Sadece nesne piksellerinde ara
coords = peak_local_max(distance, footprint=np.ones((3, 3)), labels=binary_cleaned)

# Maksimum noktalar için boş bir maske oluştur
mask = np.zeros(distance.shape, dtype=bool)

# Bulunan maksimum noktaları maskeye işaretle (True yap)
# coords.T: Koordinatları transpoze ederek (satır, sütun) şeklinde al
mask[tuple(coords.T)] = True

# İşaretlenmiş noktaları etiketle (her nesne için farklı bir numara ver)
# _: Etiket sayısını döndürür ama biz kullanmayacağız
markers, _ = ndi.label(mask)

# Watershed algoritmasını uygula
# -distance: Watershed minimumları baz aldığı için mesafeyi ters çevir
# markers: Başlangıç noktaları (nesne merkezleri)
# mask=binary_cleaned: İşlemi sadece nesne piksellerinde uygula
labels = watershed(-distance, markers, mask=binary_cleaned)

# 3 sütunlu bir figür oluştur (orijinal, binary ve sonuç görüntüleri için)
fig, axes = plt.subplots(ncols=3, figsize=(12, 4))

# Eksen dizisini düzleştir (ravel) ve ax değişkenine ata
ax = axes.ravel()

# 1. Görsel: Orijinal gri tonlamalı görüntü
ax[0].imshow(gray, cmap=plt.cm.gray)
ax[0].set_title('Original Image')

# 2. Görsel: Binary maske (gürültü temizlenmiş)
ax[1].imshow(binary_cleaned, cmap=plt.cm.gray)
ax[1].set_title('Binary Mask')

# 3. Görsel: Watershed segmentasyon sonucu
# nipy_spectral colormap: Farklı nesneleri farklı renklerle gösterme
ax[2].imshow(labels, cmap=plt.cm.nipy_spectral)
ax[2].set_title('Watershed Segmentation')

# Tüm eksenlerdeki x ve y eksenlerini kaldırma
for a in ax:
    a.set_axis_off()

# Görseller arasında uygun boşluk bırakma
plt.tight_layout()

# Görseli Kaydetmek için 
plt.savefig("AiProjects/Watershed.jpg")

# Görselleri gösterme
plt.show()

