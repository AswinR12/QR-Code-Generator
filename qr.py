import pyqrcode
import png
import os
from PIL import Image

str = input("Enter the string: ")

qc = pyqrcode.create(str) #Generate QR code.

print("\nQR code generated...\n")
#Saving file.
x = 0
files = [f for f in os.listdir( os.curdir ) if os.path.isfile(f) ] #List files in PWD.
while(x==0):
	x = 1
	name = input("Save as? ")
	svg = name + ".svg"
	png = name + ".png"
	#Check if file name is taken
	for file in files:
		if file == svg or file == png:
			print("File name taken.Please use a different name.")
			x = 0
			break
#Save as svg file.
qc.svg(svg, scale = 8)
print("Saved as {}".format(svg))

#Save as png file.
qc.png(png, scale = 6)
print("Saved as {}".format(png))

#To show the QR Code
sh = input("Show code? (Y/N): ")
if sh == 'Y' or sh == 'y':
	im = Image.open(png)
	im.show()


