# MicroPython Thermal Printer
This is the MicroPython port of Python Thermal Printer by Adafruit, available [elsewhere on GitHub](https://github.com/adafruit/Python-Thermal-Printer).

Read the full story at https://kapusta.cc/2017/12/11/thermal-printer-library-for-micropython/.

## The summary of changes

1. Removed Python 2.x code
1. Removed `writeToStdout()`
1. Replaced `Serial` with `machine.UART`
1. Removed support for pre-2.68 firmware
1. Removed image printing method, because it depended on Python Imaging Library
1. Disabled calls to `wake()` and `reset()` at initialization
1. Fixes to `sleepAfter()` and `wake()`

## Additions

* `printBitmapFromFile()` - allows for printing the bitmap from file on disk, instead of reading it from array of bytes like `printBitmap()` does.
* `printBMPImage()` - allows for printing the actual .bmp image. Supports 1-bit Windows BMP format only, up to 384px wide.
* heat dots, heat time and heat interval settings are parametrized in the initializer to fine tune printer output.

## Usage

See [printertest.py]( https://github.com/ayoy/micropython-thermal-printer/blob/master/printertest.py) for usage example.

## Testing

So far I tested it only with LoPy version 1. Works fine, besides printing large bitmaps that required too much memory for the LoPy (for the bitmap provided with printertest.py) - hence `printBitmapFromFile()`.
