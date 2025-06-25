# Gerekli kütüphanelerin eklenmesi
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Görüntü yüklenmesi
image = cv2.imread('AiProjects/Resim1.png')
image=cv2.resize(image,(500,500))
# Orijinal görüntüyü numpy array'e dönüştürme
arry = np.array(image)
print("---------------Orijinal görüntü boyutu:-----------------", arry.shape)
print(arry)
while True:
    cv2.imshow("Normal resim:",image)
    if cv2.waitKey(1) == ord("q"):
        break
# Görüntüyü grayscale'e çevirme
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
while True:
    cv2.imshow("Gri resim:",gray_image)
    if cv2.waitKey(1) == ord("q") :
        break
# Grayscale görüntüyü numpy array'e dönüştürme
gray= np.array(gray_image)
print("\n --------------Grayscale görüntü boyutu:--------------", gray.shape)
print(gray)
cv2.destroyAllWindows()



