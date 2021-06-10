import cv2
import socket
import struct
import pickle

def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost" , 8485))
    connection = client_socket.makefile('wb')

    cam = cv2.VideoCapture(1)

    cam.set(3, 320);
    cam.set(4, 240);

    img_counter = 0

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    while True:
        ret, frame = cam.read()
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 0)
        size = len(data)


        client_socket.sendall(struct.pack(">L", size) + data)
        img_counter += 1
        cv2.imshow('Client Side',frame)
        if cv2.waitKey(1) == ord('q'):
            exit(0)

    cam.release()

connect()