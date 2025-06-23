import cv2

# Görüntüyü yükleme
image = cv2.imread("PythonGoruntuisleme/Resim7.jpg")
image=cv2.resize(image,(500,500))
imagecopy=image.copy()
grayscoole=cv2.cvtColor(imagecopy,cv2.COLOR_BGR2GRAY)
# Seçilen bölge koordinatları
x, y, w, h = 50, 50, 200, 200

# Gri görüntüden seçilen alan (200x200)
area=grayscoole[y:y+h,x:x+w]

# Gri alanı 3 kanallı hale getir (200x200x3)
orjresim= cv2.cvtColor(area, cv2.COLOR_GRAY2BGR)
# Gri alanın blurlaştırmak için kopya oluşturma
orjresim2=orjresim.copy()
orjresim2=cv2.blur(orjresim2,(7,7),0)

# Orijinal resmin belirli bölgesini 3 kanallı gri bölge ile değiştir
image[y:y+h, x:x+w] = orjresim
imagecopy[y:y+h,x:x+h]=orjresim2
# Normal resim ve Karartılmış resmin gösterilmesi
while True:
    cv2.imshow("GrayscooleImage:",image)
    cv2.imshow("Blurimage:",imagecopy)
    if cv2.waitKey(0)==ord("q"):
        break
# Alınan görüntülerin kaydedilmesi
cv2.imwrite("AiProjects/Grayscoleimage.jpg",image)
cv2.imwrite("AiProjects/Blurimage.jpg",imagecopy)
cv2.destroyAllWindows()
