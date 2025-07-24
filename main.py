import network
import time
import dht
import machine
from umqtt.simple import MQTTClient
import random  # untuk perubahan nilai suhu dan kelembapan

# --- Konfigurasi WiFi ---
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# --- Konfigurasi Adafruit IO ---
ADAFRUIT_IO_USERNAME = "msalmanrafadhlih"
ADAFRUIT_IO_KEY = "aio_bgqm06kr4hnnslNOgYLbrh5hWyjd"
MQTT_SERVER = "io.adafruit.com"
MQTT_PORT = 1883

# --- Topic MQTT (format: username/feeds/nama_feed) ---
TOPIC_SUHU = f"{ADAFRUIT_IO_USERNAME}/feeds/suhu"
TOPIC_HUMID = f"{ADAFRUIT_IO_USERNAME}/feeds/kelembapan"

# --- Koneksi WiFi ---
print("Menghubungkan ke WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    time.sleep(1)
print("WiFi Terhubung!")

# --- Inisialisasi Sensor DHT22 ---
sensor = dht.DHT22(machine.Pin(15))

# --- Koneksi MQTT ---
client = MQTTClient("esp32", MQTT_SERVER, user=ADAFRUIT_IO_USERNAME, password=ADAFRUIT_IO_KEY, port=MQTT_PORT)
client.connect()
print("Terhubung ke Adafruit IO!")

# --- Variabel awal untuk simulasi suhu & kelembapan ---
simulasi_suhu = 25.0
simulasi_kelembapan = 50.0

# --- Loop utama ---
while True:
    try:
        # Sensor tetap diaktifkan untuk kompatibilitas, tapi tidak digunakan sebagai nilai langsung
        sensor.measure()

        # Buat fluktuasi acak yang signifikan antara -3.0 sampai +3.0
        simulasi_suhu += random.uniform(-3.0, 3.0)
        simulasi_kelembapan += random.uniform(-5.0, 5.0)

        # Batasi nilai agar tidak di luar batas wajar
        simulasi_suhu = max(15, min(simulasi_suhu, 40))
        simulasi_kelembapan = max(20, min(simulasi_kelembapan, 90))

        # Cetak hasil
        print("Suhu:", round(simulasi_suhu, 2), "°C | Kelembapan:", round(simulasi_kelembapan, 2), "%")

        # Kirim ke MQTT
        client.publish(TOPIC_SUHU, str(round(simulasi_suhu, 2)))
        client.publish(TOPIC_HUMID, str(round(simulasi_kelembapan, 2)))

    except Exception as e:
        print("Error:", e)

    time.sleep(60)  # delay 1 menit
