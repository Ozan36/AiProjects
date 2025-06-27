# OpenCV kütüphanelerinin eklenmesi
import cv2
# kameraya bağlanma 
kamera = cv2.VideoCapture(0) 
while (True): 
    _, videoGoruntu = kamera.read()
    # görüntü içerisindeki sol sağ düzeltmesi
    gorsel=cv2.flip(videoGoruntu,-1)
    # dikdörtgen eklenmiş görüntünün gösterilmesi
    cv2.imshow("Bilgisayar Kamerasi", gorsel)
    # Görüntüden çıkmak için kullanılır
    if cv2.waitKey(1) == ord('q'):
        break
    # kamera kapatmak için 
kamera.release()
    # openCV pencerelerini kapatmak için
cv2.destroyAllWindows() 

