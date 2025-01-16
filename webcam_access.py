import cv2
from matplotlib import pyplot as plt

# only for devices with one connected capture device
def photo_capture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("photo.jpg", frame)
    cap.release()

def render():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    photo_capture()
    render()