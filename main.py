import pyqrcode, png

qr = pyqrcode.create("link")
qr.png('qrcode.png', scale=8)