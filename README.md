# alarmclock

Neopixel matrix alarmclock. Based on a 32x8 neopixel matrix.

# Software Installation
1. You need at least rp2-pico-w-20220914-unstable-v1.19.1-409-g0e8c2204d.uf2 for the webrepl support. See [WebREPL für den Raspberry PI Pico W](https://www.pluess.li/2022/09/17/webrepl-fuer-den-raspberry-pi-pico-w)
2. Clone/Copy the whole project
3. Create a secrets.py file to set your WLAN ssid und password
   ```python
   ssid = 'your SSID'
   password = 'your very secret password'
   ```
4. The default webrepl password is `einstein`. You can change is in `webrepl_cfg.py`
5. Default logging level ist INFO. See can set an other leben in `loguitl.py`.

# Testing
In a microypthon unix port installation do
   ```
   >>> import upip
   >>> upip.install('micropython-unittest')
   ```
   And then on the command line: `micropython alltests.py`

# Hardware

Disclaimer: Affiliate Links

* [Raspberry Pi Pico W](https://amzn.to/3RcdRRv)
* [8x32 Neopixel Matrix](https://s.click.aliexpress.com/e/_DEMup7D)

# References

* https://github.com/blaz-r/pi_pico_neopixel
* https://github.com/robhagemans/hoard-of-bitfonts
* https://github.com/robhagemans/monobit
* https://github.com/pfalcon/pycopy-lib/tree/master/logging
* https://www.pluess.li/2022/09/22/logging-mit-micropython/
* https://www.pluess.li/2022/09/17/webrepl-fuer-den-raspberry-pi-pico-w/
