import pyotp
import qrcode
code = "LmaoTestCode"
img = qrcode.make(pyotp.totp.TOTP(code).provisioning_uri(name='LexaNoN', issuer_name='PythonTest'))
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
totp = pyotp.TOTP(code)
print("Current OTP:", totp.now())