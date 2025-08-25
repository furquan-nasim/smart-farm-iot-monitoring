import time
import json
import random
import ssl
import paho.mqtt.client as mqtt

# ---------- CONFIG ----------
ENDPOINT = "a2rfxkrlzbtxoj-ats.iot.us-east-1.amazonaws.com"   # Replace with your AWS IoT Core endpoint
CLIENT_ID = "sim-01"                           # Same as Thing name
TOPIC = "farm/sensors"                         # MQTT topic where data is published

# Certificates (downloaded when creating the certificate)
CA_PATH = "AmazonRootCA1.pem"
CERT_PATH = "device.cert.pem"
KEY_PATH = "private.key.pem"
# ----------------------------


# Callback when connection succeeds
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to AWS IoT Core!")
        client.subscribe(TOPIC)  # Optional: subscribe back to same topic
    else:
        print("❌ Connection failed. Code:", rc)


# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"📩 Message received from topic {msg.topic}: {msg.payload.decode()}")


# Initialize MQTT client
client = mqtt.Client(client_id=CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message

# Configure TLS/SSL authentication
client.tls_set(
    ca_certs=CA_PATH,
    certfile=CERT_PATH,
    keyfile=KEY_PATH,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# Connect
client.connect(ENDPOINT, 8883, keepalive=60)
client.loop_start()

# Publish random sensor data every 5 seconds
try:
    while True:
        payload = {
            "deviceId": "sim-01",   # ✅ Added deviceId
            "temperature": round(random.uniform(20, 35), 2),
            "moisture": round(random.uniform(30, 70), 2),
            "ph": round(random.uniform(5.5, 7.5), 2),
            "timestamp": int(time.time())
        }
        client.publish(TOPIC, json.dumps(payload), qos=1)
        print(f"📤 Sent: {payload}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Simulation stopped.")
    client.loop_stop()
    client.disconnect()
