#ifndef MICROPY_HW_BOARD_NAME
// Can be set by mpconfigboard.cmake.
#define MICROPY_HW_BOARD_NAME "LilyGo T-QT Pro"
#endif
#define MICROPY_HW_MCU_NAME "ESP32S3"

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL (1)

#define MICROPY_HW_I2C0_SCL (44)
#define MICROPY_HW_I2C0_SDA (43)

#define MICROPY_BOARD_STARTUP LILYGO_TQT_PRO_ESP32_board_startup
void LILYGO_TQT_PRO_ESP32_board_startup(void);
