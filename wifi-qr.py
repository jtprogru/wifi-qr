#!/usr/bin/env python3

import os
import sys

import pyqrcode


def main():
    WIFI_SSID = os.getenv("WIFI_SSID", None)
    WIFI_PROTOCOL = "WPA"
    WIFI_PASSWD = os.getenv("WIFI_PASSWD", None)
    WIFI_FILENAME = f"{WIFI_SSID}.png"

    if (WIFI_SSID is None) or (WIFI_PASSWD is None):
        print("ERROR - WIFI not set in environment")
        print("Please see in README.md")
        sys.exit(1)

    # About shis string please see in Wikipedia
    # https://en.wikipedia.org/wiki/QR_code#Joining_a_Wi%E2%80%91Fi_network
    qrstr = f"WIFI:S:{WIFI_SSID};T:{WIFI_PROTOCOL};P:{WIFI_PASSWD};;"

    qr = pyqrcode.create(qrstr)
    qr.png(WIFI_FILENAME, scale=10)

    print(f"QR-code saved in {WIFI_FILENAME}")
    print("Please open this file in any image viewer")
    print("and scan this QR-code with your smartphone")


if __name__ == "__main__":
    main()
    sys.exit(0)
