import cv2

# Görüntüyü yükleme
image = cv2.imread("PythonGoruntuisleme/Resim7.jpg")

# Görüntü boyutunu kontrol et ve yeniden boyutlandır (isteğe bağlı)
if image is not None:
    image = cv2.resize(image, (500, 500))
else:
    print("Hata: Görüntü yüklenemedi!")
    exit()

# Orijinal görüntünün kopyasını oluşturma
imagecopy = image.copy()


# Dikdörtgen çiz (içi sarı dolu)
cv2.rectangle(imagecopy,(50,50),(200,200),(0,255,255),5)

cv2.rectangle(imagecopy,(50,50),(200,200),(0,0,0),-1)
# Sonuçları gösterme
cv2.imshow("Orijinal resim", image)
cv2.imshow("Sarialanli resim", imagecopy)
cv2.imwrite("PythonGoruntuisleme/Orjresim.jpg",image)
cv2.imwrite("PythonGoruntuisleme/Sarialan.jpg",imagecopy)

# Klavyeden 'q' tuşuna basılana kadar bekle
while True:
    if cv2.waitKey(0) == ord('q'):
        break

# Pencereleri kapat
cv2.imwrite("AiProjects/Orj.jpg",image)
cv2.imwrite("AiProjects/Yellow.jpg",imagecopy)
cv2.destroyAllWindows()

