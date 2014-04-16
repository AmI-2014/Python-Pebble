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
import rest, time

# the base url
base_url = 'http://localhost:8080' 

def control_music(command, url):
    
    # init json content for PUT requests
    data = '{ }'
    
    # check if I need to play or stop music...
    if command == 'PLAYPAUSE':
        # get the music server status
        status = rest.send(url = base_url + '/api/v1/player')
        
        if status['status'] == 'playing':
            url = url + 'stop'
        else:
            url = url + 'play'
            # read the playlist
            playlist = open('playlist.json')
            data = playlist.read()
    
    # execute the command
    rest.send('PUT', base_url + url, data, { 'Content-Type':'application/json' })
    
    # update the track metadata
    update_metadata()
    
def update_metadata():
    # init
    artist = ""
    title = "No Music Found"
    album = ""
    
    # get current track metadata as string
    queue = rest.send(url = base_url + '/api/v1/player')
    if queue and queue['current']:
        artist = str(queue['current']['artist'])
        title = str(queue['current']['title'])
        album = str(queue['current']['album'])
    
    pebble.set_nowplaying_metadata(title, album, artist)

def music_handler(endpoint, response):
    control_events = {
                      "PLAYPAUSE": "/api/v1/player/",
                      "NEXT": "/api/v1/player/next"
                      }
    if response in control_events:
        control_music(response, control_events[response])

if __name__ == '__main__':
    # create a new Pebble object
    pebble = libpebble.Pebble()
    
    # pebble MAC address
    pebble.id = '00:17:E9:6D:31:04'
    
    # init PBL log
    pebble.print_pbl_logs = False
    
    # connect via Bluetooth
    pebble.connect_via_lightblue()
    
    # register as music handler
    pebble.register_endpoint("MUSIC_CONTROL", music_handler)
    
    # wait for data...
    try:
        while True:
            update_metadata()
            time.sleep(5)
    except KeyboardInterrupt:
        # close the connection with the Pebble
        pebble.disconnect()