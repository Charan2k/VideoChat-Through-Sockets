import client
import server
import threading


t1 = threading.Thread(target=server.connect)
t2 = threading.Thread(target=client.connect)
t1.start()
t2.start()
