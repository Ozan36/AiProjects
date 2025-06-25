# Gerekli kütüphanelerin eklenmesi
import cv2
import numpy as np
# Görüntü yüklenmesi ve Grayscoole hale getirilmesi
img = cv2.imread("AiProjects/Cororjimg.jpg")
img=cv2.resize(img,(500,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Görüntü yüklenmesi
img2=cv2.imread("AiProjects/Cororjimg.jpg")
# Boyut değiştirme
img2=cv2.resize(img,(500,500))
# ----CORNER DETECTİON----
def Harriscorner():# Harris corner detection
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
    corners = cv2.dilate(corners, None)  # Köşeleri belirginleştir

    # En güçlü köşe değerini bulma
    max_corner_value = corners.max()

    # Eşik değerini belirleme (en güçlünün %1'i)
    threshold = 0.01 * max_corner_value

    #Hangi pikseller köşe olarak kabul edilsin?
    corner_mask = corners > threshold

    #Köşe olan pikselleri kırmızı yapma
    img[corner_mask] = [0, 0, 255]
    # Görüntü gösterme ve kaydetme
    cv2.imshow("Corner Detection(Harris):",img)
    cv2.imwrite("AiProjects/Harrisimg.jpg",img)

def Cannyedge():
    # ----EDGE DETECTİON----
    gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    # Görüntü kenarları belirlenme
    gray2=cv2.Canny(gray2,150,150)
    # Görüntü gösterme ve kaydetme
    cv2.imshow("Edge Detection(Canny):",gray2)
    cv2.imwrite("AiProjects/Cannyimg.jpg",gray2)
while True:
    Harriscorner()
    Cannyedge()
    if cv2.waitKey(0) == ord("q"):
        break

cv2.destroyAllWindows()