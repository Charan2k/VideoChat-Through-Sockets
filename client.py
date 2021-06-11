import cv2
import socket
import struct
import pickle

def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("" , 8485))

    cam = cv2.VideoCapture(1)

    while True:
        while cam.isOpened():
            ret, frame = cam.read()
            data = pickle.dumps(frame, 0)
            size = len(data)


            client_socket.sendall(struct.pack(">L", size) + data)
            cv2.imshow('Client Side',frame)
            if cv2.waitKey(1) == ord('q'):
                exit(0)

    cam.release()

connect()
