"""ESP32-S3-LCD-1.28
https://www.waveshare.com/wiki/ESP32-S3-LCD-1.28
Firmware: ESP32_GENERIC/firmware_16MiB.bin
"""

from machine import Pin, SPI
import gc9a01

TFA = 0
BFA = 0
WIDE = 0
TALL = 1

LCD_RS = 4
LCD_MOSI = 5
LCD_SCK = 6
LCD_CS = 7
LCD_RST = 8
LCD_BL = 9


def Display(rotation=0, buffer_size=0, options=0):
    spi = SPI(1, baudrate=60000000, sck=Pin(LCD_SCK), mosi=Pin(LCD_MOSI))

    return gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(LCD_RST, Pin.OUT),
        cs=Pin(LCD_CS, Pin.OUT),
        dc=Pin(LCD_RS, Pin.OUT),
        backlight=Pin(LCD_BL, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )


ENC_A = 41
ENC_B = 40
ENC_BUTTON = 42
WAKE_BUTTON = ENC_BUTTON

from rotary_irq_esp import RotaryIRQ


def Dial(min_val=0, max_val=100):
    return RotaryIRQ(ENC_A, ENC_B, min_val, max_val, False, RotaryIRQ.RANGE_WRAP, False)
