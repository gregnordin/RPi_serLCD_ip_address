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
    
    
## Set up python script to run every time RPi starts up

Make`serlcd.py` run on startup by: 

1) Edit `rc.local`

- Run `sudo nano /etc/rc.local`   
- Add the line `python3 /home/pi/code/RPi_email_ip_address/serlcd.py > home/pi/code/RPi_email_ip_address/serlcd.log 2>&1` at the bottom of file on the line before `exit 0`    
- Save and exit with `<Cntl+o>` then `<Enter>` then `<Cntl+x>`  

2) Test with `sudo reboot` and see if the IP address is shown on the serLCD. This should happen 30 seconds after boot (to allow time to connect to the internet)


# Alternative using Adafruit LCD display

[How to Find IP Address of Raspberry Pi using Python Script](https://circuitdigest.com/microcontroller-projects/display-ip-address-of-raspberry-pi)


# Old - disregard

## Develop code to show ip address

Contents of `~/Documents/Projects/raspberry_pi/RPi_serLCD_ip_address`

    $ ls -l
    -rw-r--r--@ 1 nordin  staff  3454 Sep 23 10:20 README.md
    -rw-r--r--  1 nordin  staff  1730 Sep 23 10:08 ip_address_on_serLCD.py
    -rwxr-xr-x@ 1 nordin  staff  6533 Mar 20  2019 serlcd.py


From `~/Documents/Projects/raspberry_pi/RPi_serLCD_ip_address` copy files to RPi:

    rsync -P serlcd.py pi@xx.xx.xx.xx:/home/pi/code/serlcd_ip_address/
    
## Change file permissions

1) Set file permissions to be able to be executed on startup: `chmod 755 ip_address_on_serLCD.py` (This is not really needed)




