# wifi-qr

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub stars](https://img.shields.io/github/stars/jtprogru/wifi-qr.svg)](https://github.com/jtprogru/wifi-qr/stargazers)
[![GitHub issues](https://img.shields.io/github/issues-raw/jtprogru/wifi-qr)](https://github.com/jtprogru/wifi-qr/issues)
[![GitHub](https://img.shields.io/github/license/jtprogru/wifi-qr)](https://github.com/jtprogru/wifi-qr/)

Simple script for generate QR-code for connect to WiFi.

## Documentation

See code - this script is VERY simple :)

## Environment Variables

Before a running script, please create file `.env` like this:

```ini
export WIFI_SSID=MyHomeWiFiSSID
export WIFI_PASSWD=MyHomeWiFiPassword
```

## Run locally


```shell
# Create virtual environment
# with default system Python 3.x
make venv
# Run QR-code generator
make run
```

After running you can open PNG-file and scan this file with your smartphone.

## Feedback

For feedback please create [issues](https://github.com/jtprogru/wifi-qr/issues).

## Authors

- Michael (jtprogru) Savin
  - :octocat: [@jtprogru](https://github.com/jtprogru)
  - :bird: [@jtprogru](https://www.twitter.com/jtprogru)
  - :moneybag: [savinmi.ru](https://savinmi.ru)


## License

[WTFPL](LICENSE)

