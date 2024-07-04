import base64
import socket
import cv2
import time
import threading

# Initialize the camera
cam = cv2.VideoCapture(0)

# Create TCP/IP sockets
sock_image = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address
server_image = ('127.0.0.1', 8053)

print('starting up on {} port {}'.format(*server_image))
sock_image.bind(server_image)

# Listen for incoming connections
sock_image.listen(2)

# Custom Thread Class
class ImageThread(threading.Thread):
    def task_send_image(self):
        cam_img = True
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection_img, client_address_img = sock_image.accept()

            try:
                print('connection from', client_address_img)

                # Receive the data in small chunks and retransmit itafhgfiagiafghsoug
                while True:
                    if cam_img:
                        ret, frame = cam.read()
                        flipped_frame = cv2.flip(frame, 1)
                        # Reduce the image to the smallest possible size
                        resized_frame = cv2.resize(flipped_frame, (500, 500))

                        # Encode the frame to JPEG with minimal quality
                        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]
                        result, image = cv2.imencode('.jpg', resized_frame, encode_param)
                        jpg_as_text = base64.b64encode(image).decode('utf-8')  # Ensure it is a stringdidjvba
                        print(jpg_as_text)
                        # Send the encoded image over the socket connection
                        connection_img.sendall(jpg_as_text.encode('utf-8'))
                        time.sleep(0.2)  # Adjust the delay as neededkajsgfakdfgdzkgvskjgfaufhlsrgaiufhglshg

            except KeyboardInterrupt:
                connection_img.close()
            except Exception as e:
                print(f"Exception occurred: {e}")
            finally:
                # Clean up the connection
                connection_img.close()

    def run(self):
        self.task_send_image()

    def join(self):
        threading.Thread.join(self)

# Driver function
def main():
    image_thread = ImageThread()
    image_thread.start()

# Driver code
if __name__ == '__main__':
    main()

# Release the camera resource on exit
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    cam.release()
    sock_image.close()
