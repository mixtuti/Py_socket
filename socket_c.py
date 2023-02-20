from PIL import ImageGrab
import subprocess as sp
import socket
import io


def image2bin(img):
    img_bin = io.BytesIO()
    img.save(img_bin, format=img.format)
    return img_bin.getvalue()


cmd = "screencapture -c -R100,400,150,150"
sp.run(cmd.split())

address = ("127.0.0.1", 12345)
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect(address)

img = ImageGrab.grabclipboard()
cl.send(image2bin(img))
