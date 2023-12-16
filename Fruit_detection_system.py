from ultralytics import YOLO
import numpy
import easyocr



model = YOLO("yolov8s.pt","v8")

detect_o = model.predict(source="E:\\Codes\\weights\\wl.jpg",conf=0.25,save=True)

print(detect_o)
print(detect_o[0])

predict_number = 13
reader = easyocr.Reader(['en'])
result = reader.readtext(f'E:\\Codes\\runs\\detect\\predict{predict_number}\\wl.jpg',detail=0)
print("Result = ",result[0][:-4])