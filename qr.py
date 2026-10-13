import qrcode

# Apne LinkedIn profile ka link yahan paste karo
data = "https://www.linkedin.com/in/chhaya-ahirvar-72912a335?utm_source=share_via&utm_content=profile&utm_medium=member_android"

# QR Code banao
qr = qrcode.make(data)

# QR Code ko save karo
qr.save("linkedin_qr.png")

print("LinkedIn QR Code created successfully!")
