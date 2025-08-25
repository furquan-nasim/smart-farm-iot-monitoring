import ssl
import paho.mqtt.client as mqtt

ENDPOINT = "a2rfxkrlzbtxoj-ats.iot.us-east-1.amazonaws.com"  # your endpoint
CLIENT_ID = "sim-01"
TOPIC = "test/connection"

CA_PATH = "AmazonRootCA1.pem"
CERT_PATH = "device.cert.pem"
KEY_PATH = "private.key.pem"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to AWS IoT Core!")
        client.publish(TOPIC, "Hello from sim-01", qos=1)
        print("📤 Test message published!")
    else:
        print("❌ Connection failed with code:", rc)

client = mqtt.Client(client_id=CLIENT_ID)
client.on_connect = on_connect

client.tls_set(
    ca_certs=CA_PATH,
    certfile=CERT_PATH,
    keyfile=KEY_PATH,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

client.connect(ENDPOINT, 8883, 60)
client.loop_forever()
