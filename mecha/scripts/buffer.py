import paho.mqtt.client as mqtt

broker_url = "103.20.207.171"
broker_port = 1883
topic="ldb01/posx"
payload = "eiei za 229"

def on_message(client, userdata, message):
   x=message.payload.decode()
   print("Message Recieved: "+x)
   print(x.strip()=="hi")
   
       
client = mqtt.Client()

client.on_message = on_message
print(client.connect(broker_url, broker_port))
client.publish(topic, payload, qos=0, retain=False)
client.subscribe(topic, qos=0)

client.loop_forever()
