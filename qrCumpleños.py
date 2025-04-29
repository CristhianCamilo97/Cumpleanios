import qrcode

# Cambia la URL si es necesario
url = "https://cristhiancamilo97.github.io/Cumpleanios/Cumpleaños.html"

# Generar el código QR
img = qrcode.make(url)

# Guardar la imagen
img.save("Feliz cumpleaños.png")

print("¡QR generado y guardado!")
