'''
Created on Apr 15, 2014

@author: derussis

Copyright (c) 2014 Luigi De Russis
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
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