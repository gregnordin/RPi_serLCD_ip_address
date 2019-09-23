import datetime
import subprocess
import time

from serlcd import SerLCD

def connect_type(word_list):
    """ This function takes a list of words, then, depeding which key word, returns the corresponding
    internet connection type as a string. ie) 'ethernet'.
    """
    if 'wlan0' in word_list or 'wlan1' in word_list:
        con_type = 'WiFi'
    elif 'eth0' in word_list:
        con_type = 'Ethernet'
    else:
        con_type = 'current'
    return con_type

time.sleep(30)

lcd = SerLCD()

lcd.setBacklight(64, 64, 64)
lcd.noCursor()
lcd.clear()

arg='ip route list'  # Linux command to retrieve ip addresses.
# Runs 'arg' in a 'hidden terminal'.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.

# Split IP text block into three, and divide the two containing IPs into words.
ip_lines = data[0].splitlines()
split_line_a = ip_lines[0].decode().split()
split_line_b = ip_lines[1].decode().split()

# con_type variables for the message text. ex) 'ethernet', 'wifi', etc.
ip_type_a = connect_type(split_line_a)
ip_type_b = connect_type(split_line_b)

"""Because the text 'src' is always followed by an ip address,
we can use the 'index' function to find 'src' and add one to
get the index position of our ip.
"""
ipaddr_a = split_line_a[split_line_a.index('src')+1]
ipaddr_b = split_line_b[split_line_b.index('src')+1]

# Creates a sentence for each ip address.
my_ip_a1 = '%s IP:' % (ip_type_a)
my_ip_a2 = '%s' % (ipaddr_a)
my_ip_b = '%s IP: %s' % (ip_type_b, ipaddr_b)

# date_and_time = datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
# print(date_and_time)
# print(my_ip_a1)
# print(my_ip_a2)

lcd.write(my_ip_a1)
lcd.setCursor(0, 1)
lcd.write(my_ip_a2)
