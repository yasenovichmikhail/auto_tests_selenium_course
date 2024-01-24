
import qrcode 
  
def generate_qr_code(data): 
    qr = qrcode.QRCode(version=1, box_size=10, border=5)  # type: ignore
    qr.add_data(data) 
    qr.make(fit=True) 
    img = qr.make_image(fill_color="black", back_color="white") 
    img.save("qr_code.png") 
    print("QR code generated!") 
  
data = 'Data to be encoded'
generate_qr_code(data) 