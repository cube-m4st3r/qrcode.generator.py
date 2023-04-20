# import modules
import qrcode
from PIL import Image


def run():

    # taking image which user wants
    # in the QR code center
    Logo_link = 'logo.jpg'

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    url = ''

    QRcode.add_data(url)

    QRcode.make()

    QRimg = QRcode.make_image(
        fill_color="black", back_color="white").convert('RGB')

    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    QRimg.save('qrcode.png')

    print('QR code generated!')

if __name__ == "__main__":
    run()