import cv2
from deepface import DeepFace
import time

def detect_mood():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    
    mood_colors = {
    "happy": (0, 255, 0),        # Green
    "sad": (255, 0, 0),          # Blueish red
    "angry": (0, 0, 255),        # Red
    "neutral": (255, 255, 0),    # Yellow
    "surprise": (255, 0, 255),   # Magenta
    "fear": (128, 0, 128),       # Purple
    "disgust": (0, 128, 0)       # Dark Green
}


    print("🟢 Real-Time Mood Detection Running... Press 's' to capture mood | Press 'q' to quit without saving")

    last_mood = "Detecting..."
    last_detect_time = 0
    detect_interval = 2  # seconds
    
    face_found = False

    while True:
        ret, frame = cam.read()
        if not ret:
            print("❌ Failed to access webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            face_found = True
            for (x, y, w, h) in faces:
                color = (0, 255, 0) if w > 100 and h > 100 else (0, 0, 255)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, "Face Detected", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

                current_time = time.time()
                if current_time - last_detect_time > detect_interval:
                    try:
                        roi = frame[y:y+h, x:x+w]
                        cv2.imwrite("temp_face.jpg", roi)
                        result = DeepFace.analyze(img_path="temp_face.jpg", actions=['emotion'], enforce_detection=False)
                        last_mood = result[0]['dominant_emotion']
                        last_detect_time = current_time
                    except:
                        last_mood = "Undetected"

                mood_text = f"Mood: {last_mood}"
                mood_color = mood_colors.get(last_mood, (255, 255, 255))  # default white
                cv2.putText(frame, f"Mood: {last_mood}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, mood_color, 2)

        else:
            face_found = False

        # Show window and overlay
        cv2.putText(frame, "Moodify is detecting your mood...", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.imshow("Moodify - Real-Time Mood Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            if face_found:
                print(f"\n✅ Final Captured Mood: {last_mood}")
            else:
                print("⚠️ No face detected. Please make sure your face is visible to the camera ⚠️")
                last_mood = None
            break
        elif key == ord('q'):
            print("\n❌ Exited without saving mood.")
            last_mood = None
            break

    cam.release()
    cv2.destroyAllWindows()
    return last_mood