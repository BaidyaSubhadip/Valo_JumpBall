import cv2
import bodydetect as bd
import socket

# Initialize camera parameters
width, height = 1920, 1080
cam1 = cv2.VideoCapture(0)  # First camera
cam1.set(3, width)
cam1.set(4, height)

# Initialize the body detector and socket for camera 1
detector1 = bd.FullBodyDetector()
connection1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort1 = ('127.0.0.1', 5052)  # Change port if necessary

frame_count1 = 0
print_interval1 = 1  # Print coordinates every 1 frame

while True:
    success1, img1 = cam1.read()
    if not success1:
        break
    
    data1 = []
    
    img1, co_or1 = detector1.findBody(img1, draw=True)
    frame_count1 += 1

    if frame_count1 % print_interval1 == 0 and co_or1:
        for val in co_or1:
            data1.extend([val[0], height - val[1]])
        connection1.sendto(str.encode(str(data1)), serverAddressPort1)
    
    cv2.imshow("Image1", img1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam1.release()
cv2.destroyAllWindows()
