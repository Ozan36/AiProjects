import cv2
import numpy as np

# Trackbar callback fonksiyonu (gerekli ama kullanılmayacak)
def nothing(x):
    pass

cap = cv2.VideoCapture("PythonGoruntuisleme/video.mp4")

# Trackbar penceresi oluştur
cv2.namedWindow("Trackbars")

# HSV değerlerini ayarlamak için trackbarlar oluştur
cv2.createTrackbar("LH", "Trackbars", 0, 179, nothing)  
cv2.createTrackbar("LS", "Trackbars", 0, 255, nothing) 
cv2.createTrackbar("LV", "Trackbars", 0, 255, nothing)   
cv2.createTrackbar("UH", "Trackbars", 179, 179, nothing) 
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing) 
cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing)  

while True:
    ret, frame = cap.read() 
    # Video bittiğinde çık
    if not ret:
        break   

    # Görüntüyü yeniden boyutlandır
    frame = cv2.resize(frame, (400,400))  
    # BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  

    # Trackbarlardan HSV sınır değerlerini al
    lh = cv2.getTrackbarPos("LH", "Trackbars")
    ls = cv2.getTrackbarPos("LS", "Trackbars")
    lv = cv2.getTrackbarPos("LV", "Trackbars")
    uh = cv2.getTrackbarPos("UH", "Trackbars")
    us = cv2.getTrackbarPos("US", "Trackbars")
    uv = cv2.getTrackbarPos("UV", "Trackbars")

    lower = np.array([lh, ls, lv])  
    upper = np.array([uh, us, uv])  
    
    # HSV aralığındaki pikseller için maske oluştur
    mask = cv2.inRange(hsv, lower, upper) 
    # Maskeyi orijinal görüntüye uygula
    result = cv2.bitwise_and(frame, frame, mask=mask) 

    cv2.imshow("Original", frame)   
    cv2.imshow("Mask", mask)         
    cv2.imshow("Filtered", result) 
    
    if cv2.waitKey(0)== ord('q'):
        break
cap.release()   
cv2.destroyAllWindows() 
