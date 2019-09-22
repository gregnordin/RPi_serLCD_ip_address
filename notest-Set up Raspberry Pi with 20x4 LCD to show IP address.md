# Set up Raspberry Pi with 20x4 LCD to show IP address

## First talk to serLCD

Follow [AVR-Based Serial Enabled LCDs Hookup Guide](https://learn.sparkfun.com/tutorials/avr-based-serial-enabled-lcds-hookup-guide/all#i2c-hardware-hookup--example-code---basic) to hook up [SparkFun 20x4 SerLCD - Black on RGB 3.3V](https://www.sparkfun.com/products/14074) to Raspberry Pi 3B+ I2C1 to LCD's I2C.

Enable I2C on RPi.

Follow [this Sparkfun tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi) to set up RPi software.

`ssh` into RPi

    pi@raspberrypi:~ $ i2cdetect -y 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- 72 -- -- -- -- --

Get [sparkfun_serlcd.py](shigeru-kawaguchi/Python-SparkFun-SerLCD) and rename serlcd.py. Copy to RPi.

Try out using this code to write to LCD:

    pi@raspberrypi:~/code/serlcd_ip_address $ python3
    Python 3.7.3 (default, Apr  3 2019, 05:39:12)
    [GCC 8.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from serlcd import SerLCD
    >>> ls
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'ls' is not defined
    >>> lcd = SerLCD()
    >>> lcd.setBacklight(64, 64, 64)
    >>> lcd.noCursor()
    >>> lcd.write("Hello World!")
    >>> lcd.setCursor(0, 1)
    >>> lcd.write("Line 2")
    >>> lcd.write("Line 3")
    >>> lcd.setCursor(0, 2)
    >>> lcd.write("Line 3")
    >>> lcd.setCursor(0, 0)
    >>> lcd.write("aa")
    >>> lcd.clear()
    
Everything works great.

## Develop code to show ip address

