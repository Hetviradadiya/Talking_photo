import cv2
import os

def detect_gender(photo_path):
    # Pre-trained models
    proto = os.path.join("models", "gender_deploy.prototxt")
    model = os.path.join("models", "gender_net.caffemodel")
    gender_list = ['Male', 'Female']

    # Load model
    net = cv2.dnn.readNetFromCaffe(proto, model)

    image = cv2.imread(photo_path)
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(227, 227),
                                 mean=(78.4263377603, 87.7689143744, 114.895847746),
                                 swapRB=False)

    net.setInput(blob)
    gender_preds = net.forward()
    gender = gender_list[gender_preds[0].argmax()]
    print(f"Detected Gender: {gender}")
    return gender.lower()
