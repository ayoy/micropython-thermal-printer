#!/usr/bin/python

from Adafruit_Thermal import *
from machine import Pin

# Feel free to experiment with heatdots, heattime and heatiniterval
# to nail down your printer's sweet spot :)
printer = Adafruit_Thermal(pins=(Pin.exp_board.G14,), heatdots=5, heatinterval=40)

# Test inverse on & off
printer.inverseOn()
printer.println("Inverse ON")
printer.inverseOff()

# Test character double-height on & off
printer.doubleHeightOn()
printer.println("Double Height ON")
printer.doubleHeightOff()

# Set justification (right, center, left) -- accepts 'L', 'C', 'R'
printer.justify('R')
printer.println("Right justified")
printer.justify('C')
printer.println("Center justified")
printer.justify('L')
printer.println("Left justified")

# Test more styles
printer.boldOn()
printer.println("Bold text")
printer.boldOff()

printer.underlineOn()
printer.println("Underlined text")
printer.underlineOff()

printer.setSize('L')   # Set type size, accepts 'S', 'M', 'L'
printer.println("Large")
printer.setSize('M')
printer.println("Medium")
printer.setSize('S')
printer.println("Small")

printer.justify('C')
printer.println("normal\nline\nspacing")
printer.setLineHeight(50)
printer.println("Taller\nline\nspacing")
printer.setLineHeight() # Reset to default
printer.justify('L')

# Change printer settings for smoother barcodes
printer = Adafruit_Thermal(pins=(Pin.exp_board.G14,), heatdots=4, heattime=120, heatinterval=80)

# Barcode examples
printer.feed(1)
# CODE39 is the most common alphanumeric barcode
printer.printBarcode("ADAFRUT", printer.CODE39)
printer.setBarcodeHeight(100)
# Print UPC line on product barcodes
printer.printBarcode("123456789123", printer.UPC_A)
time.sleep(2)

# These settings allow for much cleaner output when printing images
printer = Adafruit_Thermal(pins=(Pin.exp_board.G14,), heatdots=1, heattime=155, heatinterval=1)

# # Print the 75x75 pixel logo in adalogo.py
import adalogo
printer.printBitmap(adalogo.width, adalogo.height, adalogo.data, LaaT=True)
printer.println("Adafruit!")

try:
    # # Print the 135x135 pixel QR code stored in the file on disk
    printer.printBitmapFromFile(135, 135, '/flash/gfx/qrcode')

    # TODO: figure out what's wrong here
    time.sleep(2)

    # # Print some .bmp bitmap images
    printer.printBMPImage('/flash/gfx/aykm.bmp')
    printer.printBMPImage('/flash/gfx/notbad.bmp')
except OSError as e:
    print(e.errno)
    pass

printer.feed(3)

# printer.sleep()      # Tell printer to sleep
# printer.wake()       # Call wake() before printing again, even if reset
# printer.setDefault() # Restore printer to defaults
