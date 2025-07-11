import cv2

# OpenCV DNN
net = cv2.dnn.readNet("ObjectDetection.py/dnn_model/yolov4-tiny.cfg",
                    "ObjectDetection.py/dnn_model/yolov4-tiny.weights")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(308, 308), scale=1/255)

# coconame dosyasını okuma ve boş satır silme 
classes = []
with open("ObjectDetection.py/dnn_model/coco.names", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
# strip()
# Kamera bağlantısı
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)  # Videonun FPS’ini al

while True:
    # Kamera görüntüsü okuma,alma
    ret, frame = cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    # Nesne tanıma 
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=0.4)
    
    # Draw detections with confidence scores
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)

        class_name = classes[class_id]
        
        # Nesne ismi ve confidence değerini yazdır
        text = f"{class_name} {score:.2f}"
        cv2.putText(frame, text, (x, y - 10), 
                cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
    
    # Çıkış talimatını ekrana yazdır
    cv2.putText(frame, "Cikis icin 'q' ya basin", 
            (10, 450),  # Ekranın alt kısmına yerleştir
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    # FPS değeri çerçeveye ekleme
    cv2.putText(frame,f"FPS Degeri: {fps}  ",(450,30),
            cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    
    cv2.imshow("Nesne Tanima", frame)
    
    # 'q' tuşu ile çıkış (1ms bekleme süresi ile akış sağlanır)
    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

