import cv2
import numpy as np

cap = cv2.VideoCapture("AiProjects/video2.mp4")

while True:
    ret, frame = cap.read()
    
    if not ret:  # Video bittiğinde döngüden çıkma
        break
    
    # Kareyi yeniden boyutlandırma
    frame = cv2.resize(frame, (500, 500))
    
    # BGR'den HSV'ye dönüştürme
    into_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    L_limit = np.array([35, 100, 100])   # Yeşil ton için alt HSV sınırı
    U_limit = np.array([85, 255, 255])   # Yeşil ton için üst HSV sınırı
    
    # Maske oluşturma (yeşil alanları beyaz yapar)
    b_mask = cv2.inRange(into_hsv, L_limit, U_limit)
    
    green = cv2.bitwise_and(frame, frame, mask=b_mask)
    
    # Orijinal kareyi gösterme
    cv2.imshow('Original', frame)
    
    # Yeşil renk tespitli kareyi gösterme
    cv2.imshow('Green Detector', green)
    
    if cv2.waitKey(1)== ord("q"):
        break

# Kaynakları temizleme
cap.release()
cv2.destroyAllWindows()