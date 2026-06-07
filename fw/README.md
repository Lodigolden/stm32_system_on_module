# Overview
> NOTE: This file assums the user has Zephyr installed in a location easily accessible from any terminal. 

> TODO: All commands here are for a Linux system. Update w/ Windows commands.

## Developing
Use the following commands to start developing when using linux:
> source ~/zephyrproject/.venv/bin/activate

> source ~/zephyrproject/zephyr/zephyr-env.sh

## Building and Flashing
Use the following command:
> python scripts/flash_uart.py -b -f

- The -b argument builds the project.
- The -f argument flashes the SOM.

## Accessing SOM Terminal
Use the following command:
> screen /dev/ttyUSB0 57600
