# Include(s)
import argparse
from pathlib import Path
import subprocess

# User Commands
build_command = "west build -p always -b som"
flash_command = "stm32flash -b 115200 -m 8e1 -w build/zephyr/zephyr.bin -v -g 0x08000000 /dev/ttyUSB0"

#---------------------------------------------------------------------------------------------------
def main():
    # User arguments
    parser = argparse.ArgumentParser(description="A script for building and flashing the SOM")

    parser.add_argument('-b', '--build', action='store_true')
    parser.add_argument('-f', '--flash', action='store_true')

    args = parser.parse_args()

    target_dir = Path(__file__).resolve().parents[1]

    if args.build:
        subprocess.run([build_command], shell=True, cwd=target_dir)
    if args.flash:
        subprocess.run([flash_command], shell=True, cwd=target_dir)

#---------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
