
from umqtt.robust import MQTTClient
import dht
import machine
import time
import sys



dht_pin = machine.Pin(14)
d = dht.DHT22(dht_pin)


c = MQTTClient("UfvkGJlABz6l7Eam72312", '178.128.40.119', user='UfvkGJlABz6l7Eam74v4', password='')
c.connect()





while True:

	d.measure()
	c.publish(b"v1/devices/me/telemetry", b'{"temperature": '+str(d.temperature())+', "humidity": '+str(d.humidity())+'}')
	time.sleep(10)
	print([d.temperature()],[d.humidity()])



c.disconnect()


