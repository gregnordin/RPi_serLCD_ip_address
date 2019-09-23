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

`~/Documents/Projects/raspberry_pi/RPi_serLCD_ip_address`

    $ ls -l
    total 32
    -rw-r--r--  1 nordin  staff  1722 Sep 21 19:36 ip_address_on_serLCD.py
    -rw-r--r--@ 1 nordin  staff  3009 Sep 21 19:38 notest-Set up Raspberry Pi with 20x4 LCD to show IP address.md
    -rwxr-xr-x@ 1 nordin  staff  6533 Mar 20  2019 serlcd.py


From `~/Documents/Projects/raspberry_pi/RPi_serLCD_ip_address` copy files to RPi:

    rsync -aP --exclude='__pycache__' --exclude='.git/' --exclude='.gitignore' --exclude='.DS_Store' . pi@10.37.203.150:/home/pi/code/serlcd_ip_address/
    
    
    
    
## Set up python script to run every time RPi starts up

1) Set file permissions to be able to be executed on startup: `chmod 755 ip_address_on_serLCD.py` (This is not really needed)

2) Make it run on startup by: 

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Run `sudo nano /etc/rc.local`   

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add the line `python3 /home/pi/code/RPi_email_ip_address/startup_mailer.py > home/pi/code/RPi_email_ip_address/startup_mailer.log 2>&1` at the bottom of file on the line before `exit 0`    

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Save and exit with `<Cntl+o>` then `<Enter>` then `<Cntl+x>`  

3) Test with `sudo reboot` and see if you get the email. The email will send 30 seconds after boot (to allow time for the internet to connect itself)

# Alternative with Adafruit LCD display

[How to Find IP Address of Raspberry Pi using Python Script](https://circuitdigest.com/microcontroller-projects/display-ip-address-of-raspberry-pi)

