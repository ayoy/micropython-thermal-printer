# MicroPython Thermal Printer
This is the MicroPython port of Python Thermal Printer by Adafruit, available [elsewhere on GitHub](https://github.com/adafruit/Python-Thermal-Printer).

## The summary of changes

1. Removed Python 2.x code
1. Removed `writeToStdout()`
1. Replaced `Serial` with `machine.UART`
1. Removed support for pre-2.68 firmware
1. Removed image printing method, because it depended on Python Imaging Library
1. Disabled calls to `wake()` and `reset()` at initialization
1. Fixes to `sleepAfter()` and `wake()`
1. Parametrized heat dots and heat interval settings for various versions of printers

## Usage

See [printertest.py]( https://github.com/ayoy/micropython-thermal-printer/blob/master/printertest.py) for usage example.

## Testing

So far I tested it only with LoPy version 1. Works fine, besides printing bitmaps that requires too much memory for the LoPy (for the bitmap provided with printertest.py).
