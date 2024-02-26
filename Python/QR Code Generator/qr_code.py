import qrcode

def generate_qrcode(url, file_name):
    
    qr = qrcode.QRCode(
        version=3,
        box_size=20,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('QR Code Generator\\' + file_name + '.png')
    

if __name__ == '__main__':   
    url = input('Enter an URL: ')
    file_name = input('Enter File Name: ')
    
    generate_qrcode(url, file_name)

