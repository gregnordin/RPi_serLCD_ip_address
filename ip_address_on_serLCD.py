import time

from serlcd import SerLCD

lcd = SerLCD()

lcd.setBacklight(64, 64, 64)
lcd.noCursor()
lcd.clear()
lcd.write("Hello World!")
lcd.setCursor(0, 1)
lcd.write("Line 2")
lcd.setCursor(0, 2)
lcd.write("Line 3")

time.sleep(2)
lcd.clear()
