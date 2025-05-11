from tensorflow.keras.models import load_model
import numpy as np
import cv2

# Load the trained model
model = load_model("models/gender_mobilenet_model.h5")

# Load face detection model
face_net = cv2.dnn.readNetFromCaffe('models/deploy.prototxt', 'models/res10_300x300_ssd_iter_140000_fp16.caffemodel')

def detect_face(img, img_size=(128, 128)):
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_net.setInput(blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            startX, startY, endX, endY = box.astype("int")
            face = img[startY:endY, startX:endX]
            face = cv2.resize(face, img_size)
            face = face / 255.0
            return np.expand_dims(face, axis=0)

    return None

def detect_gender(photo_path):
    img = cv2.imread(photo_path)
    if img is None:
        return "Invalid image path or unreadable image."

    face_array = detect_face(img)
    if face_array is None:
        return "❌ No face detected."

    prob = model.predict(face_array)[0][0]
    gender = 'Male' if prob < 0.5 else 'Female'
    confidence = (1 - prob) if gender == 'Male' else prob
    # return f"{gender} ({confidence * 100:.2f}%)"
    return gender.lower()



# from deepface import DeepFace
# import tensorflow as tf

# def detect_gender(photo_path):
#     try:
#         result = DeepFace.analyze(img_path=photo_path, actions=['gender'], enforce_detection=True,  # allow non-detected faces
#     detector_backend='opencv'
# )
#         print(result)

#         # gender = result[0].get('dominant_gender', 'unknown').lower()
#         # return gender if gender in ['male', 'female'] else 'unknown'
#         gender = result[0]['gender'].lower()
#         print(gender)
#         return 'female' if 'female' in gender else 'male'
#     except Exception as e:
#         print(f"[Gender Detection Error]: {e}")
#         return 'male'  # fallback to male if detection fails
#     finally:
#         tf.keras.backend.clear_session()

# photo_path = "C:/Users/ADMIN/Pictures/Camera Roll/b1.jpg"

# gender = detect_gender(photo_path)
