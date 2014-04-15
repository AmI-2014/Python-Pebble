'''
Created on Apr 15, 2014

@author: derussis
'''

import pebblelibs.pebble as libpebble
import time

if __name__ == '__main__':
    # create a new Pebble object
    pebble = libpebble.Pebble()
    
    # set the Pebble ID (MAC address)
    pebble.id = '00:17:E9:6D:31:04'
    
    # init PBL log 
    pebble.print_pbl_logs = False
    
    # compose a message to send to the watch, before opening the connection to the watch
    print "Prepare the message to send to the watch, please!"
    sender = raw_input('Sender: ')
    message = raw_input('Message: ')
    
    # connect via Bluetooth
    pebble.connect_via_lightblue()
    
    print "Sending the message..."
    # send the message as a SMS notification
    pebble.notification_sms(sender, message)
    
    # wait 10 seconds...
    time.sleep(10)
    
    # send a ping, too
    print "Send ping..."
    print "Ping sent with data " + str(pebble.ping())
    
    # close the connection with the Pebble
    pebble.disconnect()