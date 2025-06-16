import pyqrcode
import png

link = "https://codegnan.com/"

qr = pyqrcode.create(link)

qr.png("myqr.png",scale=8)
