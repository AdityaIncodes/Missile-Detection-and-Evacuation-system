import cv2
import numpy as np

class KalmanTracker:
    def __init__(self):
        self.kalman = cv2.KalmanFilter(4, 2)

        self.kalman.measurementMatrix = np.array(
            [[1,0,0,0],
             [0,1,0,0]], np.float32)

        self.kalman.transitionMatrix = np.array(
            [[1,0,1,0],
             [0,1,0,1],
             [0,0,1,0],
             [0,0,0,1]], np.float32)

        self.kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

    def predict(self, x, y):
        measured = np.array([[np.float32(x)],
                             [np.float32(y)]])

        self.kalman.correct(measured)
        predicted = self.kalman.predict()

        return int(predicted[0]), int(predicted[1])