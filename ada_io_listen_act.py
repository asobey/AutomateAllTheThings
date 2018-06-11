#!python3
# Adafruit IO Listen and Act
# Listen to Adafruit IO server and act.

from Adafruit_IO import MQTTClient
import os, time, yaml


def accessPrivateYAML(yaml_name):
    with open(yaml_name, 'r') as private:
        try:
            privateData = yaml.load(private)
            return(privateData)
        except yaml.YAMLError as exc:
            print(exc)

def connected(client):
    client.subscribe('tv_audio_state')

def message(client, feed_id, payload):
    print('Feed: %s; Payload: %s' % (feed_id, payload))
    if payload == 'tv_audio_ON':
        #Turn On TV and change input source
        os.system('irsend SEND_ONCE lircdLG KEY_POWER')
        time.sleep(12)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_POWER')
    if payload == 'switch_to_roku':
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_SELECT')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_EXIT')
    if payload == 'switch_to_live':
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1.5)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_SELECT')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_EXIT')

    if payload == 'tv_roku_ON':
        #Turn On TV and change input source
        os.system('irsend SEND_ONCE lircdLG KEY_POWER')
        os.system('irsend SEND_ONCE lircdSoundBar KEY_Power')
        time.sleep(8)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1.5)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_I')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_SELECT')
        time.sleep(1)
        os.system('irsend SEND_ONCE lircdLG KEY_EXIT')
        print("Message Recieved, TV & Roku ON")
    if payload == 'tv_audio_OFF':   # Turn Off TV and SoundBar
        os.system('irsend SEND_ONCE lircdLG KEY_POWER')
        os.system('irsend SEND_ONCE lircdSoundBar KEY_Power')
    if payload == 'volume_up':      # Turn Volume Up
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEUP')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEUP')
    if payload == 'volume_down':   # Turn Volume Down
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEDOWN')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEDOWN')
    if payload == 'volume_up3':      # Turn Volume Up
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEUP')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEUP')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEUP')
    if payload == 'volume_down3':   # Turn Volume Down
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEDOWN')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEDOWN')
        time.sleep(2)
        os.system('irsend SEND_ONCE lircdSoundBar KEY_VOLUMEDOWN')
    if payload == 'sound_OnOff':    # Change sound state
        os.system('irsend SEND_ONCE lircdSoundBar KEY_Power')


if __name__ == '__main__':

    privateData = accessPrivateYAML('AdafruitPrivate.yaml')

    client = MQTTClient(privateData['AdaUserName'], privateData['AdaAPI'])

    # Setup the callback functions defined above:
    print('setting up client functions...')
    client.on_connect = connected
    client.on_message = message

    print('connecting to client...')
    client.connect()
    print('conncted and listening!')
    # pick one of the followingt 3 ways of looping the MQTT cleint
    # client.loop_background() # start background thread and return
    # client.loop() # loop once
    client.loop_blocking() # block forever on client loop
