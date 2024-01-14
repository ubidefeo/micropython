The following files are custom built for the LilyGo T-QT Pro with 128x128 TFT display but should work on most ESP32-S3-FN4R2 without external Flash and RAM with internal 4MiB of flash.

This firmware supports configurations with and without SPIRAM (also known as PSRAM) and will auto-detect a connected SPIRAM chip at startup and allocate the MicroPython heap accordingly. However if your board has Octal SPIRAM, then use the "spiram-oct" variant.
