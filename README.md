# STM32H7 System-on-Module
## Overview
This STM32H7 system-on-module is everything needed to get the MCU up and running. Simply place a footprint for the board-to-board connectors on your motherboard, and use whatever pins your project needs!

## Hardware
The system-on-module is a powerful compute source with everything you need for intensive computation. Peripherals include:
- STM32H743ZGT6 32Bit MCU
- AS4C8M16SA-7TCN 128MBit SDRAM
- AT25FF161A-SSHN-T 16MBit QSPI Flash
- CP2102N-A02-GQFN20R USB-to-UART Bridge

The system on module has a point-of-load regulator (TPSM861253RDXR) to ensure stable, efficient power delivery to on-board peripherals.

## Firmware
Included in this repository is a device tree file and other necessary files for building a zephyr image. The **fw/** README.md file gives instructions for building on a Linux system.

> TODO: Write instructions for Windows use. 
