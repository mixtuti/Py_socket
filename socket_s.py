from PIL import Image
import socket
import io

address = ("127.0.0.1", 12345)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(1)
print("waiting...")

cl, cla = server.accept()
print("connected!!", cla)

while True:
    data = cl.recv(409600)
    if not data:
        print("client is closed")
        break

    img = Image.open(io.BytesIO(data))
    img.show()
