import cv2

def frame():
    cap = cv2.VideoCapture(0)

    while True :
        _, frame = cap.read()
        cv2.imshow("robot_car", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    frame()