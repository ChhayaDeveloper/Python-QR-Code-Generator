import qrcode

# Apne LinkedIn profile ka link yahan paste karo
data = "https://forms.gle/5snu4GUhiY45YFd99"

# QR Code banao
qr = qrcode.make(data)

# QR Code ko save karo
qr.save("linkedin_qr.png")

print("LinkedIn QR Code created successfully!")
