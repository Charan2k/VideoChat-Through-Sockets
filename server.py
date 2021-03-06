import socket
import cv2
import pickle
import struct

def connect():
    HOST=''
    PORT=8485

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    print('Socket bind complete')
    s.listen(10)
    print(f'LISTENING AT {PORT}')

    conn,addr=s.accept()
    print(f'Connection Accepted from {addr[0]}')

    data = b""
    payload_size = struct.calcsize(">L")
    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        cv2.imshow('Server Side',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()

connect()
