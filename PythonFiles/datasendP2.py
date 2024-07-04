import cv2
import bodydetect as bd
import socket

# Initialize camera parameters
width, height = 1920, 1080
cam2 = cv2.VideoCapture(1)  # Second camera
cam2.set(3, width)
cam2.set(4, height)

# Initialize the body detector and socket for camera 2
detector2 = bd.FullBodyDetector()
connection2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort2 = ('127.0.0.1', 5053)  # Different port for second camera

frame_count2 = 0
print_interval2 = 1  # Print coordinates every 1 frame

while True:
    success2, img2 = cam2.read()
    if not success2:
        break
    
    data2 = []
    
    img2, co_or2 = detector2.findBody(img2, draw=True)
    frame_count2 += 1

    if frame_count2 % print_interval2 == 0 and co_or2:
        for val in co_or2:
            data2.extend([val[0], height - val[1]])
        connection2.sendto(str.encode(str(data2)), serverAddressPort2)
    
    cv2.imshow("Image2", img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam2.release()
cv2.destroyAllWindows()
