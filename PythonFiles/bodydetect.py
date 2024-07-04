import cv2
import mediapipe as mp

class FullBodyDetector:
    def __init__(self, staticMode=False, modelComplexity=1, smoothLandmarks=True,
                 enableSegmentation=False, smoothSegmentation=True,
                 detectionCon=0.5, trackCon=0.5):
        self.staticMode = staticMode
        self.modelComplexity = modelComplexity
        self.smoothLandmarks = smoothLandmarks
        self.enableSegmentation = enableSegmentation
        self.smoothSegmentation = smoothSegmentation
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHolistic = mp.solutions.holistic
        self.holistic = self.mpHolistic.Holistic(static_image_mode=self.staticMode,
                                                 model_complexity=self.modelComplexity,
                                                 smooth_landmarks=self.smoothLandmarks,
                                                 enable_segmentation=self.enableSegmentation,
                                                 smooth_segmentation=self.smoothSegmentation,
                                                 min_detection_confidence=self.detectionCon,
                                                 min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findBody(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.holistic.process(imgRGB)
        body_parts = []

        h, w, c = img.shape

        # Define a function to process landmarks safely
        def process_landmark(landmarks, idx, color, size=5):
            if landmarks and idx < len(landmarks.landmark):
                landmark_point = landmarks.landmark[idx]
                cx, cy = int(landmark_point.x * w), int(landmark_point.y * h)
                body_parts.append([cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), size, color, cv2.FILLED)

        # Process different parts
        # Face landmarks
        if self.results.face_landmarks:
            process_landmark(self.results.face_landmarks, 1, (0, 255,0))  # Nose tip

        # Pose landmarks
        pose_indices = {
             
            'shoulders': [11, 12],
            'elbows': [13, 14],
            'palms': [15, 16],
            'pinky':[17,18],
            'index':[21,22],
            'waist': [23,24],
            'knees': [25, 26],
            'feet1': [29, 30],
            'feet2':[31,32],
        }
        
        for key, indices in pose_indices.items():
            for idx in indices:
                process_landmark(self.results.pose_landmarks, idx, (0, 255, 0))

        return img, body_parts