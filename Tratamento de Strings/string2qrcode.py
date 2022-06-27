# Necessario a instalar esse dois
# pip install pyqrcode
# pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode

# link desejado ou texto para o QRCode
QRString = 'https://github.com/jnishizima'

#Montar o QRCode
url = pyqrcode.create(QRString)

# Salvar o QRCode gerado no local desejado
url.png(r'qr.png', scale=8)