import yaml

from Adafruit_IO import MQTTClient

def accessPrivateYAML(yaml_name):
    with open(yaml_name, 'r') as private:
        try:
            privateData = yaml.load(private)
            return(privateData)
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == '__main__':

    privateData = accessPrivateYAML('AdafruitPrivate.yaml')
    print(privateData['AdaAPI'])
    mqtt = MQTTClient(privateData['AdaAPI'])

    mqtt.send('speedtest_download', 666)
